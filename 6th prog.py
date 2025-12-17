from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
X = [[1],[2],[3],[4]]
y = [0,0,1,1]
model = GaussianNB()
model.fit(X, y)
pred = model.predict(X)
print("Confusion Matrix:\n", confusion_matrix(y, pred))
print("Accuracy:", accuracy_score(y, pred))


