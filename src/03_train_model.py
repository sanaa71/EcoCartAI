import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# --------------------------------
# 1. Load dataset
# --------------------------------

df = pd.read_csv(
    "dataset/ecocart_products_with_eco_score.csv"
)

print("Dataset Shape:", df.shape)


# --------------------------------
# 2. Select input features
# --------------------------------

features = [
    "category",
    "material",
    "weight_g",
    "packaging",
    "recyclable",
    "reusable",
    "durability_years",
    "certification"
]

X = df[features]

# Target variable
y = df["eco_score"]


# --------------------------------
# 3. Identify feature types
# --------------------------------

categorical_features = [
    "category",
    "material",
    "packaging",
    "recyclable",
    "reusable",
    "certification"
]

numerical_features = [
    "weight_g",
    "durability_years"
]


# --------------------------------
# 4. Encode categorical features
# --------------------------------

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        ),
        (
            "numerical",
            "passthrough",
            numerical_features
        )
    ]
)


# --------------------------------
# 5. Create ML model
# --------------------------------

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)


# --------------------------------
# 6. Create pipeline
# --------------------------------

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)


# --------------------------------
# 7. Split dataset
# --------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))


# --------------------------------
# 8. Train model
# --------------------------------

pipeline.fit(X_train, y_train)

print("\nModel training completed!")


# --------------------------------
# 9. Make predictions
# --------------------------------

y_pred = pipeline.predict(X_test)


# --------------------------------
# 10. Evaluate model
# --------------------------------

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = mse ** 0.5

r2 = r2_score(y_test, y_pred)


print("\n--- MODEL PERFORMANCE ---")

print("MAE :", round(mae, 2))
print("RMSE:", round(rmse, 2))
print("R²  :", round(r2, 2))


# --------------------------------
# 11. Save trained model
# --------------------------------

joblib.dump(
    pipeline,
    "model/ecocart_model.pkl"
)

print("\nModel saved successfully!")
print("Location: model/ecocart_model.pkl")