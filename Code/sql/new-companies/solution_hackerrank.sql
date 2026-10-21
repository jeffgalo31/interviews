-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Explained version: solution.sql
SELECT c.company_code, c.founder,
       (SELECT COUNT(DISTINCT lm.lead_manager_code) FROM Lead_Manager lm WHERE lm.company_code = c.company_code),
       (SELECT COUNT(DISTINCT sm.senior_manager_code) FROM Senior_Manager sm WHERE sm.company_code = c.company_code),
       (SELECT COUNT(DISTINCT m.manager_code) FROM Manager m WHERE m.company_code = c.company_code),
       (SELECT COUNT(DISTINCT e.employee_code) FROM Employee e WHERE e.company_code = c.company_code)
FROM Company c
ORDER BY c.company_code;
