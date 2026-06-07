SELECT
    name AS artist_name,
    MAX(CAST(followers AS BIGINT)) AS followers
FROM datawarehouse
GROUP BY name
ORDER BY followers DESC
LIMIT 10;
