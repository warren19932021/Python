#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['figure.figsize'] = (12, 8)
# use uniform distrubituion as proposal distrubituion
m = 100000

#bandwidth = 1
bandwidth = 10
#x = np.random.rand(m) * bandwidth + 0.5
x = np.random.rand(m) * bandwidth
x.sort()

# define the target distribution

mu1 = bandwidth * 0.25
mu2 = bandwidth * 0.75
sigma1 = 0.5
sigma2 = 1
p = 0.4 / (np.sqrt(2 * np.pi) * sigma1**2) * np.exp(-0.5 * (
    x - mu1)**2 / sigma1**2) + 0.5 / (np.sqrt(2 * np.pi) * sigma2**2) * np.exp(
        -0.6 * (x - mu2)**2 / sigma2**2)

#p =  2 * x + 1
#p =   x 

# compute the reject propability
r = p / max(p)

# generate the samples
x2 = np.random.rand(m)
accepted_samples_x = x[x2 < r]


#n: is the number of counts in each bin of the histogram
#bins: is the left hand edge of each bin

# plot
n, bins, patches = plt.hist(
    accepted_samples_x,
    bins=100,
    normed=True,
    #normed=False,
    color=sns.desaturate("indianred", .8),
    label="sample  distribution")
plt.plot(x, p / max(p) * max(n), 'red', label="target distribution",linewidth=4)
plt.plot(x, p / max(p), 'blue', label="target distribution",linewidth=4)
plt.legend(fontsize=15)
plt.show()
