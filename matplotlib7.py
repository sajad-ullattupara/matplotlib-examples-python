# Bar Graph

from matplotlib import pyplot as plt

plt.bar([0.25, 1.25, 2.25, 3.25, 4.25], [30, 70, 40, 60, 50],
        label="ProductA", width=.5)
plt.bar([.75, 1.75, 2.75, 3.75, 4.75], [50, 70, 30, 40, 60],
        label="ProductB", color='r', width=.5)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Sale')
plt.title('Sales Report')

plt.show()
