"""
Broadcasting :

1.simple example  
2.2d array + 1d array 
3. multiply 
4. with columns : (2,3)  (2,) 

Important rule to remember

Two array dimensions are compatible when:
They are equal, or
One of them is 1, or
One array has no dimension there (because it has fewer dimensions).
"""

import numpy as np 
# ex :1 
"""
arr =np.array([12,45,67,89,90])
multiply = arr *2 

print(multiply)
"""
# ex :2 

"""arr =np.array([
    [1,2,3],
    [5,6,7]
])     # shape ------> 2,3   total  element  : 6

arr2 =np.array([
    [1],
     [2]
    ])  # -----> (2,)
print(arr.shape)
print(arr2.shape)
print(arr * arr2)
"""
# ex :3 

"""arr =np.array([
    [1,2,3],
    [5,6,7]
])

arr2=np.array([12,13,14])
print(arr + arr2)
"""