from sklearn.metrics import silhouette_score
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from kmeans import embeddings_np, labels
import numpy as np

silhouette_avg = silhouette_score(embeddings_np, labels)

print("Silhouette Score:", silhouette_avg)


for cluster_id in set(labels):
    cluster_points = embeddings_np[labels == cluster_id] 
   
    similarity_matrix = cosine_similarity(cluster_points)  
    distance_matrix = euclidean_distances(cluster_points)  
    
    average_similarity = np.mean(similarity_matrix)
    average_distance = np.mean(distance_matrix)
 
    print(f"Cluster {cluster_id}: Average Similarity: {average_similarity}")
    print(f"Cluster {cluster_id}: Average Distance: {average_distance}")