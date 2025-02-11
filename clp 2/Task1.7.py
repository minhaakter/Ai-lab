import pandas as pd

n = int(input("Enter number of products: "))
data = {"Product": [], "Price": [], "Quantity": []}

for _ in range(n):
    product = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity sold: "))
    data["Product"].append(product)
    data["Price"].append(price)
    data["Quantity"].append(quantity)

df = pd.DataFrame(data)
df["Revenue"] = df["Price"] * df["Quantity"]
total_revenue = df.groupby("Product")["Revenue"].sum()

print("Total Revenue per Product:\n", total_revenue)