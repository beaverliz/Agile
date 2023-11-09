import random
import time
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.cluster import KMeans


def compare_two_numbers(m, n):
    m_str = str(m)
    n_str = str(n)

    position_match_count = 0
    value_match_count = 0

    m_letters = {}
    n_letters = {}

    if len(m_str) != len(n_str):
        raise ValueError('Введенное число не 6-значное')

    for i in range(len(m_str)):
        if m_str[i] == n_str[i]:
            position_match_count += 1
        else:
          if n_str[i] not in n_letters:
              n_letters[n_str[i]] = 1
          else:
              n_letters[n_str[i]] += 1
          if m_str[i] not in m_letters:
              m_letters[m_str[i]] = 1
          else:
              m_letters[m_str[i]] += 1

    intersection = set(m_letters) & set(n_letters)
    for l in intersection:
        value_match_count += min([m_letters[l], n_letters[l]])

    return position_match_count, value_match_count

def compare_many_numbers(number_amount, m):
    x_list = []
    y_list = []

    start_time = time.time()

    for i in range(number_amount):
        n = random.randint(100_000, 999_999)
        result1, result2 = compare_two_numbers(m, n)
        x_list.append(result1)
        y_list.append(result2)
        print(f'm = {m}, n = {n}')
        print(f'P({result1}), N({result2})')

    end_time = time.time()
    print(f'Затрачено времени {round(end_time - start_time, 2)} с')

    return x_list, y_list

def show_scatter(x, y):
    fig, ax = plt.subplots()
    ax.scatter(x, y)

    coordinates = list(zip(x, y))
    point_counts = Counter(coordinates)

    for point, count in point_counts.items():
        ax.annotate(str(count), xy=point)

    plt.xlabel('P')
    plt.ylabel('N')
    plt.show()

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
    plt.show()


if __name__ == '__main__':
    number_amount = 10_000
    add_number = 931_771
    x, y = compare_many_numbers(number_amount, add_number)
    show_scatter(x, y)
    # cluster(x, y)
