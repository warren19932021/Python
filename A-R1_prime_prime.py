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
        if y*c <= (math.pow(x - split_val, power)):
            return x

power = 4
t = 1.0
x1 = 0
x2 = 2.2
sum_ =  0.697664
x = np.linspace(x1, x2, 100)
c = 1.2**4




samples = []
for  i in range(100000):
    samples.append(AceeptReject(t))
n, bins, patches = plt.hist(samples, bins=80, normed=False,label='sampling')

y = [math.pow(xi - t, power)/c*max(n) for xi in x]
plt.plot(x, y,label='f(x)')


cc = [max(n) for xi in x]
plt.plot(x, cc, '--',label='c*g(x)')


plt.legend()
plt.show()

