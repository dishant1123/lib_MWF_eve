import numpy as np 
# vstack : vertical stack 

"""
arr1 =np.array([1,2,3,4,5])
arr2 =np.array([
    [1,2,3],
    [4,5,6]
])

result = np.vstack(arr1)
print("original array : \n",arr1)
print("vertical array :\n",result)

print("original array 2: \n",arr2)
result2 =np.vstack(arr2)
print("vertical array 2: \n",result2)
"""
# hstack : horizontal stack

"""arr1 =np.array([1,2,3,4,5])
arr2 =np.array([
    [1,2,3],
    [4,5,6]
])

result = np.hstack(arr1)
print("original array : \n",arr1)
print("horizontal array :\n",result)

print("original array 2: \n",arr2)
result2 =np.hstack(arr2)
print("horizontal array 2: \n",result2)
"""

# hw :  what is  different between hstack and vstack and flatten and ravel? 

# concatenate :
'''
arr1 =np.array([1,2,3,4,5])
arr2 =np.array([6,7,8,9,10])

arr3 =np.array([
    [1,2,3],
    [4,5,6]
])  # -------> arr3 shape is  : (2,3)

"""arr4 =np.array([
    [11,12,13],
    [14,15,16],
    [17,18,19]
])"""

arr4 = np.array([
    [11,12,13,14],
    [15,16,17,18]
])   # ------> arr4 shape is  : (2,4)
# result = np.concatenate((arr1,arr2))
# print("original array : \n",arr1)
# print("original array 2: \n",arr2)

# print("concatenate array :\n",result)
print("arry 3: \n",arr3)
print("arry 4: \n",arr4)
print("concatenate array 2: \n",np.concatenate((arr3,arr4)))

# note : concatenate  only  possible when  col are same  in  both array. 

'''

# dstack : stacking in depth

"""arr1=np.array([
    [1,2,3,4],
    [5,6,7,8]
])

arr2 =np.array([
    [9,10,11,12],
    [13,14,15,16]
])

print("arry 1: \n",arr1)
print("arry 2: \n",arr2)
result = np.dstack((arr1,arr2))

print("dstack array :\n",result)
print("shape of dstack array :\n",result.shape)

arr4 = np.arange(1,33).reshape(2,2,2,4)  
print("arry 4: \n",arr4)
   #     -----> 2 *2  2 ,4 
"""

# split : 
"""
sales =np.array([1000,2000,3000,4000,5000,6000])

result =np.split(sales,3)
print("sales array :\n",sales)
print("split array :\n",result)
"""

# array_split :

"""sales =np.array([1000,2000,3000,4000,5000,6000,7000])

# result =np.array_split(sales,3)
result =np.array_split(sales,2)

print("sales array :\n",sales)
print("array_split array :\n",result)
"""

# insert ,delete,append :

"""arr=np.array([10,20,30,40,50,60,70,80,90,100])

print(np.append(arr,11))  # last add in arr 

result = np.insert(arr,4,600)
print("insert array :\n",result)

arr[5] =900 
print(arr)

result =np.delete(arr,5)  # ----> delete the  index wise 
print("delete array :\n",result)
"""

# view : 

"""arr=np.array([10,20,30,40,50,60,70,80,90,100])
arr2=arr.view()  # ----> arr2 =arr its  also  create the view 

arr[2]=1000

print("original array :\n",arr)
print("view array :\n",arr2)
"""

# copy :
arr=np.array([10,20,30,40,50,60,70,80,90,100])
arr2=arr.copy()  

arr[2]=1000

print("original array :\n",arr)
print("view array :\n",arr2)
