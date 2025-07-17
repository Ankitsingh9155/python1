
import pandas as pd 
from sklearn.linear_model import LinearRegression

#Sample Data
data = {
    'hours': [1, 2, 3, 4, 5],
    'marks': [20,334,55,67,77]
}
df=pd.DataFrame(data)

#Model

X=df[['hours']]
Y=df['marks']           #Target

model = LinearRegression()
model.fit(X,Y)

#predict
predicted=model.predict([[7]])
print(f"Predicted marks for 7 study hours: {predicted[0]}")
