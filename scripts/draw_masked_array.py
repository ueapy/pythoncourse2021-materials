import matplotlib.pyplot as plt
import matplotlib.patches as mpatch
import numpy as np
import os

nx = 5
ny = 4

np.random.seed(0)
mask = set(np.random.randint(0, nx*ny, 11))

fig = plt.figure(figsize=(nx//2*3, ny//2), facecolor='w')
# ax = fig.add_axes([0, 0, 1, 1], xticks=[], yticks=[], frameon=True)
ax = fig.add_subplot(132, xticks=[], yticks=[], frameon=False)
ax2 = fig.add_subplot(131, xticks=[], yticks=[], frameon=True)
ax3 = fig.add_subplot(133, xticks=[], yticks=[], frameon=True)

ax.set_title(r'${\tt mask }$')
ax2.set_title(r'${\tt array }$')
ax3.set_title(r'${\tt masked}$ ${\tt array }$')
ax.set_ylabel(r'${\tt + }$')
ax3.set_ylabel(r'${\tt || }$', labelpad=3)

n = 0
for i in range(nx):
    for j in range(ny):
        if n in mask:
            color = '#AAAAAA'
        else:
            color = '#FFFFFF'
        rect = mpatch.Rectangle((i, j), 1, 1,
                                facecolor=color,
                                edgecolor='w')
        rect2 = mpatch.Rectangle((i, j), 1, 1,
                                 facecolor='#FFFFFF',
                                 edgecolor='k')
        rect3 = mpatch.Rectangle((i, j), 1, 1,
                                 facecolor=color,
                                 edgecolor='k')
        ax.add_artist(rect)
        ax2.add_artist(rect2)
        ax3.add_artist(rect3)
        n += 1

for iax in (ax, ax2, ax3):
    iax.set_xlim((0, nx))
    iax.set_ylim((0, ny))
    iax.set_aspect('equal')

fig.savefig(os.path.join(os.path.pardir, 'figures', 'masked_array.png'),
            bbox_inches='tight')
