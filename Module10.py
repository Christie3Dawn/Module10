import matplotlib.pyplot as plt
import numpy as mp
import pandas as pd
import random
import ggplot


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

# Plot generated numbers using matplotlib
plt.plot(x1, y1, linewidth = 5, color = "c") # or color "m"
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Simple matplotlib Plot')

# Show the plot
plt.show()



# Plot with ggplot
ggplot(aes(x = x1, y = y1)) +\
       geom_line()