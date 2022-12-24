import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter


n_bins = 20
x = ("carlos", "carlos", "joao", "maria")
y = (1, 2, 3, 4, 5)


plt.hist(x)
plt.show()
