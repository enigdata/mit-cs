###### Knapsack Problem
###Greedy algorithm 

#choose food example
class Food(object):
    def __init__(self, name, value, calories):
        self.name = name 
        self.value = value 
        self.calories = calories

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue()/self.getCost() 

    def __str__(self):
        return self.name + ': <' + str(self.value)\
            + ', ' + str(self.calories) + '>'


def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))

    return menu 

#Implementation of Flexible Greedy 
def greedy(items, maxCost, keyFunction):
    itemsCopy = sorted(items, key = keyFunction, reverse = True)
    result = []
    totalValue, totalCost = 0,0
    for i in range(len(itemsCopy)):
        if (totalCost + itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue() 

    return (result, totalValue)

def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken =', val)
    for item in taken:
        print(' ', item)

def multiple_test(foods, maxUnits):
    print('Use greedy by value to allocate,')
    testGreedy(foods, maxUnits, Food.getValue)
    print('Use greedy by cost to allocate,')
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
    print('Use greedy by density to allocate, ')
    testGreedy(foods, maxUnits, Food.density)

names = ['wine', 'beer', 'pizza', 'burger', 'fries',
'cola', 'apple', 'donut', 'cake']

values =  [89,90,95,100,90,79,50,10]
calories =  [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)
multiple_test(foods, 750)

