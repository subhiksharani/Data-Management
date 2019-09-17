SELECT App as appName
FROM googleplaystore_user_reviews
GROUP BY App
HAVING COUNT(Review) = 1;