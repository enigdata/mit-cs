### Distance metrics 
### Minkowski distance 

def minkowskiDist(v1, v2, p):
    '''
    Assumes v1 and v2 are equal-length arrays of numbers
    Returns Minkowski distance of order p between v1 and v2 
    '''
    dist = 0 
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p 
    return dist**(1/p)

### Define Animal Class
class Animal(object):
    def __init__(self, name, features):
        self.name = name 
        self.features = pylab.array(features)

    def getName(self):
        return self.name 

    def getFeatures(self):
        return self.features

    def distance(self, other):
        '''
        Assumes other an Animal
        Returns the Euclidean distance between feature vectors of self and other
        '''
        return minkowskiDist(self.getFeatures(), other.getFeatures(), 2)

def compareAnimals(animals, precision):
    '''
    Assumes animals is a list of animals, precision an int>= 0
    Builds a table of Euclidean distance between each animal
    '''
    columnLabels = []
    for a in animals:
        columnLabels.append(a.getName())
    rowLabels = columnLabels[:]
    tableVals = []
    # Get distances between pairs of animals 
    # For each row
    for a1 in animals:
        row = []
        #For each column
        for a2 in animals:
            if a1 == a2:
                row.append('--')
            else:
                distance = a1.distance(a2)
                row.append(str(round(distance, precision)))
        tableVals.append(row)
    #Produce table
    table = pylab.table(rowLabels = rowLabels, 
                        colLabels = columnLabels,
                        cellText = tabelVals,
                        cellLoc = 'center',
                        loc = 'center',
                        colWidths = [0.2]*len(animals))
    table.scale(1, 2.5)
    pylab.savefig('distances')



