##### Functions for evaluating classifiers
def accuracy(truePos, falsePos, trueNeg, falseNeg):
    numerator = truePos + trueNeg
    denominator = truePos + trueNeg + falsePos + falseNeg
    return numerator/denominator

def sensitivity(truePos, falseNeg):
    ### Out of all the predicted positives, how much is right?
    try:
        return truePos/(truePos + falseNeg)

    except ZeroDivisionError:
        return float('nan')

def specificity(trueNeg, falsePos):
    ### Out of all the actual negatives, how much did we catch?
    try:
        return trueNeg/(trueNeg + falsePos)
    except ZeroDivisionError:
        return float('nan')

####### K-nearest Neighbors
### Build examples and divide data into training and test sets
class Runner(object):
    def __init__(self, gender, age, time):
        self.featureVec = (age, time)
        self.label = gender 

    def featureDist(self, other):
        dist = 0.0 
        for i in range(len(self.featureVec)):
            dist += abs(self.featureVec[i] - other.featureVec[i])**2
        return dist**0.5 

    def getTime(self):
        return self.featureVec[1]
    
    def getAge(self):
        return self.featureVec[0]

    def getLabel(self):
        return self.label 

    def getFeatures(self):
        return self.featureVec 

    def __str__(self):
        return str(self.getAge()) + ', ' + str(self.getTime())\
                + ', ' + self.label 

def buildMarathonExample(fileName):
    data = getBMData(filename)
    examples = []
    for i in range(len(data['age'])):
        a = Runner(data['gender'][i], data['age'][i], data['time'][i])
        examples.append(a)
    return examples

def divide80_20(examples):
    Indices = random.sample(range(len(examples)), len(examples)//5)
    trainingSet, testSet = [], []
    for i in range(len(examples)):
        if i in Indices:
            testSet.append(examples[i])
        else:
            trainingSet.append(examples[i])
    return trainingSet, testSet

#Finding the k-nearest neighbors
def findKNearest(example, exampleSet, k):
    kNearest, distances = [], []
    #Build lists containing first k examples and their distances
    for i in range(k):
        kNearest.append(exampleSet[i])
        distances.append(example.featureDist(exampleSet[i]))
    maxDist = max(distances)
    for e in exampleSet[k:]:
        dist = example.featureDist(e)
        if dist < maxDist:
            #replace further neighbor by this one
            maxIndex = distances.index(maxDist)
            kNearest[maxIndex] = e 
            distances[maxIndex] = dist 
            maxDist = max(distances)
    return kNearest, distances

