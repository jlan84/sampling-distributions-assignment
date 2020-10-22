import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
plt.style.use('fivethirtyeight')
font = {'weight': 'bold', 'size': 16}
plt.rc('font', **font)

def bootstrap(arr, resamples=10):
    arr_out = []
    for i in range(resamples):
        arr_out.append([])
        arr_out[i].append(np.random.choice(arr,size=arr.shape[0],replace=True))
    return np.array(arr_out)

def bootstrap_ci(sample, stat_function=np.mean, resamples=1000, ci=95):
    bootstrapped = bootstrap(sample, resamples=resamples)
    bootstrap_stat_lst = list(map(stat_function, bootstrapped))
    lo, hi = np.percentile(bootstrap_stat_lst, [(100-ci)/2, ci+(100-ci)/2])
    return lo, hi, bootstrap_stat_lst

def boot_hist(ax, bootstrapped_lst, title=None):
    ax.hist(bootstrapped_lst, bins=30)
    ax.set_title(title)
    


if __name__ == "__main__":
    
    productivity_arr = np.loadtxt('../data/productivity.txt')
    
    """
    #2 Because this sample may not be representative of the entire population. 
    The mean difference is a point estimate of the entire population and does not
    tell us anything unless we have a measure of how certain it is.
    """

    #3
    ci = 90
    lo, hi, bootstrap = bootstrap_ci(productivity_arr, ci=ci)
    print(f'The lower and upper bound for the {ci}% confidence interval are\
 {lo} and {hi} respectively.')

    fig, ax = plt.subplots()
    boot_hist(ax, bootstrap, 'Bootstrapped Mean')
    plt.show()

    """
    #5 We cannot say that switching the monitors caused an increase in 
     productivity using a 95% confidence interval due to the lower confidence 
     interval of 2.5% being negative

     Using a 90% CI, the lower bound mean was 0.68 hrs increase in productivity.
     Using this if we swapped, the minimum net profit increase would equal 
     100*2000*0.68 - 100*500
     """
    rev = 100*2000*lo
    cost = 100*500
    profit = (rev-cost)
    print(f'Using a 90% CI, the lower bound mean was 0.68 hrs increase in\
 productivity. Using this if we swapped, the minimum net profit increase would \
equal 100*2000*0.68 - 100*500 = ${profit:.2f}')

    