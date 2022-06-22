# Sub Plots

import matplotlib.pyplot as plt

fig = plt.figure()
fig.subplots_adjust(bottom=0.1, left=0.1, top=0.9, right=0.9)

plt.subplot(2, 1, 1)
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 4)
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 5)
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 6)
plt.xticks([])
plt.yticks([])

plt.show()
