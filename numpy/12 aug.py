import  numpy as np
import random as r 

"""a=r.random()  # give  float  number between 0-1  
a=r.randrange(1,20,2)  # last number excluded  
a=r.randint(1,5)  # both  numbers are included

a=r.choice([1,2,3,4,"ram"])
a=r.choices([1,2,3,4,"ram"],k=3)
print(a)
"""

# using  random generate the numpy array :

"""arr = np.random.randint(low=-10,high=10,size=(3,3))
arr = np.random.randint(low=-10,high=10,size=25).reshape(5,5)

arr =np.random.random(size=(3,3))
arr=np.random.choice([1,2,3,4,5,6],size=(3,3))

np.random.seed(5)
print(np.random.randint(low=-10,high=10,size=(3,3)))

"""

# linspace :
"""arr =np.linspace(1,15,4)  # formula  : stop -start /step-1 ----> 10-1 / 5-1
print(arr)
"""

# airthematic operator : + - * / ** % //

"""
arr1 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

arr2 = np.array([
    [11,12,13],
    [14,15,16],
    [17,18,19]
])

print("original array arr1 is  : \n",arr1)
print("original array arr2 is  : \n",arr2)
"""
"""print("arr1 + arr2 is  : \n",arr1+arr2)
print("arr1 - arr2 is  : \n",arr1-arr2)
print("arr1 * arr2 is  : \n",arr1*arr2)  # it is not  matrix multiplication
print("arr1 / arr2 is  : \n",arr1/arr2)
print("arr1 // arr2 is  : \n",arr1//arr2)  # floor division  : int
print("arr1 % arr2 is  : \n",arr1%arr2)  # remainder  : int
"""

# matrix multiplication : np.dot() , np.matmul(), @ ---> matrix multiplication

"""
result =np.dot(arr1,arr2)
result =np.matmul(arr1,arr2)
result =arr1@arr2
print("arr1 * arr2 is  : \n",result)"""

# eye ,identity ,transpose ,T ,ravel(), flatten(),matrix  :

"""arr =np.eye(3)
arr=np.identity(4)
print(arr)

"""

# transpose :

"""
arr1 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print("original array arr1 is  : \n",arr1)
transpose = arr1.T
transpose = arr1.transpose()
transpose = np.transpose(arr1)
print("transpose of arr1 is  : \n",transpose)
"""

# flatten :

"""arr1 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

aar2=arr1.flatten()
arr1[2] =99

print("original array arr1 is  : \n",arr1)
print("flatten of arr1 is  : \n",aar2)
"""

# ravel :

"""arr1 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

aar2=arr1.ravel()

arr1[2]=99
print("original array arr1 is  : \n",arr1)
print("ravel of arr1 is  : \n",aar2)
"""

arr = np.arange(1,33).reshape(2,2,2,4)
print(arr)

