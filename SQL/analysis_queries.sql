SELECT
Product_ID,
SUM(Sale_Amount) AS Total_Revenue
FROM Sales_Transactions
GROUP BY Product_ID
ORDER BY Total_Revenue DESC;

SELECT
c.Region,
SUM(s.Sale_Amount) AS Revenue
FROM Customers c
JOIN Sales_Transactions s
ON c.Customer_ID = s.Customer_ID
GROUP BY c.Region
ORDER BY Revenue DESC;