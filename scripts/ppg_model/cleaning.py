import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load dataset
file_path = r"C:\Users\Shashank Mahato\Desktop\HaemScan\ppg_model\cleaned_anemia_dataset.csv"
df = pd.read_csv(file_path)

# Trim whitespace from column names
df.columns = df.columns.str.strip()

# Assuming 'HGB' is the column containing hemoglobin levels
hemoglobin_column = "HGB"  # Ensure the correct column name

# Convert HGB column to numeric, forcing errors to NaN
df[hemoglobin_column] = pd.to_numeric(df[hemoglobin_column], errors='coerce')

# Drop rows where HGB is NaN after conversion
df.dropna(subset=[hemoglobin_column], inplace=True)

# Create Anemia classification column (threshold: 10.5 g/dL)
df['Anemia'] = (df[hemoglobin_column] < 10.5).astype(int)  # 1 = Anemic, 0 = Non-Anemic

# Drop remaining rows with missing values
df.dropna(inplace=True)

# Encode categorical columns (if any)
categorical_columns = df.select_dtypes(include=['object']).columns
label_encoders = {}

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Normalize numerical features
numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
numerical_columns = [col for col in numerical_columns if col != "Anemia"]  # Exclude target column
scaler = StandardScaler()
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

# Define input features (X) and target (y)
X = df.drop(columns=['Anemia'])
y = df['Anemia']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Save processed datasets
X_train.to_csv("X_train.csv", index=False)
X_test.to_csv("X_test.csv", index=False)
y_train.to_csv("y_train.csv", index=False)
y_test.to_csv("y_test.csv", index=False)

print("Preprocessing Complete")
print(f"Train shape: {X_train.shape}, Test shape: {X_test.shape}")
print(f"Anemia class distribution: \n{df['Anemia'].value_counts()}")
