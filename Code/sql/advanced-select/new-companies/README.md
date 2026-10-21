# New Companies

**Difficulty:** Medium · **Section:** Advanced Select · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/the-company/problem)

Amber's conglomerate corporation just acquired some new companies. Each of the companies follows this hierarchy:

```
Founder → Lead Manager → Senior Manager → Manager → Employee
```

Given the table schemas below, write a query to print the company_code, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees. Order your output by ascending company_code.

**Note:**

- The tables may contain duplicate records.
- The company_code is string, so the sorting should not be numeric. For example, if the company_codes are C_1, C_2, and C_10, then the ascending company_codes will be C_1, C_10, and C_2.

## Input Format

The following tables contain company data:

- **Company:** The company_code is the code of the company and founder is the founder of the company.
- **Lead_Manager:** The lead_manager_code is the code of the lead manager, and the company_code is the code of the working company.
- **Senior_Manager:** The senior_manager_code is the code of the senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company.
- **Manager:** The manager_code is the code of the manager, the senior_manager_code is the code of its senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company.
- **Employee:** The employee_code is the code of the employee, the manager_code is the code of its manager, the senior_manager_code is the code of its senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company.

## Sample Input

> On HackerRank the sample tables are images; rebuilt here from the problem's explanation.

**Company**

| company_code | founder |
|---|---|
| C1 | Monika |
| C2 | Samantha |

**Lead_Manager**

| lead_manager_code | company_code |
|---|---|
| LM1 | C1 |
| LM2 | C2 |

**Senior_Manager**

| senior_manager_code | lead_manager_code | company_code |
|---|---|---|
| SM1 | LM1 | C1 |
| SM2 | LM1 | C1 |
| SM3 | LM2 | C2 |

**Manager**

| manager_code | senior_manager_code | lead_manager_code | company_code |
|---|---|---|---|
| M1 | SM1 | LM1 | C1 |
| M2 | SM3 | LM2 | C2 |
| M3 | SM3 | LM2 | C2 |

**Employee**

| employee_code | manager_code | senior_manager_code | lead_manager_code | company_code |
|---|---|---|---|---|
| E1 | M1 | SM1 | LM1 | C1 |
| E2 | M1 | SM1 | LM1 | C1 |
| E3 | M2 | SM3 | LM2 | C2 |
| E4 | M3 | SM3 | LM2 | C2 |

## Sample Output

```
C1 Monika 1 2 1 2
C2 Samantha 1 1 2 2
```

## Explanation

In company C1, the only lead manager is LM1. There are two senior managers, SM1 and SM2, under LM1. There is one manager, M1, under senior manager SM1. There are two employees, E1 and E2, under manager M1.

In company C2, the only lead manager is LM2. There is one senior manager, SM3, under LM2. There are two managers, M2 and M3, under senior manager SM3. There is one employee, E3, under manager M2, and another employee, E4, under manager, M3.

## Solution

One row per company, and for each level count the **distinct** codes that belong to that company:

```sql
SELECT c.company_code,
       c.founder,
       (SELECT COUNT(DISTINCT lm.lead_manager_code)   FROM Lead_Manager   lm WHERE lm.company_code = c.company_code),
       (SELECT COUNT(DISTINCT sm.senior_manager_code) FROM Senior_Manager sm WHERE sm.company_code = c.company_code),
       (SELECT COUNT(DISTINCT m.manager_code)         FROM Manager        m  WHERE m.company_code  = c.company_code),
       (SELECT COUNT(DISTINCT e.employee_code)        FROM Employee       e  WHERE e.company_code  = c.company_code)
FROM Company c
ORDER BY c.company_code;
```

- **Every table already has `company_code`**, so each level can be counted on its own; no need to walk the hierarchy.
- **Subquery per column** (correlated subquery): for each company row `c`, count the rows in that table where `company_code = c.company_code`.
- **`COUNT(DISTINCT ...)`** because "the tables may contain duplicate records": a duplicated `SM1` row must still count as 1.
- **`ORDER BY c.company_code`** sorts as text, so `C_1, C_10, C_2`, exactly what the note asks for.

**Common shortcut:** join `Company` to `Employee` and count distinct codes there. It works on HackerRank's data, but it misses any manager who has no employees yet, so the per-table version is safer.

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank, **choose MySQL** in the language menu; it opens on DB2)
