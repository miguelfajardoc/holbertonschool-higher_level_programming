-- top top city
SELECT (city), AVG(value) AS avg_temp FROM temperatures where month >= 7 AND month <= 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
