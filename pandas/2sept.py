# pandas :  pip install pandas
"""
1. data cleaning ----> remove  null values,remove duplicate rows ,fill missing values
2. data analysis ----> group by ,count , mean , median , sum , max , min , std , var ,  describe , corr , cov , plot 

3. using EDA  : exploratory data analysis
4. data transformaion : 
"""
import pandas as pd
import numpy as np
# seris  : 

"""s = pd.Series([12,46,73,84,95,36,17,18,19,110])
print(s)
print(type(s))

s1=pd.Series({'name' :['tanisha','suyog','ayushi','ayesha'],
              'marks' :[98,91,90,84]})
print(s1)
print(type(s1))

s2=pd.Series({"tanisha":98,"suyog":91,"ayushi":90,"ayesha":84})
print(s2)
print(type(s2))

s3=pd.Series([98,91,90,84],index=['tanisha','suyog','ayushi','ayesha'])
print(s3)

s4 =pd.Series([90,78,67,45,23],index=[1,2,3,4,5])
print(s4)

"""

# null values :

"""s5 =pd.Series([88,78,67,np.nan,23],index=[1,2,3,4,5])
print(s5)
print(s5.isnull().sum())
s5 =s5.fillna(76)
print(s5)
"""

# info ,describe,describe(include =all),head ,tail : 

s1=pd.Series([12,34,56,78,90,23,np.nan,67,89,100])
print(s1)
print(s1.head(2))  # by default  print first 5 rows
print(s1.tail(2))  # by default  print last 5 rows
print(s1.info()) 
print(s1.describe())
print(s1.describe(include ='all'))