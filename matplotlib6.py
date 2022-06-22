# Histogram

import matplotlib.pyplot as plt
population_age = [5, 55, 23, 45, 1, 56, 43, 38, 97, 67, 46, 35, 67, 38, 29, 18, 84, 35,
                  68, 97, 34, 23, 12, 5, 16, 86, 93, 76, 75, 83, 64, 55, 58, 47, 35, 49, 32, 24, 27, 54]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.hist(population_age, bins, histtype='bar', rwidth=0.8)
plt.xlabel('Age group')
plt.ylabel('Number of people')
plt.title('Population_Histogram')
plt.show()
