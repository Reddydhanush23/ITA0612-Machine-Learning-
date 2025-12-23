from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X,y)
models = {
    "DT": DecisionTreeClassifier(),
    "NB": GaussianNB(),
    "KNN": KNeighborsClassifier()
}
for name, model in models.items():
    model.fit(X_train, y_train)
    print(name, accuracy_score(y_test, model.predict(X_test)))
