import random 
import math 
import scipy.integrate
import statistics

dist, numSamples = [], 1000000

for i in range(numSamples):
    dist.append(random.gauss(0, 100))

##### PDF for Normal Distribution
def gaussian(x, mu, sigma):
    part1 = 1/(sigma * (2*math.pi)**0.5)
    part2 = math.e**(-((x-mu)**2/(2*sigma**2)))
    return part1*part2

xVals, yVals = [], []
mu, sigma = 0, 1
x = -4

while x<=4:
    xVals.append(x)
    yVals.append(gaussian(x, mu, sigma))
    x += 0.05 

def checkEmpirical(numTrials):
    for t in range(numTrials):
        mu = random.randint(-10, 10)
        sigma = random.randint(1, 10)
        print('For mu = ', mu, 'and sigma = ', sigma)
        for numStd in (1, 1.96, 3):
            area = scipy.integrate.quad(gaussian, mu - numStd*sigma, mu + numStd*sigma, (mu, sigma))[0]
            print(f'Fraction within {numStd} std = {area}')


#checkEmpirical(100)

####### Simulating Buffon-Laplace Method 
#### statistically valid != true

def throwNeedles(numNeedles):
    inCircle = 0 
    for Needles in range(1, numNeedles + 1, 1):
        x = random.random() # generates a random float number between 0 to 1 
        y = random.random()
        if (x*x + y*y)**0.5 <= 1.0:
            inCircle += 1 
    return 4*(inCircle/float(numNeedles))

def getEst(numNeedles, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)

    std = statistics.stdev(estimates)
    current_estimate = sum(estimates)/len(estimates)
    print('Est. = ' + str(current_estimate))
    print('Std. = ' + str(round(std, 6)))
    print('Num of Needles = ', str(numNeedles))

    return (current_estimate, std)

def estimatePi(precision, numTrials):
    numNeedles = 1000
    std = precision
    while std >= precision/1.96:
        current_estimate, std = getEst(numNeedles, numTrials)
        numNeedles *= 2 
    return current_estimate

estimatePi(0.005, 100)


