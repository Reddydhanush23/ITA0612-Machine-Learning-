from sklearn.neural_network import MLPClassifier
X = [[0,0],[0,1],[1,0],[1,1]]
y = [0,1,1,0]
model = MLPClassifier(hidden_layer_sizes=(2,), max_iter=500)
model.fit(X, y)
print("Predictions:", model.predict(X))
