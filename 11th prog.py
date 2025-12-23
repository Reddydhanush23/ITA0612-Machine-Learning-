from sklearn.tree import DecisionTreeClassifier
X = [[25,30000],[40,60000],[30,40000],[50,80000]]
y = [0,1,0,1]
model = DecisionTreeClassifier()
model.fit(X, y)
print(model.predict([[35,50000]]))
