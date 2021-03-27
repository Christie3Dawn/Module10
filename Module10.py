import matplotlib.pyplot as plt
import pandas as pd
import random
#from plotnine import ggplot, aes, geom_line
from plotnine import *


# Create random numbers to plot
x1 = []
for i in range(5):
    n = random.randint(1, 26)
    x1.append(n)

print(x1)


y1 = []
for i in range(5):
    n = random.randint(1, 26)
    y1.append(n)

print(y1)

# Plot generated using matplotlib
plt.plot(x1, y1, linewidth = 5, color = "c") # or color "m"
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Simple matplotlib Plot')

# Show the plot
plt.show()



# Plot with ggplot

df = pd.DataFrame({'x': x1, 'y': y1}, columns =['x', 'y'])

g = ggplot(aes(x='x', y='y'), data = df) +\
    geom_line(size = 3, color = "#d80c6b") +\
    xlab("x-axis") +\
    ylab("y-axis") +\
    ggtitle("Simple Plot with ggplot")

print(g)