import numpy as np

temperatures = np.array([
    [32, 35, 31, 30, 33, 36, 34],
    [28, 30, 29, 31, 32, 33, 30],
    [35, 37, 36, 38, 39, 40, 37]
])
print(f"shape: {temperatures.shape}")
print(f"the overall average: {np.mean(temperatures)}")
print(f"the higest: {np.max(temperatures)}")
print(f"the lowest: {np.min(temperatures)}")
print(f"the avg temp of each day: {np.mean(temperatures, axis =1)}")
print(f"the highest temperature of each city.: {np.max(temperatures, axis =1)}")
print(f"the temp> 35: {temperatures[temperatures>35]}")
print(f"the temp between 30 and 35: {temperatures[(temperatures >= 30) & (temperatures <= 35)]}")
print(f"the temp increace by 2: {temperatures+2}")
print(f"the reshape: {temperatures.reshape(7,3)}")
print(type(temperatures))