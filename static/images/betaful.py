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

        bayes = mpimg.imread('./Thomas_Bayes.gif')
        bayes = bayes[:,:,0].astype(np.float64)
        m,n = bayes.shape[0],bayes.shape[1]
        print(m,n)
        #bayes=np.column_stack((bayes,bayes[:,::-1]))
        u,s,vh = np.linalg.svd(bayes/255., full_matrices=False)
        s[1:] = 0
        bayes = np.dot(u * s, vh)
        #plt.imshow(np.row_stack((bayes,bayes[::-1])), cmap='inferno')
        plt.imshow(bayes, cmap='inferno')
        plt.axis(False)
        plt.tight_layout()
        plt.show()
        plt.imsave('compressedbayes_inferno.png', bayes, format='png', cmap='inferno')

    elif n==6:
        from matplotlib import image as mpimg

        wsg = mpimg.imread('./William_Sealy_Gosset.jpg')
        m,n = wsg.shape[0],wsg.shape[1]
        plt.imshow(wsg)
        plt.axis(False)
        plt.tight_layout()
        plt.show()
        plt.imsave('student_viridis.png', wsg, format='png', cmap='viridis')


    elif n==7:
        from matplotlib import image as mpimg
        
        bayes = mpimg.imread('./Thomas_Bayes.gif')
        bayes = bayes[:,:,0].astype(np.float64)
        m,n = bayes.shape[0],bayes.shape[1]
        u,s,vh = np.linalg.svd(bayes/255., full_matrices=False)
        s[12:] = 0
        bayes = np.dot(u * s, vh)
        revbayes = bayes[:,::-1]
        L1 = bayes[:m//3, :m//3]
        R1 = revbayes[:m//3, -m//3 + 1:]
        L2 = bayes[:m//3, -m//3+1:]
        R2 = revbayes[:m//3, :m//3]

        pic1 = np.column_stack((L2,L1,R1,R2))
        pic2 = np.column_stack((L2,L1,R1,R2))

        pic1 = np.row_stack((pic1[::-1],pic1))
        pic2 = np.row_stack((pic2[::-1],pic2))

        pic = np.row_stack((pic1,pic2))
        print(pic.shape)

        plt.imshow(pic, cmap='inferno')
        plt.axis(False)
        plt.show()
        plt.imsave('background_viridis.png', pic, format='png', cmap='viridis_r')

figure(5)




### END FILE ###
