from sklearn.cluster import DBSCAN
from varta_bert import embeddings
import numpy as np


embeddings_np = np.array([tensor.numpy() for tensor in embeddings])

dbscan = DBSCAN(eps=50, min_samples=3)
dbscan.fit(embeddings_np)

labels = dbscan.labels_
print(labels)

n_clusters = len(set(labels)) - (1 if -1 in labels else 0)

print("Number of clusters:", n_clusters)

print("Cluster labels:")
for i, label in enumerate(labels):
    print(f"Sample {i+1}: Cluster {label}")

