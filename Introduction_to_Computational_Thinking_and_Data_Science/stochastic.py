#Implementing a random process
import random 

def rollDie():
    return random.choice([1,2,3,4,5,6])

def testRoll(n=10):
    res = ''
    for i in range(n):
        res = res + str(rollDie())
    print(res)

# Simulation of Die Rolling
def runSim(goal, numTrials, txt):
    total = 0 
    for i in range(numTrials):
        res = ''
        for j in range(len(goal)):
            res += str(rollDie())
        if result == goal:
            total += 1 

    print(f'Actual probability of {txt} = {round(1/(6**len(goal)), 8)}')
    print(f'Estimated probability of {txt} = {round(total/numTrials, 8)}')

# Simulation for the classic birthday problem 
def sameDate(numPeople, numSame):
    possibleDates = range(366)
    birthday_hash = [0] * 366
    for p in range(numPeople):
        birth_date = random.choice(possibleDates)
        birthdays[birth_date] += 1 

    return max(birthdays) >= numSame 

#adjust the prior probabilities easily
def sameDate2(numPeople, numSame):
    possibleDates = 4 * list(range(0,57)) + [58] + 4 * list(range(59, 366)) + 4 * list(range(180,270))
    birthdays = [0] * 366 
    for p in range(numPeople):
        birth_date = random.choice(possibleDates)
        birthdays[birth_date] += 1 
    return max(birthdays) >= numSame 




