###################################################
# K Means Clustering - Basic Template
###################################################

# Import required Python packages

from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

# Import sample data

my_df = pd.read_csv("data/sample_data_clustering.csv")

# Plot the data

plt.scatter(my_df["var1"], my_df["var2"])
plt.xlabel("var1")
plt.ylabel("var2")
plt.show()

# Instantiate & fit the model

kmeans = KMeans(n_clusters = 3, random_state = 42)
kmeans.fit(my_df)

# Add the cluster labels to our df

my_df["cluster"] = kmeans.labels_
my_df["cluster"].value_counts()

# Plot our clusters and centroids

centroids = kmeans.cluster_centers_
print(centroids)

clusters = my_df.groupby("cluster")

for cluster, data in clusters:
    plt.scatter(data["var1"],data["var2"], marker = "o", label = cluster)
    plt.scatter(centroids[cluster,0], centroids[cluster, 1], marker = "X", color = "black", s = 300)
plt.legend()
plt.tight_layout()
plt.show()
    























