import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(123)
def bootstrap(x, resamples=10000):
    """Draw bootstrap resamples from the array x.

    Parameters
    ----------
    x: np.array, shape (n, )
      The data to draw the bootstrap samples from.
    
    resamples: int
      The number of bootstrap samples to draw from x.
    
    Returns
    -------
    bootstrap_samples: np.array, shape (resamples, n)
      The bootsrap resamples from x.
    """
    n = len(x)
    bootStrapList = []
    for i in range(resamples):
        bootStrapList.append([])
        for j in range(n):
            bootStrap = np.random.choice(x, replace=True)
            bootStrapList[i].append(bootStrap)
    return np.array(bootStrapList)

monitorChanges = np.loadtxt('data/productivity.txt')

#You cannot just report the mean change in productivity because you need to determin
#If the sample is representative of the population
# by setting a confidence interval.

def bootstrap_ci(sample, stat_function=np.mean, resamples=10000, ci=95):
    n = len(sample)
    data = bootstrap(monitorChanges)
    paramList = []
    for val in data:
        paramList.append(stat_function(val))
    lower = np.percentile(paramList, (100-ci)/2) 
    upper = np.percentile(paramList, ci+(100-ci)/2)
    return lower, upper, paramList

lower, upper, meanBS = bootstrap_ci(monitorChanges)

print(f'The lower and upper bound of the 95% confidence interval are {lower: .3f} \
and {upper: .3f}. Based on this, since the lower interval is negative, a change\
in monitors may lead to a decrease in productivity')

lower, upper, meanBS = bootstrap_ci(monitorChanges, ci=90)

print(f'The lower and upper bound of the 90% confidence interval are {lower: .3f} \
and {upper: .3f}. Based on this, using the lower bound of the CI, changing monitors\
may lead to an increase in revenue of $74n800 (0.624*100*2000 - 100*500)')


