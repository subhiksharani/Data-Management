SELECT COUNT(a1.App) AS countApp
FROM googleplaystore AS a1
WHERE a1.App NOT IN (SELECT a2.App 
FROM googleplaystore_user_reviews AS a2);