from sklearn.naive_bayes import GaussianNB
X = [[25000,1],[50000,0],[30000,1],[80000,0]]
y = [0,1,0,1]
model = GaussianNB()
model.fit(X,y)
print(model.predict([[45000,0]]))
