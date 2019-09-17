SELECT COUNT(DISTINCT(a1.App)) as countApp
FROM googleplaystore_user_reviews AS a1
WHERE a1.App IN
(SELECT a2.App
FROM googleplaystore_user_reviews AS a2
WHERE a2.Sentiment="Negative")
AND a1.App IN
(SELECT a3.App
FROM googleplaystore_user_reviews AS a3
WHERE a3.Sentiment="Positive");