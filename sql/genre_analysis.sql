SELECT
    genre,
    COUNT(*) AS total_tracks,
    ROUND(AVG(CAST(track_popularity AS INTEGER)),2) AS avg_popularity
FROM datawarehouse
WHERE genre IS NOT NULL
GROUP BY genre
HAVING COUNT(*) >= 10
ORDER BY avg_popularity DESC;
