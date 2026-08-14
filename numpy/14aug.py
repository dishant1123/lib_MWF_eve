import numpy as np
# mathematical  function  : 

"""
arr= np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

arr1 =np.array([
    [11,12,13],
    [114,15,16],
    [17,18,19]
])

print(np.add(arr,arr1))
print(np.subtract(arr,arr1))
print(np.multiply(arr,arr1)) # it is not  matrix multiplication ----> matmul(),np.dot(),a@b
print(np.divide(arr,arr1))
print(np.power(arr,arr1))
print(np.remainder(arr1,arr))
"""
# sum ,axis , min ,max ,sort 
"""arr= np.array([
    [11,2,3],
    [4,5,-6],
    [7,-8,99]
])

print(np.sum(arr))
print(np.sum(arr,axis=0))  # axis =0 col wise sum 
print(np.sum(arr,axis=1))  # axis =1 row wise sum 

print(np.min(arr))
print(np.min(arr,axis=0))  # axis =0 col wise min
print(np.min(arr,axis=1))  # axis =1 row wise min

print(np.argmin(arr))  # index number of the minimum value
print(np.argmin(arr,axis=0))  
print(np.argmin(arr,axis=1))  

print(np.max(arr))
print(np.max(arr,axis=0))  # axis =0 col wise min
print(np.max(arr,axis=1))  # axis =1 row wise min

print(np.argmax(arr))  # index number of the minimum value
print(np.argmax(arr,axis=0))  
print(np.argmax(arr,axis=1))  

print(np.sort(arr)) # by default  row wise  asc to desc 
print(np.sort(arr,axis=0)) 
"""

# np.mode , np.sqrt ,np.exp ,np.log : 

"""
arr= np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(np.mod(arr,2))  # 1 % 2= 1   ---->same as np.remainder(arr,2) 
print(np.sqrt(arr)) 
print(np.exp(arr))  # e^x  ----> in maths e value is  : 2.71 
print(np.log(arr))  # log of arr
"""

# persontage and persontile :
"""arr= np.array([90,89,85,78])
print(np.percentile(arr,25))  # 25th percentile
"""
"""
Percentage = "How much did I get?"
Percentile = "How well did I rank compared to others?"


Concept	Meaning	Example
Percentage	Portion out of 100	80 marks out of 100 → 80%
Percentile	Position in distribution	80 marks at 90th percentile → better than 90% of students
"""

# staistical  method : mean  median  std  var

arr = np.array([12.67,45.90,78,1,4.21,10.01])

print(np.mean(arr))  # mean:25 
print(np.median(arr))  # median : 1 4 10 12 45 78  ----> n1+n2 /2  ----> 10 +12 /2 ===>11
print(np.std(arr))  
print(np.var(arr))
print(np.cumsum(arr))
print(np.prod(arr))  # multiply all the elements

print(np.floor(arr))  # floor of all the elements
print(np.ceil(arr))  # ceil of all the elements