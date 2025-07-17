import pandas as pd
from sklearn.linear_model import LinearRegression

# Step 1: Load the dataset
data = {
    'Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Marks': [20, 30, 35, 45, 50, 60, 65, 70, 75, 85]
}
df = pd.DataFrame(data)

# Step 2: Split into X (independent) and y (dependent)
X = df[['Hours']]  # 2D array (features)
y = df['Marks']    # 1D array (target)

# Step 3: Train the Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Step 4: Display the slope and intercept
print(f"Slope (Coefficient): {model.coef_[0]}")
print(f"Intercept: {model.intercept_}")
