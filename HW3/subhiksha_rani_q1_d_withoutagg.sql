SELECT a1.App as appName
FROM googleplaystore_user_reviews AS a1
WHERE NOT EXISTS(SELECT a2.App
FROM googleplaystore_user_reviews AS a2
WHERE a1.App = a2.App AND a1.Review != a2.Review);