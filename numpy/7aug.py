"""
data type  : 
1.string  : immutable  ---> not changes in string. 
2. list   : mutable   ----> changes in list 
3. tuple : immutable  ---> no changes in tuple 
4. dict : mutable  ---> key value  ---> changes in dict 
5. set  : mutable  ----> changes in set ---> no duplicate values store in set 
    -----> fronzen set  ---> immutable set 

"""

s1="hello"
print(s1)
print(type(s1))

l1=[12,34,56,78,True,False,78j ,"ram"] # list  access index number  : start 0 
print(l1)
print(type(l1))
print(l1[2])
print(l1[3:5])  # 3 start index 5 end index
print(l1[-1])

"""t1=(12,34,56,78,True,False,78j ,"ram")

print(t1)
print(type(t1))

t2 =23,
print(t2)
print(type(t2))
"""
"""d1 ={"phy" : 90 , "che" : 78,90 :"com"}
print(d1)
print(type(d1))
print(len(d1))

s1={12,2,2,2,4,5,6,6,7,8,9,10,"ase"}
print(s1)
print(type(s1))

fz =frozenset({12,45,67,89,90,90})
print(fz)
print(type(fz))
"""

# numpy : 
"""
1. mathematical functions , operations , matrix 
2. less memory usage
3. list vs  numpy 

"""
import numpy as np

a=np.array([10,20,30,40,50,60,70,80,90,100,110,120,90,True])
print(a)
print(type(a))
print(a[0])
print(a[4])
print(a[-5])

"""
A        B
1 2 3   11  12 13
4 5 6   14  15 16 
7 8 9   17  18 19

"""
