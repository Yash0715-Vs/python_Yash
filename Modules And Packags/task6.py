import numpy as np

prices = np.array([100, 200, 350, 500, 750])

increase = prices * 0.10

new_prices = prices + increase

print(new_prices)