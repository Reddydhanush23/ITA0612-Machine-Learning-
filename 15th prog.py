from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
iris = load_iris()
X, y = iris.data, iris.target
model = GaussianNB()
model.fit(X, y)
print(model.predict([[6.0,3.0,4.8,1.8]]))
