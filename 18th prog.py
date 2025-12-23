from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron
X, y = load_iris(return_X_y=True)
model = Perceptron()
model.fit(X, y)
print(model.predict([[5.9,3.0,5.1,1.8]]))
