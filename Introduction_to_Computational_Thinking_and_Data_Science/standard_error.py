def standard_error_of_mean(population_std, sampleSize):
    '''
    Given the population standard deviation and sample size, 
    compute the standard error of sample mean
    '''
    return population_std/sampleSize**0.5 

### relationship between standard deviation and standard error:
### to compute standard deviation, we have to take multiple samples and calculate how much they vary 
### to compute standard error, we look at one sample, using the formula above, and we get the same number more or less

### Notice in the formula, we have to get the population standard deviation
### How do we do that?
### We see from the class example that if the sample size is large enough, the sample std is a pretty good approximation of population std 

### Does Distribution Matter? Yes it does. The more skew you have, the more samples you will need to get a good approximation
### Does population size matter? Shockingly no.

### Conclude: we choose the sample size based on some kind of measure of the skew of the population
### Key: pick independent samples






