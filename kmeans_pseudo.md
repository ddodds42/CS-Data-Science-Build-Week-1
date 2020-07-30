K-Means clustering: an unsupervised statistical learning algorithm for
identifying similar "clusters" which emerge in the data.

THE PSEUDOCODE:

Give it a CLASSY name:
    INITIALIZATION... the class takes as a parameter:
        K, or the number of clusters you want it to identify
        And initializes with an empty variable for mean cluster point values
    
    Function for PREDICTING cluster membership takes as parameters:
    A single input value (point in space), and the Kmean's class variables
        For k number of means, calculates input's squared distance to each mean,
    Returns the spatially closest k-mean
    
    Function for FITTING the K-Means instance to the data takes as parameters:
    A set of input values (points in space), and the Kmean's class variables
        Assign self-means to k number of randomly selected input points
        Make a VAR_A to track whether points were reassigned a new cluster

        Until there's no points reassigned new clusters
        Predict each input's cluster membership to self-means, store it in a
        VAR_B list of cluter assignments

        If VAR_A adn VAR_B are identicle:
            Return those predictions. No points were reassigned to new clusters
        
        Else, set VAR_A equal to VAR_B

        For each of k clusters:
            Label which points were assigned to each cluster, store it in VAR_C
            Calctulate the new mean location of each cluster based on it's new
            membership in VAR_C


OPTIMAL_K suplemental function to determine the best number of cluster:
It takes as parameters the input points and a k value.
    Instantiate a clustering class to use for iterating k values
    Fit the clustering instance to the input value points
    VAR_A to hold the means output when clustering
    VAR_B to store cluster prediction labels with their input point
    Sum the squared euclidean distance of each input to its cluster mean point
    Return the sum


SCIPYABLE euclidean_dist & squared_dist
scipy.spatial.distance.euclidean()

NUMPYABLE means of np.dot(np.array([]), axis=0)