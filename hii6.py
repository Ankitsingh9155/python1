import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Create Dataset
data = {
    'Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Marks': [20, 30, 35, 45, 50, 60, 65, 70, 75, 85]
}
df = pd.DataFrame(data)

# Step 2: Scatter Plot using Matplotlib
plt.figure(figsize=(6, 4))
plt.scatter(df['Hours'], df['Marks'], color='blue')
plt.title('Study Hours vs Marks (Matplotlib)')
plt.xlabel('Hours Studied')
plt.ylabel('Marks Obtained')
plt.grid(True)
plt.show()

# Step 3: Scatter Plot using Seaborn
plt.figure(figsize=(6, 4))
sns.scatterplot(x='Hours', y='Marks', data=df, color='green')
plt.title('Study Hours vs Marks (Seaborn)')
plt.xlabel('Hours Studied')
plt.ylabel('Marks Obtained')
plt.grid(True)
plt.show()

# Step 4 (Bonus): Regression Line using sns.regplot
plt.figure(figsize=(6, 4))
sns.regplot(x='Hours', y='Marks', data=df, color='red')
plt.title('Study Hours vs Marks with Regression Line')
plt.xlabel('Hours Studied')
plt.ylabel('Marks Obtained')
plt.grid(True)
plt.show()
