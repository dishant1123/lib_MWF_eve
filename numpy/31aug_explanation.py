import random
import numpy as np


"""arr =np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
np.random.seed(42)
result = np.random.randint(0,10,size=(3,3))
print(result)
"""


np.random.seed(2024)   #  seed ----> fix the  array  element. 
n_products = 10

base_price = np.random.randint(
    200, 3000, size=n_products
).astype(float)

print("Base Prices:", base_price)

units_m1 = np.random.randint(
    50, 500, size=n_products
).astype(float)
print("Units Month 1:", units_m1)


units_m2 = np.random.randint(
    50, 500, size=n_products
).astype(float)
print("Units Month 2:", units_m2)


units_m3 = np.random.randint(
    50, 500, size=n_products
).astype(float)
print("Units Month 3:", units_m3)


cost_price = base_price * np.random.uniform(
    0.4, 0.7, size=n_products
)
print("Cost Prices:", cost_price)

# revenue   , profit  : 