import random
import math
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#%matplotlib inline
sns.set_style('darkgrid')
plt.rcParams['figure.figsize'] = (12, 8)


def AceeptReject(split_val):
    global c
    global power
    while True:
        #x = 3*random.uniform(0, 1)
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if y*c <= math.pow(x - split_val, power):
            return x

power = 4
t = 0.4  
#sum_ = (math.pow(1-t, power + 1) - math.pow(-t, power + 1)) / (power + 1)  
sum_ =  0.0176
x = np.linspace(0, 1, 100)
c = 0.6**4/sum_

#x = np.linspace(0, 3, 100)
#c = 0.6**4/sum_


cc = [c for xi in x]
plt.plot(x, cc, '--',label='c*g(x)')
y = [math.pow(xi - t, power)/sum_ for xi in x]
plt.plot(x, y,label='f(x)')
samples = []
for  i in range(10000):
    samples.append(AceeptReject(t))
plt.hist(samples, bins=50, normed=True,label='sampling')
plt.legend()
plt.show()
