import pandas as pd
import joblib

# Load trained model
model = joblib.load("model/ecocart_model.pkl")

print("================================")
print("          ECO-CART AI")
print("================================")

# Take product details from user
category = input("Enter category: ")
material = input("Enter material: ")
weight = float(input("Enter weight in grams: "))
packaging = input("Enter packaging: ")
recyclable = input("Is it recyclable? (Yes/No): ")
reusable = input("Is it reusable? (Yes/No): ")
durability = float(input("Enter durability in years: "))
certification = input("Enter certification (or None): ")

# Create product dataframe
new_product = pd.DataFrame({
    "category": [category],
    "material": [material],
    "weight_g": [weight],
    "packaging": [packaging],
    "recyclable": [recyclable],
    "reusable": [reusable],
    "durability_years": [durability],
    "certification": [certification]
})

# Predict Eco Score
prediction = model.predict(new_product)

eco_score = prediction[0]

# Keep score between 0 and 100
eco_score = max(0, min(100, eco_score))

# Determine eco-friendly level
if eco_score >= 80:
    level = "Highly Eco-Friendly 🌱"
elif eco_score >= 60:
    level = "Moderately Eco-Friendly ♻️"
elif eco_score >= 40:
    level = "Less Eco-Friendly ⚠️"
else:
    level = "Not Eco-Friendly ❌"

print("\n================================")
print("          RESULT")
print("================================")
print(f"Predicted Eco Score: {eco_score:.2f}/100")
print(f"Eco Level: {level}")
print("================================")