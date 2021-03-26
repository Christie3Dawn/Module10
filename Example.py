import matplotlib.pyplot as plt

fig, figure = plt.subplots()

data = {

    "Hamburger": 139,

    "Hotdog": 216,

    "Cheeseburger": 182,

    "Chili Cheese Dog": 57

}

x_axis_data = data.keys()

y_axis_data = data.values()

figure.bar(x_axis_data, y_axis_data)

figure.set(ylim=[0, 250],

           ylabel='Number of Orders',

           xlabel='Menu Item',

           title='Number of Orders for each Menu Item at the Baseball Game')

plt.show()

import numpy as np

import pandas as pd

from ggplot import *

from plotnine import *

plt.style.use('ggplot')

x = [0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]

y = [56, 68, 50, 72, 65, 63, 78, 84, 61, 76, 96, 81, 67, 87, 99, 91, 81, 72]

data2 = {'Hours': x, 'Score': y}

df = pd.DataFrame(data2, columns=['Hours', 'Score'])

print(df)

g = ggplot(aes(x='Hours', y='Score'), data=df) + geom_point()

print(g)