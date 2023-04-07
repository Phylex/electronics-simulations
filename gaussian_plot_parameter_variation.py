#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

# set style for plot to be dark
plt.style.use('dark_background')

# set greens and blues as background
PALETTS = {'blue-green': ['navy', 'blue', 'royalblue', 'dodgerblue',
                          'deepskyblue', 'darkturquoise', 'turquoise',
                          'aqua', 'aquamarine'],
           'green-yellow': ['darkgreen', 'green', 'limegreen', 'lime',
                            'lawngreen', 'greenyellow', 'yellowgreen',
                            'olivedrap', 'darkolivegreen'],
           'red-yellow': ['firebrick', 'lightcoral', 'coral',
                          'orangered', 'red', 'darkorange',
                          'orange', 'gold', 'goldenrod'], }
BLOG_FIGSIZE = (10, 6)
mu = [-1, 0, 1]
sigma = [0.5, 0.8, 1, 1.2, 1.5]
x = np.linspace(-4, 4, 10000)
fig, ax = plt.subplots(figsize=BLOG_FIGSIZE)
for m, c in zip(mu, PALETTS['blue-green'][1:]):
    y = st.norm.pdf(x, loc=m)
    ax.plot(x, y, color=c, linewidth=2, label=r'$\mu$ = {}'.format(m))
plt.grid(linewidth=.2)
plt.tight_layout()
plt.legend()
plt.savefig('gaussian_vary_mu.svg', transparent=True)

fig, ax = plt.subplots(figsize=BLOG_FIGSIZE)
for s, c in zip(sigma, PALETTS['blue-green'][1:]):
    y = st.norm.pdf(x, scale=s)
    ax.plot(x, y, color=c, linewidth=2, label=r'$\sigma$ = {}'.format(s))
plt.grid(linewidth=.2)
plt.tight_layout()
plt.legend()
plt.savefig('gaussian_vary_sigma.svg', transparent=True)
