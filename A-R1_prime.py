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
        x = random.uniform(0, 2.2)
        y = random.uniform(0, 1)
        if y*c <= (math.pow(x - split_val, power))/sum_:
            return x

power = 4
t = 1.0
x1 = 0
x2 = 2.2
sum_ = (math.pow(x2-t, power + 1) - math.pow(x1-t, power + 1)) / (power + 1)  
#sum_ =  0.697664
x = np.linspace(x1, x2, 100)
c = 1.2**4/sum_



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
