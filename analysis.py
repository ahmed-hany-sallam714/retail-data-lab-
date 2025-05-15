import pandas as pd
import numpy as np

# 📥 Load datasets
sales = pd.read_csv("sales_train.csv")
items = pd.read_csv("items.csv")
shops = pd.read_csv("shops.csv")
item_categories = pd.read_csv("item_categories.csv")
data = pd.read_csv("Online_Retail.csv", encoding="ISO-8859-1")

# 📌 Filtering function: return groups where avg price > 500
def filter_func(dataframe):
    return dataframe["item_price"].mean() > 500

# Apply filter on item_id groups (more meaningful than item_price)
filtered_sales = sales.groupby("item_id").filter(filter_func)
print("Filtered sales where average item price > 500:")
print(filtered_sales)

# 🧮 Aggregating mean of item_price
print("Average item price:")
print(sales.aggregate({"item_price": np.mean}))

# 🏬 Group by shop_id and print each group
for shop_id, group in sales.groupby("shop_id"):
    print(f"Shop ID: {shop_id}")
    print(group)

# 📊 Statistics on item_id
print("Statistics for item_id:")
print("Standard deviation:", sales["item_id"].std())
print("Count:", sales["item_id"].count())
print("Mean:", sales["item_id"].mean())
print("Median:", sales["item_id"].median())
print("Min:", sales["item_id"].min())
print("Max:", sales["item_id"].max())
print("Variance:", sales["item_id"].var())
# ⚠️ Avoid using prod() due to potential overflow
# print("Product:", sales["item_id"].prod())
print("Sum:", sales["item_id"].sum())

# 📈 Descriptive statistics
print("Sales description:")
print(sales.describe())

# 📦 Average price per item
print("Average price per item:")
print(sales.groupby("item_id")["item_price"].mean())

# ✅ Count number of sold items (positive quantity)
number = (sales["item_cnt_day"] > 0).sum()
print(f"Number of sold items: {number}")

# 🔍 Check for null values
print("Null values in sales:")
print(pd.isnull(sales).sum())

# 🔗 Merge sales with item details using item_id
print("Merged sales with items on item_id:")
print(sales.merge(items, how="outer", on="item_id"))

# 👁️ Show first rows of each DataFrame
print("First 5 rows of sales:")
print(sales.head())
print("*" * 20)
print("First 5 rows of items:")
print(items.head())
print("*" * 20)
print("First 5 rows of shops:")
print(shops.head())
print("*" * 20)
print("First 5 rows of item_categories:")
print(item_categories.head())
print("*" * 20)

# 🔄 Examples of merging/joining DataFrames
a = pd.DataFrame({"item": ["a", "b", "c"], "id": [5, 2, 4]})
b = pd.DataFrame({"item": ["f", "8", "c"], "id": [1, 2, 3]})

# Merge on both item and id
print("Outer merge on item and id:")
print(pd.merge(a, b, how="outer", on=["item", "id"]))

# Concatenation (append is deprecated)
print("Concatenated a and b:")
print(pd.concat([a, b]))

# Set index for join operations
a = a.set_index("id")
b = b.set_index("id")

# Join with suffixes
print("Joined DataFrames with suffixes:")
print(a.join(b, how="outer", lsuffix="_left", rsuffix="_right"))

# Reset index if you want to merge on 'id' again
a = a.reset_index()
b = b.reset_index()

# Valid merge examples
print("Inner merge on id:")
print(pd.merge(a, b, how="inner", on="id"))

print("Outer merge on id:")
print(pd.merge(a, b, how="outer", on="id"))

print("Left merge with suffixes:")
print(pd.merge(a, b, how="left", on="id", suffixes=("_left", "_right")))

# 🔥 Note: the following merge would fail if 'ho' doesn't exist
# print(pd.merge(a, b, how="outer", left_on="item", right_on="ho"))  # ⚠️ Invalid

# Concatenate and reset index
print("Concatenated with keys, reset index:")
print(pd.concat([a, b], keys=["x", "y"]).reset_index())

print("Concatenated with keys:")
print(pd.concat([a, b], keys=["x", "y"]))

print("Concatenated with ignore_index:")
print(pd.concat([a, b], ignore_index=True))
