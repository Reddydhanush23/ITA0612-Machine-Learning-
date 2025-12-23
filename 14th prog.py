from sklearn.linear_model import LinearRegression
X = [[800],[1000],[1200],[1500]]
y = [40,50,65,80]
model = LinearRegression()
model.fit(X, y)
print(model.predict([[1100]]))
