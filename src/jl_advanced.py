import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

np.random.seed(123)
plt.style.use('fivethirtyeight')
font = {'weight': 'bold', 'size': 16}
plt.rc('font', **font)

def bootstrap(arr, resamples=10):
    arr_out = []
    for i in range(resamples):
        idxs = np.random.randint(arr.shape[0], size=arr.shape[0])
        boot = arr[idxs]
        arr_out.append(boot)
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

    data = np.loadtxt('../data/law_sample.txt')
    x = data[:,0]
    y = data[:, 1]
    corr = stats.pearsonr(x,y)
    print(f'The correlation for this is {corr[0]:.2f}')
    stat_function = lambda x: stats.pearsonr(x[:,0],x[:,1])[0]
    lo, hi, boot = bootstrap_ci(data, stat_function=stat_function)
    """
    # 3 The 95% CI is from 0.462 to 0.96 so there is a positive correlation 
    between first semester GPA and LSAT Score
    """
    print(lo,hi)
    fig, ax = plt.subplots()
    boot_hist(ax, boot)
    # plt.show()
    """
    #5 The pearson correlation for all the data is 0.76 which falls between the 
    95% CI on the bootstrapped data
    """
    all_data = np.loadtxt('../data/law_all.txt')
    print(stats.pearsonr(all_data[:,0], all_data[:,1])[0])
