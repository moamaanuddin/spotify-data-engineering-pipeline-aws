SELECT
    track_name,
    name AS artist_name,
    track_popularity
FROM datawarehouse
ORDER BY track_popularity DESC
LIMIT 10;
