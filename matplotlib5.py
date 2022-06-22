# Area Plot

import matplotlib.pyplot as plt
days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 7, 9, 6]
working = [8, 10, 6, 8, 9]
other = [9, 7, 11, 7, 9]

plt.plot([], [], color='m', label='Sleeping', linewidth=5)
plt.plot([], [], color='c', label='Working', linewidth=5)
plt.plot([], [], color='r', label='Other', linewidth=5)

plt.stackplot(days, sleeping, working, other, colors=['m', 'c', 'r'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Stack Plot')
plt.legend()
plt.show()
