import pandas as pd

# Load dataset
df = pd.read_csv("dataset/ecocart_ecommerce_products_500.csv")

# Handle missing certification
df["certification"] = df["certification"].fillna("None")

print("Dataset Shape:", df.shape)

print("\n--- MATERIALS ---")
print(df["material"].value_counts())

print("\n--- PACKAGING ---")
print(df["packaging"].value_counts())

print("\n--- RECYCLABLE ---")
print(df["recyclable"].value_counts())

print("\n--- REUSABLE ---")
print(df["reusable"].value_counts())

print("\n--- CERTIFICATION ---")
print(df["certification"].value_counts())

print("\n--- DURABILITY ---")
print(df["durability_years"].describe())