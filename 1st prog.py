# FIND-S Algorithm
data = [
    ['Sunny','Warm','Yes'],
    ['Sunny','Cold','Yes'],
    ['Rainy','Warm','No']
]
hypothesis = None
for row in data:
    if row[-1] == 'Yes':
        if hypothesis is None:
            hypothesis = row[:-1]
        else:
            for i in range(len(hypothesis)):
                if hypothesis[i] != row[i]:
                    hypothesis[i] = '?'
print("Most Specific Hypothesis:", hypothesis)
