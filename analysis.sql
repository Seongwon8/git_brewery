SELECT state, COUNT(*) AS brewery_count
FROM breweries
GROUP BY state
ORDER BY brewery_count DESC;
