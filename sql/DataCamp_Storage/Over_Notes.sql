 -- window functions
    -- are processed after every part of the query except
    -- the final ORDER BY
    -- uses information in the result seet to calculate information
    -- as opposed to using the database directly
    -- window functions are not available in SQLite


 -- OVER window function:
 -- instead of writing a subquery
 -- pass the aggregate value over the existing results set
 -- results are identical
 -- simpler syntax
 -- faster processing time

SELECT
    date,
    (home_goal + away_goal) AS goals,
    (SELECT AVG(home_goal + away_goal)
        FROM match
        WHERE season = '2011/2012') AS overall_avg
 FROM match
 WHERE season = '2011/2012';


 -- same using OVER()
 SELECT
    date,
    (home_goal + away_goal) AS goals,
    AVG(home_goal + away_goal) OVER() AS overall_avg
 FROM match
 WHERE season = '2011/2012';



 --  RANK window function:
 -- creates a column numbering your dataset highest to lowest
 -- based on a column you specify

 -- what is the rank of matches based on the number of goals scored
SELECT
    date,
    (home_goal + away_goal) AS goals,
    RANK() OVER(ORDER BY home_goal + away_goal) AS goals_rank
FROM match
WHERE season = '2011/2012'
-- result:
-- date | goals | goals_rank
-- 04-28 | 0 | 1


