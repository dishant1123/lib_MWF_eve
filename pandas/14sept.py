# pandas : 
"""
1. read csv, read excel ,read_csv(tsv) , SQL file read 
2. head  tail  info describe  describe(all)
3. dataframe ----> dict , list 
4. loc  -----> label wise, lioc ----> index wise 
5. query ----> c ondition 
6. isna ---> value  missing ---> True 
7. missing  value  count ----> isna().sum() 
8. fillna ---> missing value fill  ----> direct fill or  mean , median,mode 
9. drop ---> colname  , axis  -----> reomve  the  row  or  col 
10.dropna ----> thresh limit , axis  ----> null value  
11.sort_value ----> sort by default  asc to desc ----> desc to asc  ----> asc =false 
12.sort_index ----> sort by index 
13.reset_index ----> index reset     

"""

import  pandas as pd
import numpy as np

"""df =pd.DataFrame({
    "id" :[1,2,3,4,5,6,7,8,9,10],
    'name' : [np.nan,"sita","ravan","bhudev","sahdev","minaxi","yug","ravan","bhudev","sahdev"],
    "age" :[56,25,44,41,np.nan,23,27,56,25,np.nan],
    "salary":[10000,20000,np.nan,8580,np.nan,96000,np.nan,10000,20000,np.nan]
})
print(df)
"""
"""
task  :1 person  who has salary  more than 20000 -----> name  , salary  ,age 
task : 2  print  col wise  missing value count
task : 3 fillna () ----> age  ----> median , salary ----> mean ,name  ----> ram 
task : 4 drop  -----> id 
task : 5 sort_value ----> salary  ----> asc to desc 
task : 6 assign the  new  index number and  sort  this  ----> using sort_index
task : 7 reset_index number  for  above task 5.    
"""

"""
days     sales 
1         1000
2         1500
3         1700
4         1300
5         1200  
6         2000  
7         1800
8         2300  
9         2500
10        50000  -----> 6000

outlier ----> its  effected to my avg  sales.

two ways  : 
1. IQR method  ----> inter quartile range

IQR = Q3 - Q1 -----> Q3 = 75 th percentile , Q1 = 25 th percentile

q1 = np.quantile(df['sales'],0.25)
q3= np.quantile(df['sales'],0.75)

IQR = q3 - q1

lower_limit = q1 - 1.5 * IQR
upper_limit = q3 + 1.5 * IQR -----> 6000

2. z score method  ----> z score
from scipy.stats import zscore
z_score = zscore(df['sales'])

z_score > 2    -----> outlier

# clip : 

"""
