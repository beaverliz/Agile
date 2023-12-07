#!C:\Users\Professional\AppData\Local\Programs\Python\Python38-32\python.exe
import sys
import json
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.cluster import KMeans
import time

sys.path.append("c:\\users\\professional\\appdata\\local\\programs\\python\\python38-32\\lib\\site-packages")

save_path = '..\\saved_plots\\'

def cluster(x, y):
    num_clusters = 4
    data = list(zip(x, y))
    kmeans = KMeans(n_clusters=num_clusters, random_state=0)
    kmeans.fit(data)
    cluster_centers = kmeans.cluster_centers_
    labels = kmeans.labels_

    fig, ax = plt.subplots()

    for i in range(num_clusters):
        cluster_data = [data[j] for j in range(len(data)) if labels[j] == i]
        cluster_x, cluster_y = zip(*cluster_data)
        ax.scatter(cluster_x, cluster_y, label=f'Cluster {i + 1}')

        overlapping_counts = Counter(cluster_data)
        for point, count in overlapping_counts.items():
            ax.annotate(str(count), xy=point)

    center_x, center_y = zip(*cluster_centers)

    ax.scatter(center_x, center_y, s=100, c='red', marker='x', label='Cluster Centers')
    plt.title('Кластеризация точек на 4 кластера')
    plt.xlabel('P')
    plt.ylabel('N')
    plt.legend()
    file_name = f'cluster_plot_{int(time.time())}.png'
    file_path = save_path + file_name
    plt.savefig(file_path)
    plt.close()

    return file_path

p_array = json.loads(sys.argv[1])
n_array = json.loads(sys.argv[2])
result_path = cluster(p_array, n_array)
print(json.dumps(result_path))
