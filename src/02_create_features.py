import pandas as pd

# Load dataset
df = pd.read_csv("dataset/ecocart_ecommerce_products_500.csv")

# Replace missing certifications with None
df["certification"] = df["certification"].fillna("None")


# -----------------------------
# 1. MATERIAL SCORE
# -----------------------------

material_scores = {
    "Bamboo": 95,
    "Hemp": 95,
    "Jute": 90,
    "Organic Cotton": 90,
    "Recycled Cotton": 90,
    "Bamboo + Cotton":85,
    "Reclaimed Wood": 90,
    "Bamboo Fiber": 90,
    "Plant Fiber": 90,
    "Plant-based": 90,
    "Rattan": 85,
    "Linen": 85,
    "Wool": 80,
    "Wood": 80,
    "Glass": 80,
    "Stainless Steel": 80,
    "Cast Iron": 80,
    "Ceramic": 75,
    "Paper": 75,
    "Cotton": 70,
    "Denim": 65,
    "Canvas": 70,
    "Recycled Polyester": 70,
    "Recycled Plastic": 60,
    "Aluminum": 65,
    "Steel": 65,
    "Metal": 60,
    "Silicone": 55,
    "Viscose": 55,
    "Nylon": 40,
    "Polyester": 40,
    "Leather": 45,
    "Plastic": 30,
    "PVC + Copper": 25,
    "Plastic + Electronics": 25,
    "Aluminum + Electronics": 40,
    "Aluminum + Lithium Battery": 35,
    "Medical Silicone": 50,
    "MDF": 50,
    "Fruit": 85,
    "Coffee Beans": 75,
    "Tea Leaves": 80,
    "Honey": 80,
    "Wheat": 85,
    "Cocoa": 75,
    "Oats": 85,
    "Rice": 80,
    "Nuts": 80
}

df["material_score"] = df["material"].map(material_scores)


# -----------------------------
# 2. PACKAGING SCORE
# -----------------------------

packaging_scores = {
    "Compostable": 100,
    "Minimal Packaging": 95,
    "Recycled Cardboard": 90,
    "Paper": 85,
    "Cardboard": 75,
    "Glass": 70,
    "Plastic": 30
}

df["packaging_score"] = df["packaging"].map(packaging_scores)


# -----------------------------
# 3. RECYCLABILITY SCORE
# -----------------------------

df["recyclability_score"] = df["recyclable"].map({
    "Yes": 100,
    "No": 30
})


# -----------------------------
# 4. REUSABILITY SCORE
# -----------------------------

df["reusability_score"] = df["reusable"].map({
    "Yes": 100,
    "No": 30
})


# -----------------------------
# 5. DURABILITY SCORE
# -----------------------------

# Convert durability from 0.5–15 years
# into a 0–100 score

df["durability_score"] = (
    df["durability_years"] / 15
) * 100

df["durability_score"] = df["durability_score"].clip(0, 100)


# -----------------------------
# 6. CERTIFICATION SCORE
# -----------------------------

certification_scores = {
    "FSC": 95,
    "GOTS": 95,
    "USDA Organic": 95,
    "Fair Trade": 90,
    "OEKO-TEX": 85,
    "B Corp": 85,
    "Energy Star": 90,
    "None": 40
}

df["certification_score"] = df["certification"].map(
    certification_scores
)


# -----------------------------
# 7. FINAL ECO SCORE
# -----------------------------

df["eco_score"] = (
    0.30 * df["material_score"]
    + 0.20 * df["recyclability_score"]
    + 0.15 * df["packaging_score"]
    + 0.15 * df["reusability_score"]
    + 0.10 * df["durability_score"]
    + 0.10 * df["certification_score"]
)


# Round Eco Score
df["eco_score"] = df["eco_score"].round(2)


# -----------------------------
# 8. DISPLAY RESULTS
# -----------------------------

print("\nFirst 10 Products with Eco Score:")
print(
    df[
        [
            "product_name",
            "material",
            "packaging",
            "recyclable",
            "reusable",
            "durability_years",
            "certification",
            "eco_score"
        ]
    ].head(10)
)

print("\nEco Score Statistics:")
print(df["eco_score"].describe())


# -----------------------------
# 9. SAVE FEATURE DATASET
# -----------------------------

df.to_csv(
    "dataset/ecocart_products_with_eco_score.csv",
    index=False
)

print("\nNew dataset saved successfully!")