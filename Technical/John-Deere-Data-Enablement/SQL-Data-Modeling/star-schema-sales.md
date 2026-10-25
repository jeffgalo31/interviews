# Sales Warehouse: Star Schema

**Type:** Supplemental original design exercise
**Sources:** [Databricks medallion architecture](https://docs.databricks.com/aws/en/lakehouse/medallion) · [Apache Spark SQL guide](https://spark.apache.org/docs/latest/sql-programming-guide.html)
**Focus:** data modeling, warehouse grain, dimensions, facts, analytics

## Exercise

Design a warehouse model for sales reporting that supports revenue by date, customer, and product. Explain the fact-table grain, key relationships, and how to retain history when a customer's region changes.

Example order lines:

| order_line_id | date | customer | region | product | quantity | net_amount |
|---:|---|---|---|---|---:|---:|
| 1 | 2026-03-01 | C1 | North | P1 | 2 | 20.00 |
| 2 | 2026-03-01 | C1 | North | P2 | 1 | 5.00 |
| 3 | 2026-03-02 | C2 | South | P1 | 1 | 10.00 |

For the March 2026 revenue report, the expected grouped values are `North = 25.00` and `South = 10.00`. The fact grain should preserve one row per order line so product-level analysis remains possible.

## Solution

**Fact grain:** one row per order line. Choose this before defining measures; do not mix order-level and line-level facts in the same table.

```text
DimDate       (date_key PK, full_date, month, quarter, year)
DimCustomer   (customer_key PK, source_customer_id, region, valid_from, valid_to, is_current)
DimProduct    (product_key PK, source_product_id, category, product_name)
FactOrderLine (order_line_id PK, date_key FK, customer_key FK, product_key FK,
               quantity, unit_price, discount_amount, net_amount)
```

- Use integer surrogate keys in dimensions and preserve each source system's natural ID as an attribute.
- Model `DimCustomer` as a Type 2 slowly changing dimension: when a tracked attribute such as region changes, expire the old row and insert a new version. Facts retain the customer key valid at transaction time.
- Store additive measures (`quantity`, `net_amount`) at the chosen grain; document non-additive measures separately.
- Use an explicit unknown dimension row for unresolved or late-arriving dimension data; reconcile it when the dimension arrives.

Example aggregate:

```sql
SELECT d.year,
       d.month,
       c.region,
       SUM(f.net_amount) AS revenue
FROM FactOrderLine AS f
JOIN DimDate AS d ON d.date_key = f.date_key
JOIN DimCustomer AS c ON c.customer_key = f.customer_key
GROUP BY d.year, d.month, c.region
ORDER BY d.year, d.month, c.region;
```

In a lakehouse, raw source records belong in a preserved ingestion layer; validated/conformed records feed this model, and curated business aggregates serve reporting. Databricks describes these as Bronze, Silver, and Gold layers.

**Trade-off to explain:** A star schema duplicates descriptive attributes to make analytics and BI simpler; normalize operational transactions where integrity and update behavior are the priority.
