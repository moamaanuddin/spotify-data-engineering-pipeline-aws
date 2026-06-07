SELECT
    label,
    COUNT(*) AS total_tracks,
    ROUND(AVG(CAST(track_popularity AS INTEGER)),2) AS avg_popularity
FROM datawarehouse
GROUP BY label
HAVING COUNT(*) >= 5
ORDER BY avg_popularity DESC;
