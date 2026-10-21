<!-- study-layout -->
# Java Date and Time

🟢 **Easy** · 📁 **Introduction** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-date-and-time/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

The [Calendar class](https://docs.oracle.com/javase/7/docs/api/java/util/Calendar.html) is an abstract class that provides methods for converting between a specific instant in time and a set of calendar fields such as YEAR, MONTH, DAY_OF_MONTH, HOUR, and so on, and for manipulating the calendar fields, such as getting the date of the next week.
***

You are given a date. You just need to write the method, $getDay$, which returns the *day* on that date.  To simplify your task, we have provided a portion of the code in the editor.

### Example

$month = 8$
$day = 14$
$year = 2017$

The method should return $MONDAY$ as the day on that date.

```
          AUGUST 2017
SUN MON TUE WED THU FRI SAT
          1   2   3   4   5
  6   7   8   9  10  11  12
 13 [14] 15  16  17  18  19     <- Monday, August 14 (highlighted)
 20  21  22  23  24  25  26
 27  28  29  30  31
```

### Function Description

Complete the *findDay* function in the editor below.

*findDay* has the following parameters:

- *int:* month
- *int:* day
- *int:* year

### Returns

- *string:* the day of the week in capital letters

## 📥 Input & output

### Input format

A single line of input containing the space separated month, day and year, respectively, in $MM$ $DD$ $YYYY$ format.

### Constraints

* $ 2000 < year < 3000 $

## 🧪 Example

**Input**

```
08 05 2015
```

**Output**

```
WEDNESDAY
```

**Why**

The day on August 5th 2015 was `WEDNESDAY`.

> Numbers that appear as formulas on HackerRank are filled in here.

## 💡 Solution

> [!TIP]
> **Key idea:** `Calendar.set(year, month - 1, day)`: Calendar counts months from 0, so August (8) is 7.

### ✍️ The code you write

```java
class Result {

    /*
     * Complete the 'findDay' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts following parameters:
     *  1. INTEGER month
     *  2. INTEGER day
     *  3. INTEGER year
     */

    public static String findDay(int month, int day, int year) {
        Calendar calendar = Calendar.getInstance();
        calendar.set(year, month - 1, day);       // Calendar months start at 0 (January = 0)
        return calendar.getDisplayName(Calendar.DAY_OF_WEEK, Calendar.LONG, Locale.US).toUpperCase();
    }

}
```

### 🔍 How it works

- `getDisplayName(DAY_OF_WEEK, LONG, Locale.US)` gives "Wednesday"; `toUpperCase()` makes it "WEDNESDAY".
- Modern alternative: `java.time.LocalDate.of(year, month, day).getDayOfWeek().name()`.
- HackerRank writes the answer to a file (`OUTPUT_PATH`); the local version writes to the console instead.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/introduction/java_date_and_time/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Int to String](../java_int_to_string/README.md) · [☕ All Java exercises](../../../README.md) · [Java Currency Formatter](../java_currency_formatter/README.md) ➡️
