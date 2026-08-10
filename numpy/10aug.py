"""l1=[1,2,3,4,5,6]

l2=l1   # shallow copy  
l1.append(77)

print(l1)   # 1,2,3,4,5,6,77
print(l2)  # 1,2,3,4,5,6

l1=[1,2,3,4,5,6]
l2=l1.copy()   # deep  copy  
l1.append(77)

print(l1)  # 1 2 3 4 5 6,77
print(l2)  # 1 2 3 4 5 6 ,77 
"""

# pip install numpy  

import numpy as np

"""
arr =np.array([1,2,3,4,5,6])
print(arr)  # access index    =----> start index 0 
"""
# array attributes :

"""arr =np.array([1,2,30,4,5,60])

print(arr)
print(arr.shape)  # number  of rows and  columns
print(arr.ndim)  # number of dimensions
print(arr.dtype)  # data type  
print(arr.size)  # number of elements
print(arr.itemsize)  # size of each element
"""

# 2d array  : 

"""
arr =np.array(
    [[1,2,3],
     [4,5,6],
     [7,8,9]]
)
print(arr)
print(arr.shape)  # number  of rows and  columns
print(arr.ndim)  # number of dimensions
print(arr.dtype)  # data type
print(arr.size)  # number of elements
"""

# 3d array : 

"""arr =np.array(
    [[[1,2,3],
     [4,5,6],
     [7,8,9]]]
)
print(arr.ndim)
"""

# update  :

# arr =np.array([10,20,30,40,50,60])             
# arr[4]=999  # update 
# print(arr)

"""arr =np.array(
    [[1,2,3,56],   #row  1  ----> 0
     [4,5,6,54],  # row 2   ----> 1
     [7,8,9,34]]   # row 3   ----> 2
)
# arr[1,2] =888  # 1 ----> row index   2 ----> column index
# arr[1:3,1:2] =777  # row 1 start index   3 endindex 
arr[0:2 , 2] =88  # row 1 start index   3 endindex 

print(arr)
"""
# method  : np.arange , np.zero,np.ones ,np.full
"""arr =np.arange(1,10)  # last number excluded 
arr =np.arange(1,10,2)  # start 1  end 10  step 2 
arr =np.arange(1,10,4)

arr =np.arange(1,11).reshape(5,2)  # first arg  is row  and second is column
print(arr)
"""

# np.zeros 

"""arr =np.zeros(5,dtype=int)  # 5 zeros
arr =np.zeros((5,2),dtype=int)  # 5 zeros
print(arr)
"""

# np.ones :
"""arr=np.ones(5)  # 5 ones
arr=np.ones((3,3),dtype=int)  # 3 3 ones
print(arr)
"""

# np.full :

arr = np.full((4,3),fill_value=100,dtype=int)  # 4 3 999
print(arr)

# HW : 
"""
1.Create an array of 10 student marks using np.array().
2.Generate even numbers from 2 to 50 using np.arange().
3.Create 8 equally spaced values from 100 to 500 using np.linspace().
4.Create a 4*4 matrix of zeros.
5.Create a 5*5 identity matrix.
6.Generate 20 random marks between 35 and 100.
7.Select 3 random fruits using np.random.choice().
8.Use np.random.seed(50) and generate 10 random integers between 1 and 100. Compare the output by running the code twice.

 ----> 1,2 4 

"""

