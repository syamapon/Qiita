import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)

for x in np.linspace(-1, 1, 11):
    for y in np.linspace(-1, 1, 11):
        marker = '8'
        if x > 0 and y > 0:
            marker = '$1$'
        elif x < 0 and y > 0:
            marker = '$2$'
        elif x < 0 and y < 0:
            marker = '$3$'
        elif x > 0 and y < 0:
            marker = '$4$'

        pOrg = np.array([x, y])
        pTra = np.array([[2, 1], [1, 3]]) @ pOrg

        ax.annotate('', xy=pTra,
                        xytext=pOrg,
                        arrowprops=dict(shrink=0.1, width=1, headwidth=3))

        plt.plot(pOrg[0], pOrg[1], marker = marker)
        plt.plot(pTra[0], pTra[1], marker = marker)

ax.set_xlim([-4, 4])
ax.set_ylim([-4, 4])
plt.show()
