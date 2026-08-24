#np.eye :
import numpy as  np 


"""
1 2 3   (0,0)1  (0,1)2  (0,2)3
4 5 6   (1,0)4  (1,1)5  (1,2)6
7 8 9   (2,0)7  (2,1)8  (2,2)9

1 0 0
0 1 0
0 0 1

"""
# arr= np.eye(3,dtype=int)
"""arr= np.eye(4,dtype=int)
print(arr)
"""

# np.loadtxt : cleaning data , data type  ----> int  

"""arr=np.loadtxt("student.txt",skiprows=1,dtype=int)
print(arr)
print(arr.shape)
print(arr.mean())
print(arr.std())
print(arr.max())
print(arr.min())
"""

# ex : 2 using  student2 marks. txt : 
"""
arr = np.loadtxt("student2.marks",delimiter=",",dtype=int)
print(arr)
print(arr.shape)
print(arr.ndim)
print(arr.mean())
print(arr.std())
print(arr.max())
print(arr.argmax())  # index number of the max  value  

"""

# ex :3 genfromtxt :

"""arr =np.genfromtxt("student3.txt",delimiter=",",dtype=None,skip_header=1,filling_values=0)
print(arr)
"""

# ex :4 np.nan  -----> none 

"""arr= np.array([11,2,3,4,5,np.nan,6,7,8,9,11,2,3,4])
arr[5]=0
print("original  array :",arr)
"""
# unique : no repeat value included in this function 
"""
print("unique values :",np.unique(arr))
"""

# np.where :  use  for condition 

"""
arr=np.array([11,2,3,4,5,np.nan,6,7,8,9])
print("original  array :",arr)
# result = np.where(arr<11)
result = np.where(arr>=11)
print("result :",result)
"""

# np.nonzero : return index number of the non zero value
"""
arr=np.array([11,0,63,48,5,np.nan,6,7,8,9,0,0,0])
print(np.nonzero(arr))
"""
# np.all : 
"""arr=np.array([np.nan,1,2,3,4,5,6,7,8])
print(np.all(arr))
"""

# np.nanmean , np.nanstd ,np.nansum() : 

"""arr=np.array([11,0,63,48,5,np.nan,6,7,8,9,0,0,0])

print("mean :",np.nanmean(arr))
print("std :",np.nanstd(arr))
print("sum :",np.nansum(arr))
"""

# np.clip : 

arr=np.array([11,2,3,4,5,np.nan,6,7,8,9,11,2,3,4,21,23,45,51,52,-1,0])

result = np.clip(arr,1,50)
print("result :",result)