SELECT COUNT(a1.App) AS countApp
FROM googleplaystore AS a1 LEFT OUTER JOIN googleplaystore_user_reviews AS a2
ON a1.App = a2.App
WHERE a2.App IS NULL;