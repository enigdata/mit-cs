import random 
from intro_machine_learning import minkowskiDist

### Class Cluster
class Example(object):
    def __init__(self, name, features, label = None):
        '''
        Assumes features is an array of floats
        '''
        self.name = name 
        self.features = features
        self.label = label 

    def dimensionality(self):
        return len(self.features)

    def getFeatures(self):
        return self.features[:]
    
    def getLabel(self):
        return self.label

    def getName(self):
        return self.name 

    def distance(self, other):
        return minkowskiDist(self.getFeatures(), others.getFeatures(), 2)

    def __str__(self):
        return self.name + ':' + str(self.features) + ':'\
                + str(self.label)

def Cluster(object):
    def __init__(self, examples):
        '''
        Assumes examples a non-empty list of Examples
        '''
        self.examples = examples
        self.centroid = self.computeCentroid()

    def update(self, examples):
        '''
        Assumes examples is a non-empty list of Examples
        Replace examples; return amount centroid has changed
        '''
        oldCentroid = self.centroid
        self.examples = examples
        self.centroid = self.computeCentroid()
        return oldCentroid.distance(self.centroid)

    def computeCentroid(self):
        vals = pylab.array([0.0] * self.examples[0].getFeatures())
        for e in self.examples: # compute mean
            vals += e.getFeatures()
        centroid = Example('centroid', vals/len(self.examples))
        return centroid

    def getCentroid(self):
        return self.centroid

    def variability(self):
        '''
        variability of data points in the cluster with regard to the cluster centroid
        '''
        total_distance = 0
        for e in self.examples:
            total_distance += e.distance(self.centroid) **2
        return total_distance

    def members(self):
        for e in self.examples:
            yield e 

    def __str__(self):
        names = []
        for e in self.examples:
            names.append(e.getName())
        names.sort()
        result = 'Cluster with centroid'\
            + str(self.centroid.getFeatures()) + 'contains:\n '
        for e in names:
            result = result + e + ','
        return result[:-2] # remove trailing comma and space at the end 

########### K-mean Clustering
def kmeans(examples, k, verbose = False):
    initialCentroids = random.sample(examples, k)
    clusters = []
    for e in initialCentroids:
        clusters.append(Cluster([e]))

    #Iterate until centroids do not change 
    converged = False
    numIterations = 0 
    while not converged:
        numIterations += 1 
        newClusters = []
        for i in range(k):
            newClusters.append([])

        #Associate each example with closest centroid
        for e in examples:
            #Find the centroid closest to e 
            minDistance = e.distance(clusters[0].getCentroid())
            index = 0 
            for i in range(1, k):
                distance = e.distance(clusters[i].getCentroid())
                if distance < minDistance:
                    minDistance = distance
                    index = i 

            #Add e to the list of examples for appropriate cluster
            newClusters[index].append(e)

        for c in newClusters: #avoid having empty clusters
            if len(c) == 0:
                raise ValueError('Empty Cluster')
        
        #Update each cluster; check if a centroid has changed 
        converged = True 
        for i in range(k):
              if clusters[i].update(newClusters[i]) > 0.0:
                  converged = False 
        if verbose:
            print('Iteration # ' + str(numIterations))
            for c in clusters:
                print(c)
            print(' ')

    return clusters 




def dissimilarity(clusters):
    'Input are cluster objects'
    total_distance = 0
    for c in clusters:
        total_distance += c.variability()
    return total_distance

def trykmeans(examples, numClusters, numTrials, verbose = False):
    '''
    calls kmeans numTrials times and returns the result with the lowest dissimilarity
    '''
    best = kmeans(examples, numClusters, verbose)
    minDissimilarity = dissimilarity(best)
    trial = 1
    while trial < numTrials:


