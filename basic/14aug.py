import numpy as np

# create array : 

"""
arr = np.array([1,2,3,4,5,6,7])
print(arr)
arr2 =np.array([12,34,56,78,90.78,2334])
print(arr2)
print(type(arr))
"""
"""arr=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(arr)
"""
"""arr1=np.array([[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]])
print(arr1)
"""
# array attributes : nidm ,type ,shape ,size,itemsize

"""arr=np.array([
    [1,2,3],
    [4,5,6]
    
])
print(arr)
print(arr.ndim)# number of dimensions
print(arr.dtype)# data type
print(arr.shape)# number of rows and columns
print(arr.size)# number of elements
print(arr.itemsize)# size of each element
"""

# update : 

# arr = np.array([10,20,30,40,50,60,70])

# print(arr)
# print(arr[4])
# ----> update  in array  index 4 99 
# arr[4] =99
# print(arr)

"""arr1 =np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(arr1)
print(arr1[1])
print(arr1[1][2])

arr1[1][2] =99
arr1[0][-1] =100

print(arr1)
"""

# 
"""arr =np.array(
    [[1,2,3,56],   #row  1  ----> 0
     [4,5,6,54],  # row 2   ----> 1
     [7,8,9,34]]   # row 3   ----> 2
)

arr[1,2] =888
arr[1:3,1:2] =777
print(arr)
"""

# method  : np.arange , np.zero,np.ones ,np.full

"""arr =np.arange(1,10)  # start , stop  , step 
arr =np.arange(10)
arr =np.arange(1,10,2)  # start 1  end 10  step 2
arr =np.arange(1,10,3)  # start 1  end 10  step 2

print(arr)
"""

# np.zero :

"""
arr=np.zeros(4,dtype=int)  # 4 zeros
arr =np.zeros((4,3),dtype=int)  # 4 3 zeros
print(arr)
"""
# np.ones :
"""arr=np.ones(4)  # 4 ones
arr =np.ones((3,3),dtype=int)  # 3 3 ones
print(arr)
"""

# np.full :

arr= np.full((4,3),fill_value=100,dtype=int)  # 4 3 100
print(arr)
