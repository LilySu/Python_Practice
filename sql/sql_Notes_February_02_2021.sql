within group -- is an ordered set aggregate
-- runs an aggregate and runs it within the same function
-- allows something to be grouped and aggregated at the same time

SELECT *,
    percentile_disc(gs) within group (order by "averageRating")
FROM dataframe df, generate_series(0.01, 1, 0.01) gs
GROUP BY 1,2,3;
-- this query computes items into buckets and sometimes cannot handle the load

-- Use an anti-join to filter the match table for matches where players did not score more than 700 runs.
SELECT columns
FROM match
WHERE match_id NOT IN
(SELECT column
FROM table
WHERE thing > number)

-- Get price across all wines
SELECT style, price,
    ROUND(AVG(price) OVER(), 2) AS avg_price
FROM wine
ORDER BY style

-- all the due dates can be shifted by 90 days
SELECT reference,
       due_date + interval '90 days' AS new_date
FROM invoices
ORDER BY new_date, reference;

-- Complete the query to determine which employees are also managers.
SELECT last_name
FROM employees
WHERE
  (employee_id IN (SELECT manager_id FROM employees))
ORDER BY last_name;



WITH subquery AS (
  SELECT * FROM match WHERE win_margin > 20
)

SELECT 	match_id,
	win_margin
FROM subquery
WHERE match_winner = 1
ORDER BY match_id
LIMIT 10;