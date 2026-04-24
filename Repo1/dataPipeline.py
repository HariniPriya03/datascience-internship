import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import os
# EXTRACT
def extract_data(file_path):
    print("📥 Extracting data from:", file_path)
    df = pd.read_csv(file_path)
    print("✅ Data extracted. Shape:", df.shape)
    return df

# TRANSFORM
def transform_data(df, target_column):
    print("🔄 Starting data transformation...")

    X = df.drop(columns=[target_column])
    y = df[target_column]

    num_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
    cat_cols = X.select_dtypes(include=['object']).columns.tolist()

    num_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy='mean')),
        ("scaler", StandardScaler())
    ])

    cat_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy='most_frequent')),
        ("encoder", OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer(transformers=[
        ("num", num_pipeline, num_cols),
        ("cat", cat_pipeline, cat_cols)
    ])

    X_transformed = preprocessor.fit_transform(X)

    print("✅ Transformation complete. Transformed shape:", X_transformed.shape)
    return X_transformed, y, preprocessor

# LOAD
def load_data(X_transformed, y, output_file):
    print("💾 Saving transformed data to:", output_file)
    if hasattr(X_transformed, "toarray"):
        X_transformed = X_transformed.toarray()

    df_transformed = pd.DataFrame(X_transformed)
    df_transformed['marks'] = y.reset_index(drop=True)
    df_transformed.to_csv(output_file, index=False)
    print("✅ Data saved successfully.")

# MAIN PIPELINE EXECUTION
def run_pipeline(input_file, output_file, target_column):
    if not os.path.exists(input_file):
        print(f"❌ ERROR: Input file '{input_file}' not found.")
        return

    df = extract_data(input_file)
    X_transformed, y, _ = transform_data(df, target_column)
    load_data(X_transformed, y, output_file)

#EXAMPLE
if __name__ == "__main__":
    input_csv = "data.csv"              
    output_csv = "processed_data.csv"    
    target_col = "marks"               

    run_pipeline(input_csv, output_csv, target_col)
