import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
import random
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import pylab as pl
from kmeans import KMeansCluster
from kmeans import optimal_k

iris = load_iris()
pca = PCA(n_components=2).fit(iris.data)
pca_2d = pca.transform(iris.data)

for i in range(0, pca_2d.shape[0]):
  if iris.target[i] == 0:
    c1 = pl.scatter(pca_2d[i,0], pca_2d[i,1], c='r', marker='+')
  elif iris.target[i] == 1:
    c2 = pl.scatter(pca_2d[i,0], pca_2d[i,1],c='g', marker = 'o')
  elif iris.target[i] == 2:
    c3 = pl.scatter(pca_2d[i,0], pca_2d[i,1], c='b', marker='*')

pl.legend([c1,c2,c3], ['Setosa', 'Versicolor','Virginica'])
pl.title('Iris dataset, 3 species labeled')
pl.show()


kmeans = KMeans(n_clusters=3, random_state=8).fit(pca_2d)

for i in range(0, pca_2d.shape[0]):
  if kmeans.labels_[i] == 0:
    c1 = pl.scatter(pca_2d[i,0], pca_2d[i,1], c='r', marker='+')
  elif kmeans.labels_[i] == 1:
    c2 = pl.scatter(pca_2d[i,0], pca_2d[i,1],c='g', marker = 'o')
  elif kmeans.labels_[i] == 2:
    c3 = pl.scatter(pca_2d[i,0], pca_2d[i,1], c='b', marker='*')

pl.legend([c1,c2,c3], ['Cluster1', 'Cluster2','Cluster3'])
pl.title("Iris dataset, clustered with SKLearn's k-Means")
pl.show()


kbeans = KMeansCluster(3)
kbeans.fit(pca_2d)

for i in range(0, pca_2d.shape[0]):
  if kbeans.labels[i] == 0:
    c1 = pl.scatter(pca_2d[i,0], pca_2d[i,1], c='r', marker='+')
  elif kbeans.labels[i] == 1:
    c2 = pl.scatter(pca_2d[i,0], pca_2d[i,1],c='g', marker = 'o')
  elif kbeans.labels[i] == 2:
    c3 = pl.scatter(pca_2d[i,0], pca_2d[i,1], c='b', marker='*')

pl.legend([c1,c2,c3], ['Cluster1', 'Cluster2','Cluster3'])
pl.title("Iris dataset, clustered with my handcrafted k-Means")
pl.show()


ks = range(1, 20)
errors = [optimal_k(pca_2d, k) for k in ks]

plt.plot(ks, errors)
plt.xticks(ks)
plt.xlabel('k')
plt.ylabel('Total suared error')
plt.title('Elbow plot for chosing optimal k')
plt.show()