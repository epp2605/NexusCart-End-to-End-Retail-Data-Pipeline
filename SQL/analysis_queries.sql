-- Product Revenue
SELECT Product_ID,
SUM(Sale_Amount) AS Revenue
FROM Sales_Transactions
GROUP BY Product_ID
ORDER BY Revenue DESC;

-- Customer Revenue
SELECT Customer_ID,
SUM(Sale_Amount) AS Revenue
FROM Sales_Transactions
GROUP BY Customer_ID
ORDER BY Revenue DESC;

-- Top 10 Customers
SELECT Customer_ID,
SUM(Sale_Amount) AS Revenue
FROM Sales_Transactions
GROUP BY Customer_ID
ORDER BY Revenue DESC
LIMIT 10;