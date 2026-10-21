<!-- study-layout -->
# SQL Project Planning

🟡 **Medium** · 📁 **Advanced Join** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/sql-projects/problem)

**On this page:** [📝 Problem](#-problem) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

You are given a table, <em>Projects</em>, containing three columns: <em>Task_ID</em>, <em>Start_Date</em> and <em>End_Date</em>. It is guaranteed that the difference between the <em>End_Date</em> and the <em>Start_Date</em> is equal to <em>1</em> day for each row in the table.

| Column | Type |
|---|---|
| Task_ID | Integer |
| Start_Date | Date |
| End_Date | Date |

If the <em>End_Date</em> of the tasks are consecutive, then they are part of the same project. Samantha is interested in finding the total number of different projects completed.

Write a query to output the start and&nbsp;end dates of projects listed by the number of days it took to complete the project in ascending order. If there is more than one project that have the same number of completion days, then order by the start date of the project.

## 🧪 Example

**Input**

| Task_ID | Start_Date | End_Date |
|---|---|---|
| 1 | 2015-10-01 | 2015-10-02 |
| 2 | 2015-10-02 | 2015-10-03 |
| 3 | 2015-10-03 | 2015-10-04 |
| 4 | 2015-10-13 | 2015-10-14 |
| 5 | 2015-10-14 | 2015-10-15 |
| 6 | 2015-10-28 | 2015-10-29 |
| 7 | 2015-10-30 | 2015-10-31 |

**Output**

    2015-10-28 2015-10-29
    2015-10-30 2015-10-31
    2015-10-13 2015-10-15
    2015-10-01 2015-10-04

<br>

**Why**

The example describes following <em>four</em> projects:

<ul>
	<li><em>Project 1</em>: Tasks <em>1</em>, <em>2</em> and <em>3</em> are completed on consecutive days, so these are part of the project. Thus start date of project is <em>2015-10-01</em> and end date is <em>2015-10-04</em>, so it took <em>3 days</em> to complete the project.</li>
	<li><em>Project 2</em>: Tasks <em>4</em>&nbsp;and&nbsp;<em>5</em>&nbsp;are completed on consecutive days, so these are part of the project. Thus, the start date of project is&nbsp;<em>2015-10-13</em>&nbsp;and end date is&nbsp;<em>2015-10-15</em>, so it took&nbsp;<em>2 days</em>&nbsp;to complete the project.</li>
	<li><em>Project 3</em>: Only task <em>6</em>&nbsp;is part of the project. Thus, the start date of project is&nbsp;<em>2015-10-28</em>&nbsp;and end date is&nbsp;<em>2015-10-29</em>, so it took&nbsp;<em>1 day</em>&nbsp;to complete the project.</li>
	<li><em>Project 4</em>: Only task&nbsp;<em>7</em>&nbsp;is part of the project. Thus, the start date of project is&nbsp;<em>2015-10-30</em>&nbsp;and end date is&nbsp;<em>2015-10-31</em>, so it took&nbsp;<em>1 day</em>&nbsp;to complete the project.</li>
</ul>

## 💡 Solution

> [!TIP]
> **Key idea:** A project **starts** on a Start_Date that is nobody's End_Date (no task right before it).

### ✍️ The query

```sql
SELECT s.Start_Date, MIN(e.End_Date)
FROM (SELECT Start_Date FROM Projects WHERE Start_Date NOT IN (SELECT End_Date FROM Projects)) s,
     (SELECT End_Date   FROM Projects WHERE End_Date   NOT IN (SELECT Start_Date FROM Projects)) e
WHERE s.Start_Date < e.End_Date
GROUP BY s.Start_Date
ORDER BY DATEDIFF(MIN(e.End_Date), s.Start_Date), s.Start_Date;
```

### 🔍 How it works

- A project **ends** on an End_Date that is nobody's Start_Date (no task right after it).
- Pair each start with the **first** end after it (`MIN`).
- Sort by length in days (`DATEDIFF` in MySQL, `julianday` difference in SQLite), then by start date.

> [!NOTE]
> **Local SQLite version** ([solution.sql](solution.sql)) differs only where SQLite lacks a MySQL function: `DATEDIFF(a, b)` → `julianday(a) - julianday(b)`.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** the official HackerRank sample (transcribed from HackerRank's images), so the output matches the Example above.

---

⬅️ [Contest Leaderboard](../../basic-join/contest-leaderboard/README.md) · [🗄️ All SQL exercises](../../README.md) · [Placements](../placements/README.md) ➡️
