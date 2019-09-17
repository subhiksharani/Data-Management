SELECT COUNT(*) AS countApp
FROM (SELECT COUNT(DISTINCT(a2.App))
FROM googleplaystore AS a1, googleplaystore_user_reviews AS a2
WHERE a1.App = a2.App AND a1.Type = "Free" AND a2.Sentiment="Positive"
GROUP BY a1.App
HAVING COUNT(a2.Sentiment="Positive")>=10) AS appCount;
