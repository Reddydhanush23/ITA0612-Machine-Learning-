from sklearn.linear_model import LinearRegression
X = [[1],[2],[3],[4],[5]]
y = [100,150,200,250,300]
model = LinearRegression()
model.fit(X,y)
print(model.predict([[6]]))
