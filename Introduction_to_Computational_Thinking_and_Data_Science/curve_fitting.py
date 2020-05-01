### Objective Function
### Linear Regression
### Linearly regress (or walk downhill)

import numpy as np 

### How do we know how good is the fit?
def aveMeanSquareError(data, predicted):
    error = 0 
    for i in range(len(data)):
        error += (data[i] - predicted[i])**2 
    return error/len(data)

### Need a scale-independent measure
### R squared
def rSquared(observed, predicted):
    error = ((predicted - observed) **2).sum()
    #Trick: divide numerator and denominator by len(observations)
    numerator = error/len(observed)
    denominator = np.var(observed)
    return 1 - numerator/denominator

# R squared answers: what portion of the variability in the data is accounted for by my model



