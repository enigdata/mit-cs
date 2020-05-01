##### Example: Temperature by Year
import numpy as np 

class tempDatum(object):
    def __init__(self, s):
        info = s.split(',')
        self.high = float(info[1])
        self.year = int(info[2][0:4])

    def getHigh(self):
        return self.high 

    def getYear(self):
        return self.year 

## Read Data
def getTempData():
    inFile = open('temperatures.csv')
    data = []
    for l in inFile:
        data.append(tempDatum(l))
    return data   

def getYearlyMeans(data):
    years = {}
    for d in data:
        try:
            years[d.getYear()].append(d.getHigh())
        except:
            years[d.getYear()] = [d.getHigh()]
    for y in years:
        years[y] = sum(years[y])/len(years[y])
    return years 

data = getTempData()
years = getYearlyMeans(data)
xVals, yVals = [], []
for e in years:
    xVals.append(e)
    yVals.append(years[e])

pylab.plot(xVals, yVals)
pylab.xlabel('Year')
pylab.ylabel('Mean Daily High (C)')
pylab.title('Select US Cities')

#### Cross Validation
### even in random sampling, run multiple trials
numSubsets = 10
dimensions = (1, 2, 3, 4)
rSquares = {}
for d in dimensions:
    rSquares[d] = []

def splitData(xVals, yVals):
    toTrain = random.sample(range(len(xVals)), len(xVals)//2)
    trainX, trainY, testX, testY = [], [], [], []
    for i in range(len(xVals)):
        if i in toTrain:
            trainX.append(xVals[i])
            trainY.append(yVals[i])
        else:
            testX.append(xVals[i])
            testY.append(yVals[i])
    return trainX, trainY, testX, testY

for f in range(numSubsets):
    trainX, trainY, testX, testY = splitData(xVals, yVals)
    for d in dimensions:
        model = pylab.polyfit(trainX, trainY)
        #predict_yVals = pylab.polyfit(trainX, trainY, d)
        predict_yVals = pylab.polyval(model, testX)
        rSquares[d].append(rSquared(testY, predict_yVals))

print('Mean R-squares for test data')
for d in dimensions:
    mean = round(sum(rSquared[d])/len(rSquares[d]), 4)
    std = round(np.std(rSquares[d]), 4)
    print('For dimensionality ', d, 'mean=', mean, ' std=', std)





