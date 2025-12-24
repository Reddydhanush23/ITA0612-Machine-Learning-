from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
X = [[1],[2],[3],[4]]
y = [1,4,9,16]
lin = LinearRegression()
lin.fit(X, y)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
lin2 = LinearRegression()
lin2.fit(X_poly, y)
print("Linear Prediction:", lin.predict([[5]]))
print("Polynomial Prediction:", lin2.predict(poly.transform([[5]])))
