import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset/NexusCart_100_Rows_Dataset.csv")

# Product Revenue
product_sales = df.groupby("Product_ID")["Sale_Amount"].sum()

plt.figure(figsize=(8,5))
product_sales.plot(kind="bar")
plt.title("Revenue by Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("product_revenue_chart.png")
plt.show()

# Top Customers
customer_sales = df.groupby("Customer_ID")["Sale_Amount"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(8,5))
customer_sales.plot(kind="bar")
plt.title("Top 10 Customers")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("top_customers_chart.png")
plt.show()