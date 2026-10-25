# PySpark: Reliable Bronze-to-Gold ETL

**Type:** Supplemental original exercise
**Sources:** [Apache Spark SQL guide](https://spark.apache.org/docs/latest/sql-programming-guide.html) · [Databricks medallion architecture](https://docs.databricks.com/aws/en/lakehouse/medallion)
**Focus:** ETL, large datasets, schema handling, quality, deduplication, aggregation

## Exercise

An append-only object store receives payment events with `event_id`, `customer_id`, `amount`, `event_time`, and `ingested_at`. Build transformations that preserve raw input, quarantine invalid events, keep the latest valid copy of each duplicate event, and produce daily revenue per customer.

Example input rows (timestamps are UTC):

| event_id | customer_id | amount | event_time | ingested_at |
|---|---|---:|---|---|
| e1 | C1 | 10.00 | 2026-10-12 10:00 | 2026-10-12 10:01 |
| e1 | C1 | 10.00 | 2026-10-12 10:00 | 2026-10-12 10:05 |
| e2 | C1 | 2.50 | 2026-10-12 11:00 | 2026-10-12 11:01 |
| e3 | C2 | `bad` | 2026-10-12 11:20 | 2026-10-12 11:21 |

Expected transformation results: Bronze retains all 4 source rows; the invalid/quarantine output contains `e3`; Silver contains the latest `e1` plus `e2`; Gold contains one row: `(2026-10-12, C1, 12.50, 2)` for `(event_date, customer_id, daily_revenue, event_count)`.

## Solution

This code assumes a `SparkSession` named `spark` already exists and input arrives as a DataFrame. It returns three DataFrames so orchestration can persist each output to the chosen Delta/lake tables.

```python
from pyspark.sql import DataFrame
from pyspark.sql import Window
from pyspark.sql import functions as F


def transform_payment_events(raw: DataFrame) -> tuple[DataFrame, DataFrame, DataFrame]:
    bronze = raw.withColumn("_ingested_at", F.current_timestamp())

    typed = (
        bronze
        .withColumn("event_id", F.trim(F.col("event_id").cast("string")))
        .withColumn("customer_id", F.trim(F.col("customer_id").cast("string")))
        .withColumn("amount", F.col("amount").cast("decimal(18, 2)"))
        .withColumn("event_time", F.to_timestamp("event_time"))
        .withColumn("ingested_at", F.to_timestamp("ingested_at"))
    )

    valid_condition = (
        F.col("event_id").isNotNull()
        & (F.col("event_id") != "")
        & F.col("customer_id").isNotNull()
        & (F.col("customer_id") != "")
        & F.col("amount").isNotNull()
        & (F.col("amount") >= F.lit(0))
        & F.col("event_time").isNotNull()
        & F.col("ingested_at").isNotNull()
    )

    invalid = typed.filter(~valid_condition)
    valid = typed.filter(valid_condition)

    latest_event = Window.partitionBy("event_id").orderBy(
        F.col("ingested_at").desc()
    )
    silver = (
        valid
        .withColumn("_row_number", F.row_number().over(latest_event))
        .filter(F.col("_row_number") == 1)
        .drop("_row_number")
    )

    gold = (
        silver
        .groupBy(F.to_date("event_time").alias("event_date"), "customer_id")
        .agg(
            F.sum("amount").alias("daily_revenue"),
            F.countDistinct("event_id").alias("event_count"),
        )
    )

    return bronze, invalid, gold
```

**Production additions:** Persist the raw Bronze input before transformations; write rejected records with a reason code; use a deterministic tie-breaker when ingestion timestamps can match; make writes idempotent (for example, merge by event key); record source-file/lineage metadata; add schema and quality checks; and monitor late-arriving data. For streaming input, define checkpointing and replay behavior explicitly.

**Layer intent:** Bronze preserves source fidelity, Silver is validated and deduplicated, and Gold contains business-ready aggregates. The Gold output here is daily revenue by customer.
