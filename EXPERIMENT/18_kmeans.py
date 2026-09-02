from sklearn.cluster import KMeans

X = [
    [1, 2],
    [1, 3],
    [2, 2],
    [8, 8],
    [9, 8],
    [8, 9]
]

model = KMeans(
    n_clusters=2,
    random_state=1,
    n_init=10
)

model.fit(X)

print("Cluster Labels:")
print(model.labels_)

print("Cluster Centers:")
print(model.cluster_centers_)
