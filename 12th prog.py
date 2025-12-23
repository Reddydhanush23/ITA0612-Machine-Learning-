from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
iris = load_iris()
X, y = iris.data, iris.target
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)
print(model.predict([[5.1,3.5,1.4,0.2]]))
