from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
X = [['Sunny','Hot'],['Rainy','Cold'],['Sunny','Cold']]
y = ['Yes','No','Yes']
le = LabelEncoder()
X_enc = [[le.fit_transform([i])[0] for i in row] for row in X]
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X_enc, y)
test = [[le.fit_transform(['Sunny'])[0], le.fit_transform(['Hot'])[0]]]
print("Prediction:", model.predict(test))
