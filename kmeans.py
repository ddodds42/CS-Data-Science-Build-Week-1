from scipy.spatial.distance import euclidean
import random
import numpy as np

class KMeansCluster:
    '''
    K-Means clustering: an unsupervised statistical learning algorithm for
    identifying similar "clusters" which emerge in the data.
    '''
    
    def __init__(self, k):
        self.k = k      # number of clusters you want it to identify
        self.means = None       # mean cluster point values
        self.labels = None    # tracks points assignment to cluster
    
    def predict(self, input):

      '''
      Function for PREDICTING cluster membership takes.
      '''
      eachk = range(self.k)
      # calculates each input's squared distance to its mean
      closest = min(eachk, key=lambda i: euclidean(input, self.means[i])**2)
      return closest
    
    def fit(self, inputs):
        '''
        Fits the K-Means instance to the data points you want analyzed for clusters
        '''
        # Assign self-means to k number of randomly selected input points
        self.means =  random.sample(list(inputs),self.k)

        # re-fit until there no points are reassigned new ss
        while True:
            # Predict and store each input's cluster membership
            recluster = list(map(self.predict, inputs))

            if self.labels == recluster:
            # once no points are reassigned new clusters, return predictions
                return
            
            # Else, reasign cluster membership!
            self.labels = recluster

            for i in range(self.k):
                # Label and store which points were assigned to each cluster
                coords = [c for c, m in list(zip(inputs, self.labels)) if m == i]
                self.means[i] = np.mean(coords, axis=0)


def optimal_k(inputs, k):
    '''
    suplemental function to determine the best number of clusters
    '''
    # Instantiate a clustering class to use for iterating k values
    klusterer = KMeansCluster(k)
    # Fit the clustering instance to the input value points
    klusterer.fit(inputs)
    # Store the means output when clustering
    means = klusterer.means
    # squared distance of each input to its cluster mean point represents error
    return sum(euclidean(i, means[k])**2 for i, k in list(zip(inputs, klusterer.labels)))