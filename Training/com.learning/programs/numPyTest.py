__author__ = 'aganiger'

import numpy as np

num = np.random.randint(low=10, high=30, size=10)

print(num)



# find most frequent vlaue in array
x = np.random.randint(0, 10, 40)
print("Original array:")
print(x)
print("Most frequent value in the above array:")
print(np.bincount(x).argmax())