import numpy as np
"""
slicing in array  : 
"""
# ex :1 slice   in 1d array:

"""
arr = np.array([12,34,56,78,234,560,89,99])
# access ----> index ---->start ----> 0   negative index : -1 
print(arr)
print(arr.shape) # (8,)  (,8) ----> row and col 
print(arr.ndim)  # 1d 

print(arr[5])   # pos index :L to r 
print(arr[-5])   # neg index :  r to  l 
print(arr[2:5])   # 2 start index  5 end index 
print(arr[ 0 : 6 :2])  # 0  start   6 end   2 step size 

print(arr[-2 : -5 : -1])  # -2 start index -5 end  index 
print(arr[-5: -2])  # -2 start index -5 end  index 

print(arr[ : : 2])
print(arr[ : : -2])
print(arr[ : : -1])
"""

# ex : 2 slice  in 2d array :

arr=np.array([
 [ 1 , 2 , 3,  4,  5,  6],  #0  ---->6  4  2 
 [ 7 , 8 , 9, 10, 11, 12],  #1 
 [13, 14, 15, 16, 17, 18],  #2  ---->18 16 14
 [19, 20, 21, 22, 23, 24],  #3
 [25, 26, 27, 28, 29, 30]   #4  ---->30 28 26
])
# print(arr)

print(arr[1])  # first arg  :  row  , second arg : col
print(arr[1:3])
print(arr[1:4:2])
print(arr[0:5:3])

print(arr[1:3,1:3]) # row  :1:3  col  1:3 
print(arr[1:5, : : -1])
print(arr[0: 5 :2, : : -2])  # row : 0  stop : 5 step 2 
# t : 6 4 2 18 16 14 30 28 26 
"""
1 1 1 1 1 
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1 

"""
