# Pie Chart

import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 7, 9, 6]
working = [8, 10, 6, 8, 9]
other = [9, 7, 11, 7, 9]

slices = [6, 9, 9]
activities = ['sleeping', 'working', 'other']
cols = ['c', 'm', 'r']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0, 0.1, 0),
        autopct='%1.1f%%')

plt.title('Pie Chart')
plt.show()
