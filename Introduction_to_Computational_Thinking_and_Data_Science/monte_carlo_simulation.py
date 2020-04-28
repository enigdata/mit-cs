import random 

### Roulette
class FairRoulette(object):
    def __init__(self):
        self.pockets = []
        for i in range(1, 37):
            self.pockets.append(i)
        self.ball = None 
        self.pocketOdds = len(self.pockets) - 1

    def spin(self):
        self.ball = random.choice(self.pockets)

    def betPocket(self, pocket, amt):
        if str(pocket) == str(self.ball):
            return amt * self.pocketOdds
        else:
            return -amt 

    def __str__(self):
        return 'Fair Roulette'

def playRoulette(game, numSpins, pocket, bet):
    total = 0 
    for i in range(numSpins):
        game.spin()
        total += game.betPocket(pocket, bet)
    print(f'{numSpins} spins of {game}')
    print(f'Expected return betting {pocket} =')
    print(str(100 * total/numSpins) + '%') 

    return total/numSpins

game = FairRoulette()
for numSpins in (100, 1000000):
    for i in range(3):
        playRoulette(game, numSpins, 2, 1)

#Casinos not in the business of being fair
class EuRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append('0')
    def __str__(self):
        return 'European Roulette'

class AmRoulette(FairRoulette):
    def __init__(self):
        EuRoulette.__init__(self)
        self.pockets.extend(['0', '0'])

    def __str__(self):
        return 'American Roulette'

###### Quantifying Variation in Data
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0 
    for x in X:
        tot += (x - mean)**2 

    std = (tot/len(X)) ** 0.5

    return mean, std 


    