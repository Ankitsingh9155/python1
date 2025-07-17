import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Sample data
data = {
    'hours': [1, 2, 3, 4, 5],
    'marks': [20, 33, 55, 67, 77]
}
df = pd.DataFrame(data)

# Model
X = df[['hours']]
Y = df['marks']

model = LinearRegression()
model.fit(X, Y)

# Predict for 7 hours
predicted = model.predict([[7]])
print(f"Predicted marks for 7 study hours: {predicted[0]:.2f}")

# Create points for regression line
x_range = np.linspace(df['hours'].min(), 7, 100).reshape(-1, 1)
y_range = model.predict(x_range)

# Plot
plt.scatter(df['hours'], df['marks'], color='blue', label='Actual data')
plt.plot(x_range, y_range, color='red', label='Regression line')
plt.scatter(7, predicted, color='green', marker='o', s=100, label='Predicted point (7 hrs)')

plt.xlabel('Hours of Study')
plt.ylabel('Marks')
plt.title('Study Hours vs Marks with Prediction')
plt.legend()
plt.grid(True)
plt.show()
