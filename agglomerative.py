from sklearn.cluster import AgglomerativeClustering
from varta_bert import embeddings
import numpy as np


embeddings_np = np.array([tensor.numpy() for tensor in embeddings])


agglomerative = AgglomerativeClustering(n_clusters=5, metric='euclidean', linkage='ward')
agglomerative.fit(embeddings_np)

labels = agglomerative.labels_
print(labels)

n_clusters = len(set(labels))

print("Number of clusters:", n_clusters)
print("Cluster labels:")
for i, label in enumerate(labels):
    print(f"Sample {i+1}: Cluster {label}")