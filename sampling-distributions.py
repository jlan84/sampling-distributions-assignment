import numpy as np
import scipy.stats as stats
import pandas as pd

def bootstrap(x, resamples=10000):
    bootstrap_samples = []
    for i in range(resamples):
        bootstrap_sample = np.random.choice(x, size=len(x), replace=True)
        bootstrap_samples.append(np.array(bootstrap_sample))
    return np.array(bootstrap_samples)
x = np.array([1,5,8,10,15,20,4,7])
print(bootstrap(x).shape)

df = pd.read_csv('data/productivity.txt')
print(df.info())