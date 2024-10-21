import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.metrics import silhouette_score

# Membaca data frame dari file CSV
df = pd.read_csv('./data/total_attacks_per_hour.csv')

# Memastikan data terbaca dengan benar
# print(df)

# Memilih kolom 'Total Attacks' sebagai fitur untuk clustering
X = df[['Total Attacks']]

# Menghitung Euclidean distances menggunakan linkage
linked = linkage(X, method='single')

# Menampilkan hasil perhitungan Euclidean distance
# print("Euclidean distance:\n", linked)

# Mencoba jumlah cluster dari 2 sampai 7
range_n_clusters = list(range(2, 8))
silhouette_avg_scores = []

for n_clusters in range_n_clusters:
    # Menggunakan Agglomerative Hierarchical Clustering (AHC) dengan single linkage
    model = AgglomerativeClustering(n_clusters=n_clusters, metric='euclidean', linkage='single')
    cluster_labels = model.fit_predict(X)

    # Menambahkan atribut Cluster ke DataFrame untuk menderetkan jumlah cluster
    # df['Cluster'] = cluster_labels
    # print(f"\n\nAnggota cluster-{n_clusters}")
    # # Cetak anggota dari setiap cluster
    # for cluster_num in range(n_clusters):
    #     cluster_members = df[df['Cluster'] == cluster_num]
    #     print(cluster_members)
    
    # Menghitung Silhouette Coefficient
    silhouette_avg = silhouette_score(X, cluster_labels)
    silhouette_avg_scores.append(silhouette_avg)
    print(f"Pada percobaan {n_clusters} cluster, rata-rata silhouette score : {silhouette_avg}")

# Menampilkan Silhouette Coefficient untuk setiap jumlah cluster
plt.figure(figsize=(10, 7))
plt.plot(range_n_clusters, silhouette_avg_scores, marker='o')
plt.title("Silhouette Coefficient untuk jumlah Cluster yang berbeda")
plt.xlabel("Nomor Cluster")
plt.ylabel("Silhouette Coefficient")
plt.show()

# Menemukan jumlah cluster terbaik
best_n_clusters = range_n_clusters[silhouette_avg_scores.index(max(silhouette_avg_scores))]
print(f"\n\nCluster terbaik terdapat pada percobaan {best_n_clusters} cluster")

# Menggunakan Agglomerative Hierarchical Clustering (AHC) dengan jumlah cluster terbaik
model = AgglomerativeClustering(n_clusters=best_n_clusters, metric='euclidean', linkage='single')
df['Cluster'] = model.fit_predict(X)

# Menghitung dan menampilkan Silhouette Coefficient untuk jumlah cluster terbaik
silhouette_avg = silhouette_score(X, df['Cluster'])
print(f"Dengan silhouette score : {silhouette_avg}")
print(f"\n\nBerikut anggota dari percobaan {best_n_clusters} cluster")
# Menampilkan anggota dari cluster terbaik
for cluster in range(best_n_clusters):
    cluster_members = df[df['Cluster'] == cluster]
    print(cluster_members)

# Plot Dendrogram
plt.figure(figsize=(10, 7))
dendrogram(linked,
            orientation='top',
            distance_sort='descending',
            show_leaf_counts=True)
plt.title(f'Dendrogram Agglomerative Hierarchical Clustering dari Total Serangan per Jam (Cluster Terbaik={best_n_clusters})')
plt.show()