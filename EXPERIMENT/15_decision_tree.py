from sklearn.tree import DecisionTreeClassifier

X = [
    [1],
    [2],
    [3],
    [4],
    [5],
    [6]
]

y = [
    "Fail",
    "Fail",
    "Pass",
    "Pass",
    "Pass",
    "Pass"
]

model = DecisionTreeClassifier()

model.fit(X, y)

marks = [[4]]

prediction = model.predict(marks)

print("Predicted Result:", prediction[0])
