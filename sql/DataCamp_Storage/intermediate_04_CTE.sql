-- Set up your CTE
WITH match_list AS (
    SELECT
  		country_id,
  		id
    FROM match
    WHERE (home_goal + away_goal) >= 10)
-- Select league and count of matches from the CTE
SELECT
    l.name AS league,
    COUNT(match_list.id) AS matches
FROM league AS l
-- Join the CTE to the league table
LEFT JOIN match_list ON match_list.country_id
GROUP BY l.name;