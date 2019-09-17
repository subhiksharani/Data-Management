SELECT App AS appName, Reviews AS reviewNum
FROM googleplaystore
WHERE Reviews >= 100
ORDER BY Reviews DESC
LIMIT 10;