import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

original = np.array([[0, 0], [0, 1], [1, 1], [1, 0], [0, 0]])
trans1 = np.array([[0, 0]])
trans2 = np.array([[0, 0]])
for ele in original:
    #_ele1 = np.array([[2, 1], [1, 3]]) @ ele
    #_ele2 = np.array([[0, -1], [1, 0]]) @ _ele1
    _ele1 = np.array([[0, -1], [1, 0]]) @ ele
    _ele2 = np.array([[2, 1], [1, 3]]) @ _ele1
    trans1 = np.vstack((trans1, np.array([_ele1])))
    trans2 = np.vstack((trans2, np.array([_ele2])))

ax1.plot(original[:,0], original[:,1], marker = ".", label='original')
ax2.plot(trans1[:,0], trans1[:,1], marker = ".", label='trans1')
ax3.plot(trans2[:,0], trans2[:,1], marker = ".", label='trans2')

ax1.legend(loc = 'upper center')
ax2.legend(loc = 'upper center')
ax3.legend(loc = 'upper center')
ax1.set_xlim([-4, 4])
ax1.set_ylim([-4, 4])
ax2.set_xlim([-4, 4])
ax2.set_ylim([-4, 4])
ax3.set_xlim([-4, 4])
ax3.set_ylim([-4, 4])
plt.show()
