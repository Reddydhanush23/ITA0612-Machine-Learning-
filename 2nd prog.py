# Candidate Elimination (Simple)
import pandas as pd
data = [
 ['Sunny','Warm','Yes'],
 ['Sunny','Cold','Yes'],
 ['Rainy','Warm','No']
]
S = None
G = ['?','?']
for row in data:
    if row[-1] == 'Yes':
        if S is None:
            S = row[:-1]
        else:
            for i in range(len(S)):
                if S[i] != row[i]:
                    S[i] = '?'
    else:
        for i in range(len(G)):
            if row[i] != S[i]:
                G[i] = S[i]
print("Specific Hypothesis:", S)
print("General Hypothesis:", G)
