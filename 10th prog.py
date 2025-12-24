from sklearn.mixture import GaussianMixture
X = [[1],[2],[8],[9]]
model = GaussianMixture(n_components=2)
model.fit(X)
print("Cluster Labels:", model.predict(X))

