import numpy as np
prices = np.array([100, 250, 500, 750, 1000, 1500, 2000])
print(prices[prices > 500])
print(prices[(prices < 500) | (prices > 1500)])
print(prices[prices < 500])