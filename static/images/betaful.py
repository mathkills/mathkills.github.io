import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def figure(n):
    if n == 1:
        x = np.linspace(0, 1, 300)
        
        cors = ['#00214e','#06366e','#424e6b','#60626f','#7c7a76','#9c9477','#beaf70','#e1cb5e','#ffea47']
        
        plt.figure(figsize=(15, 8))
        for i in range(9):
            plt.plot(x, stats.beta(i+3, 2).pdf(x), lw=5, c=cors[i])
            plt.plot(x, stats.beta(2, i+3).pdf(x), lw=5, c=cors[i])
        
        plt.axis(False)
        plt.savefig('betaful6', transparent=True)


    elif n == 2:
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


    elif n == 3:
        np.random.seed(450473)
        x = np.random.randn(900)
        y = -.3*x + np.random.randn(900)
        z = .5*x + np.random.normal(0,.7,size=900)

        plt.figure(figsize=(15,8))
        plt.scatter(x, y, color='#7c7a76', alpha=.2)
        plt.scatter(x, z, color='#7c7a76', alpha=.2)
        plt.xlim(-5,5)
        plt.ylim(-5,5)
        plt.axis(False)
        plt.savefig('cloud', transparent=True)
        #plt.show()

        plt.figure(figsize=(15,8))
        plt.scatter(x, y, color='black', alpha=.5)
        plt.scatter(x, z, color='#7c7a76', alpha=.2)
        plt.xlim(-5,5)
        plt.ylim(-5,5)
        plt.axis(False)
        plt.savefig('cloudcolor', transparent=True)
        #plt.show()

        plt.figure(figsize=(15,8))
        plt.scatter(x, y, color='#7c7a76', alpha=.2)
        plt.scatter(x, z, c=x, cmap='inferno', alpha=.7)
        plt.xlim(-5,5)
        plt.ylim(-5,5)
        plt.axis(False)
        plt.savefig('cloudcolor2', transparent=True)
        #plt.show()

    elif n == 4:
        x = np.random.uniform(0,1,size=1000)
        y = np.random.uniform(0,1,size=1000)
        
        plt.hexbin(x,y, gridsize=16, cmap='inferno')
        plt.axis('equal')
        plt.show()

    elif n == 5:
        from matplotlib import image as mpimg

        #bayes = mpimg.imread('./Thomas_Bayes.gif')
        #bayes = bayes[:,:,0].astype(np.float64)
        #m,n = bayes.shape[0],bayes.shape[1]
        #bayes=np.column_stack((bayes,bayes[:,::-1]))
        #u,s,vh = np.linalg.svd(bayes/255., full_matrices=False)
        #s[12:] = 0
        #bayes = np.dot(u * s, vh)
        ##plt.imshow(bayes, cmap='inferno')
        #plt.imshow(np.row_stack((bayes,bayes[::-1])), cmap='inferno')
        #plt.axis(False)
        #plt.tight_layout()
        ##plt.savefig('bayesbayes_inferno.png', transparent=True, pad_inches=0)
        #plt.show()

        wsg = mpimg.imread('./William_Sealy_Gosset.jpg')
        m,n = wsg.shape[0],wsg.shape[1]
        wsg = np.row_stack((wsg,wsg,wsg))
        plt.imshow(wsg, cmap='inferno')
        plt.axis(False)
        plt.tight_layout()
        plt.savefig('multistudent_inferno.png', transparent=True)
        #plt.show()
        
figure(5)




### END FILE ###
