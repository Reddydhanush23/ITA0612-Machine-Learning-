from sklearn.tree import DecisionTreeClassifier
X = [[2,32,3000],[4,64,5000],[6,128,8000]]
y = [0,1,2]
model = DecisionTreeClassifier()
model.fit(X,y)
print(model.predict([[4,64,6000]]))
