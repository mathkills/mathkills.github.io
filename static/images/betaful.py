import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def figure01():
    x = np.linspace(0, 1, 300)
    
    cors = ['#00214e','#06366e','#424e6b','#60626f','#7c7a76','#9c9477','#beaf70','#e1cb5e','#ffea47']
    
    plt.figure(figsize=(15, 8))
    for i in range(9):
        plt.plot(x, stats.beta(i+3, 2).pdf(x), lw=5, c=cors[i])
        plt.plot(x, stats.beta(2, i+3).pdf(x), lw=5, c=cors[i])
    
    plt.axis(False)
    plt.savefig('betaful6', transparent=True)


def figure02():
    
    x = np.linspace(-1, 1, 100)

    y = 10*x + np.random.logistic(size=100)
    y[y>0] = 1
    y[y<=0] = 0


    plt.figure(figsize=(15,8))
    plt.scatter(x, y, color='#00214e')
    plt.xlim(-1.1,1.1)
    plt.ylim(-.1,1.1)
    plt.axis(False)
    plt.savefig('choicemodel1', transparent=True)

    plt.figure(figsize=(15,8))
    plt.scatter(x, y, color='k')
    plt.plot(x,1/(1+np.exp(-10*x)), color='#ffea47')
    plt.xlim(-1.1,1.1)
    plt.ylim(-.1,1.1)

    plt.axis(False)
    plt.savefig('choicemodel2', transparent=True)


def figure03():
    np.random.seed(450473)
    x = np.random.randn(900)
    y = -.3*x + np.random.randn(900)
    z = .5*x + np.random.normal(0,.7,size=900)

    plt.figure(figsize=(15,15))
    plt.plot(x, y, '.', color='#7c7a76', alpha=.2)
    plt.plot(x, z, '.', color='#7c7a76', alpha=.2)

    plt.xlim(-5,5)
    plt.ylim(-5,5)
    plt.axis(False)
    plt.savefig('cloud', transparent=True)

    plt.figure(figsize=(15,15))
    plt.plot(x, y, '.', color='#7c7a76', alpha=.2)
    plt.plot(x, z, '.', color='#00214e', alpha=.5)

    plt.xlim(-5,5)
    plt.ylim(-5,5)
    plt.axis(False)
    plt.savefig('cloudcolor', transparent=True)


figure03()





