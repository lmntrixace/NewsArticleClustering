import numpy as np

import matplotlib.pyplot as plt
from varta_bert import embeddings

embeddings_np = np.array([tensor.numpy() for tensor in embeddings])

print(embeddings_np)


distances = np.linalg.norm(embeddings_np[:, np.newaxis] - embeddings_np, axis=2)


plt.figure(figsize=(8, 6))
plt.imshow(distances, cmap='viridis', interpolation='nearest')
plt.colorbar(label='Distance')
plt.title('Pairwise Distance between Embeddings')
plt.xlabel('Embedding Index')
plt.ylabel('Embedding Index')
plt.show()