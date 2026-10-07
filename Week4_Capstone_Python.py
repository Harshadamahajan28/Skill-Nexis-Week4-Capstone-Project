import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("cleaned_week4_dataset.csv")
data["order_date"] = pd.to_datetime(data["order_date"])
data["year"] = data["order_date"].dt.year

print("Total Sales:", data["total_price"].sum())
print("Unique Orders:", data["order_id"].nunique())
print("Average Order Value:", data["total_price"].sum()/data["order_id"].nunique())

print("\nSales by Category")
print(data.groupby("category")["total_price"].sum().sort_values(ascending=False))

print("\nTop 10 Customers")
print(data.groupby("customer_name")["total_price"].sum().sort_values(ascending=False).head(10))

data.groupby("category")["total_price"].sum().plot(kind="bar", title="Sales by Category")
plt.tight_layout(); plt.show()

data.groupby("year")["total_price"].sum().plot(kind="line", marker="o", title="Yearly Sales Trend")
plt.tight_layout(); plt.show()
