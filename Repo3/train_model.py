import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load the data
data = pd.read_csv('data.csv')

# Features and target
X = data[['Hours']]
y = data['Score']

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the model to a file
joblib.dump(model, 'model.pkl')

print("✅ Model trained and saved as model.pkl")
