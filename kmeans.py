from sklearn.cluster import KMeans
import numpy as np
from varta_bert import embeddings

embeddings_np = np.array([tensor.numpy() for tensor in embeddings])

kmeans = KMeans(n_clusters=5)

kmeans.fit(embeddings_np)
labels = kmeans.labels_


n_clusters = len(set(labels))

print("Number of clusters:", n_clusters)
print("Cluster labels:")
for i, label in enumerate(labels):
    print(f"Sample {i+1}: Cluster {label}")