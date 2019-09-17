SELECT Category AS category, AVG(Price) AS avgPrice
FROM googleplaystore
GROUP BY Category
ORDER BY AVG(Price) DESC
LIMIT 10;