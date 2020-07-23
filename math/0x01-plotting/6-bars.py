#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

people = ['Farrah', 'Fred', 'Felicia']
colors =  ['red', 'yellow', '#ff8000', '#ffe5b4']
for j in range(len(people)):
        a = 0
        for i in range(len(fruit)):
            plt.bar(people[j], fruit[i][j], bottom=a, width=0.5, color=colors[i])
            a += fruit[i][j]

plt.ylim(0, 80)
plt.legend(('apples', 'bananas', 'oranges', 'peaches'))
plt.title('Number of Fruit per Person')
plt.ylabel('Quantity of Fruit')
plt.show()
