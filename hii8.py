import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    'Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Marks': [20, 30, 35, 45, 50, 60, 65, 70, 75, 85]
}
df = pd.DataFrame(data)

# Features and target
X = df[['Hours']]
y = df['Marks']

# Train the model
model = LinearRegression()
model.fit(X, y)

# Predictions
hours = [[5], [7.5], [10]]  # List of study hour values
predictions = model.predict(hours)

# Print results
for i, h in enumerate([5, 7.5, 10]):
    print(f"Predicted Marks for {h} hours of study: {predictions[i]:.2f}")
