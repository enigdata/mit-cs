import random 

#Class Location (Immutable type)
class Location(object):
    def __init__(self, x, y):
        '''
        x and y are floats 
        '''
        self.x = x 
        self.y = y 

    def move(self, deltaX, deltaY):
        '''
        deltaX and deltaY are floats
        '''
        return Location(self.x + deltaX, 
                        self.y + deltaY)

    def getX(self):
        return self.x 

    def getY(self):
        return self.y 

    def distFrom(self, other):
        xDist = self.x - other.getX()
        yDist = self.y - other.getY()
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return f'<{str(self.x)}, {str(self.y)}>'

#Abstract Class 
# drunk class
# two subclasses of drunk: the 'usual' drunk, who wanders around at noon; the 'masochistic' drunk, who tries 
# to move northward

class Drunk(object):
    def __init__(self, name = None):
        self.name = name 

    def __str__(self):
        if self is not None:
            return self.name 
        return 'Anonymous'

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0,1), (0, -1), (1,0), (-1, 0)]
        return random.choice(stepChoices)

class MasochistDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0, 1), (0, -0.9), (1, 0), (-1, 0)]
        return random.choice(stepChoices)

#Class Field 
class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc #the drunk object has to be immutable

    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        deltaX, deltaY = drunk.takeStep()
        self.drunks[drunk] = self.drunks[drunk].move(deltaX, deltaY)

#Simulate a walk 
 
def walk(f, d, numSteps):
    '''
    f is a Field, 
    d is a Drunk,
    and numSteps is an int >=0

    Moves the drunk d with numSteps;
    Returns the distance between the final location and the start location.
    '''
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

#Simulate multiple walks
def simWalks(numSteps, numTrials, dClass):
    '''
    numSteps: int >= 0 
    numTrials: int >= 0 
    dClass: a subclass of Drunk 

    Simulates numTrials walks of numSteps steps each. 
    Returns a list of the final distances for each trial.
    '''

    Homer = dClass() 
    origin = Location(0,0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer, numSteps), 1))

    return distances 

def drunkTest(walkLengths, numTrials, dClass):
    '''
    walkLengths: a sequence of ints >= 0 
    numTrials: int >0
    dClass a subclass of Drunk 
    ''' 

    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, 'random walk of',numSteps, 'steps')
        print(' Mean =', round(sum(distances)/len(distances), 4))
        print(' Max =', max(distances))
        print(' Min =', min(distances))

print('Usual Drunk ===================>')
drunkTest((10, 100, 1000, 10000), 100, UsualDrunk)   

print('Masochistic Drunk ==================>')
drunkTest((10, 100, 1000, 10000), 100, MasochistDrunk)   


#Strange Field 
class OddField(Field):
    def __init__(self, numHoles = 1000, xRange = 100, yRange = 100):
        Field.__init__(self)
        self.wormwholes = {}
        for w in range(numHoles):
            x = random.randint(-xRange, xRange)
            y = random.randint(-yRange, yRange)
            newX = random.randint(-xRange, xRange)
            newY = random.randint(-yRange, yRange)
            newLoc = Location(newX, newY)
            self.wormwholes[(x, y)] = newLoc

    def moveDrunk(self, drunk):
        Field.moveDrunk(self, drunk)
        # do something peculiar after the move
        x = self.drunks[drunk].getX()
        y = self.drunks[drunk].getY()
        if (x, y) in self.wormwholes:
            self.drunks[drunk] = self.wormwholes[(x, y)]   


