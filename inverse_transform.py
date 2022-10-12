import numpy as np
import matplotlib.pyplot as plt

def sampleExp(Lambda = 2,maxCnt = 50000):
    ys = []
    standardXaxis = []
    standardExp = []
    for i in range(maxCnt):
        u = np.random.random()
        y = -1/Lambda*np.log(1-u) #F-1(X)
        ys.append(y)
    for i in range(1000):
        t = Lambda * np.exp(-Lambda*i/100)
        standardXaxis.append(i/100)
        standardExp.append(t)
    plt.plot(standardXaxis,standardExp,'r')
    #plt.hist(ys,1000,normed=True) # python 2
    #plt.hist(ys,1000,density=True) # python 3
    plt.show()

sampleExp()
