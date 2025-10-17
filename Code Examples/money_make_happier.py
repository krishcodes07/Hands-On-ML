# page 49
# topic: model based machine learning
# Example 1-1. Training and running a linear model using Scikit-Learn

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the data
df = pd.read_csv('data/money_make_happier.csv')
# print(df)

# Prepare the data
X = df[['GDP_per_capita']] # features
y = df['Life_satisfaction'] # labels

# Visualize the data
plt.plot(X, y)
plt.xlabel("GDP Per Capita")
plt.ylabel("Life Satisfaction")
plt.grid(True)
# plt.show()

# Choose a linear model
model = LinearRegression()
model.fit(X, y)

# Print θ₀ and θ₁
print("θ0 (intercept) =", model.intercept_) # θ₀ = value of y when x=0, adjusted so the line goes through the center of the data.
print("θ1 (slope) =", model.coef_[0]) # θ₁ = how much y changes with x, on average.

# Test the model
test_x = model.predict([[65000]])[0]
print(f"Linear model: {test_x}")

# Test the accuracy
r2 = model.score(X, y) # R^2 score
print(f"Linear model accuracy: {r2*100}")


# By a instance based model
from sklearn.neighbors import KNeighborsRegressor

# Choose a instance based model
model = KNeighborsRegressor(n_neighbors=3)
model.fit(X, y)

# Test the model
test_x = model.predict([[65000]])[0]
print(f"Instance-based model: {test_x}")

# Test the accuracy
r2 = model.score(X, y)
print(f"Instance-based model accuracy: {r2*100}")