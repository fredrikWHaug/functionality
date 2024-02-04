import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('student_performance.csv')
df = df.sample(50)

X = df['Hours Studied']
y = df['Performance Index']
X = X.values.reshape(-1, 1)
y = y.values

model = LinearRegression()
model.fit(X, y)
y_prediction = model.predict(X)
plt.plot(X, y_prediction)
plt.show()