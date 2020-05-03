### Avoid cherry picking

#### A Hypothetical Example
# Massachusettes is about 10000 square miles
#About 36,000 new cancer cases per year
#Attorney partitioned state into 1000 regions of 10 squares miles each, and looked at distribution of cases
# Expected number of cases per region: 36
# Discovered that region 111 has 143 new cancer cases over a 3 year period! More than 32% greater than expected
# How worried should residents be?

##### How Likely is it just bad luck?
import random 

numCasesPerYear = 36000
numYears = 3
stateSize = 10000
communitySize = 10
numCommunities = stateSize//communitySize 

numTrials = 100
numGreater = 0 
for t in range(numTrials):
    result = [0] * numCommunities
    for i in range(numYears*numCasesPerYear):
        result[random.choice(range(numCommunities))] += 1 
    if result[111] >= 143:
        numGreater += 1 

prob = round(numGreater/numTrials, 4)
print('Estimated probability of region 111 having at least 143 cases=', prob)

anyRegion_numGreater = 0 
for trial in range(numTrials):
    result_2 = [0] * numCommunities 
    for i in range(numYears * numCasesPerYear):
        result_2[random.choice(range(numCommunities))] += 1 
    if max(result_2) >= 143:
        anyRegion_numGreater += 1 

prob_2 = round(anyRegion_numGreater/numTrials, 4)
print('Estimated probability of some region having at least 143 cases=', prob_2)
#around 60% prob!

