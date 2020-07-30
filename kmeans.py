from scipy.spatial.distance import euclidean
import random
import numpy as np

class KMeans:
    '''
    K-Means clustering: an unsupervised statistical learning algorithm for
    identifying similar "clusters" which emerge in the data.
    '''
    
    def __init__(self, k):
        self.k = k      # number of clusters you want it to identify
        self.means = None       # mean cluster point values
    
    def predict(self, input):
    '''
    Function for PREDICTING cluster membership takes.
    '''
        eachk = range(self.k)
        # calculates each input's squared distance to its mean
        closest = min(eachk, key=lambda i: euclidean(input, self.means[i])**2)
        return closest