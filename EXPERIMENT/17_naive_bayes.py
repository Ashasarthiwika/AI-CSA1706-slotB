from sklearn.naive_bayes import GaussianNB

X = [
    [1, 20],
    [2, 21],
    [3, 22],
    [8, 30],
    [9, 31],
    [10, 32]
]

y = [
    "Low",
    "Low",
    "Low",
    "High",
    "High",
    "High"
]

model = GaussianNB()

model.fit(X, y)

prediction = model.predict([[7, 29]])

print("Predicted Class:", prediction[0])
