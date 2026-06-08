import pandas as pd

df = pd.read_csv("Dataset/NexusCart_100_Rows_Dataset.csv")

rfm = df.groupby("Customer_ID").agg({
    "Transaction_ID":"count",
    "Sale_Amount":"sum"
})

rfm.columns = ["Frequency","Monetary"]

def segment(row):
    if row["Monetary"] >= 3000:
        return "VIP Customer"
    elif row["Monetary"] >= 2000:
        return "Regular"
    else:
        return "At-Risk"

rfm["Segment"] = rfm.apply(segment, axis=1)

print(rfm)
rfm.to_csv("Python/customer_segments.csv")