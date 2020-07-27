import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

x = np.linspace(.01, 1, 300)

cors = ['#00214e','#06366e','#424e6b','#60626f','#7c7a76','#9c9477','#beaf70','#e1cb5e','#ffea47']

plt.figure(figsize=(15, 8))
for i in range(9):
    plt.plot(x, stats.beta(2, i+3).pdf(x), lw=5, c=cors[i])

plt.axis(False)
plt.savefig('betaful4', transparent=True)
