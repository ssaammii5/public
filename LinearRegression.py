import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv('C:/Users/Sami/Downloads/data.csv')
x = np.array(data.Level).reshape((-1,1))
y = np.array(data.Salary)

model = LinearRegression().fit(x,y)

plt.scatter(x,y)
plt.show()

plt.scatter(x,y)
plt.plot(x,model.predict(x))
plt.show()

# y = mx+c
print(model.predict(x))
print(model.intercept_) #c
print(model.coef_) #m
print(model.predict(np.array([[10]]))) #future predict
