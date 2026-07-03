import pandas as pd

# Load dataset
df = pd.read_csv("D:/DataForge_EDA_Sprint_2026_2026CS004/01_data/raw/dataset_raw.csv")

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing categorical values
categorical_cols = df.select_dtypes(include="object").columns
for col in categorical_cols:
    df[col] = df[col].fillna("Unknown")

# Fill missing numeric values with median
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Convert date column if present
if "Order Date" in df.columns:
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Month"] = df["Order Date"].dt.month
    df["Year"] = df["Order Date"].dt.year

# Save cleaned dataset
pd.to_csv("D:/DataForge_EDA_Sprint_2026_2026CS004/01_data/processed/dataforge_cleaned.csv", index=False)

print("Dataset cleaned successfully!")