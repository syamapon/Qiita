import matplotlib.pyplot as plt
import numpy as np

p21 = np.array([2, 1])
p21to42 = np.array([[2, 0], [0, 2]]) @ p21

fig = plt.figure()
ax = fig.add_subplot(111)
ax.annotate('', xy=p21to42,
                xytext=p21,
                arrowprops=dict(shrink=0, width=1, headwidth=8))
ax.set_xlim([0, 5])
ax.set_ylim([0, 5])

plt.plot(p21[0], p21[1], marker='.')
plt.plot(p21to42[0], p21to42[1], marker='.')

plt.show()
