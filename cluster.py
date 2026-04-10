import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, adjusted_rand_score

# -------------------------------
# LOAD DATA
# -------------------------------
digits = load_digits()
X = digits.data
y = digits.target

# -------------------------------
# K-MEANS (k = 10)
# -------------------------------
kmeans = KMeans(n_clusters=10, random_state=42)
clusters = kmeans.fit_predict(X)

centroids = kmeans.cluster_centers_

# -------------------------------
# SHOW CLUSTER CENTROIDS
# -------------------------------
plt.figure(figsize=(10,5))
for i in range(10):
    plt.subplot(2,5,i+1)
    plt.imshow(centroids[i].reshape(8,8), cmap='gray')
    plt.title(f"Cluster {i}")
    plt.axis('off')
plt.show()

# -------------------------------
# ELBOW METHOD
# -------------------------------
inertia = []
K = range(1,15)

for k in K:
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X)
    inertia.append(km.inertia_)

plt.figure()
plt.plot(K, inertia, marker='o')
plt.xlabel("Number of clusters")
plt.ylabel("Inertia (SSE)")
plt.title("Elbow Method")
plt.show()

# -------------------------------
# SILHOUETTE SCORE
# -------------------------------
print("\nSilhouette Scores:")
for k in range(2,15):
    km = KMeans(n_clusters=k, random_state=42)
    labels = km.fit_predict(X)
    score = silhouette_score(X, labels)
    print(f"k={k} -> {score:.4f}")

# -------------------------------
# ADJUSTED RAND INDEX
# -------------------------------
ari = adjusted_rand_score(y, clusters)
print("\nAdjusted Rand Index:", ari)
