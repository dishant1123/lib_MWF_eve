import pandas as pd
import numpy as np
# using  customer_data .csv file  : 

df =pd.read_csv("pandas/customer_data (1).csv")
print(df)

"""
# select name from customer_data 
# print  single  col : 
result = df['Name']
print(result)
"""

# using  multiple  columns :
# select Name , City , Salary from customer_data

"""multiple_col =df[['Name','City','Salary']]
print(multiple_col)
"""

# rename  column :
"""
df =df.rename(columns={"Name" : "First_Name","CustomerID" : "ID"})
df.rename(columns={"Name" : "First_Name","CustomerID" : "ID"},inplace=True)

print(df)

"""

#LOC : label based indexing

"""
result =df.loc[0]
result =df.loc[2:5]  # note : 2 start index  5 end index  ---> both inclusive
result =df.loc[2:5,['Name',"Salary"]] 
result =df.loc[2:5,"Name":"Salary"]

print(result)
"""

# iloc : integer based indexing
"""
result =df.iloc[0]
result =df.iloc[3:5]  # note : 3 start index  5 end index  ---> last index excluded
result =df.iloc[3:5,0:2]  # 3:5 ---> row slicing , 0:2 ---> column slicing
print(result)
"""

"""
HW
task  : 1 country  =="india" and year ==2002 print country  and year column using  loc or  iloc  or df . 
hint  : use & operator  for  condition 

a= df.loc[(df["country"]=="india") & (df["year"]==2002)]

task :2 in  mckinsey.csv dataset add new column col_name = next_year +3 display like  this  : 

    country,year,population,continent,life_exp,gdp_cap,next_year
0    Afghanistan,1952,8425333,Asia,28.801,779.4453145, 1955  
1    Afghanistan,1957,9240934,Asia,30.332,820.8530296, 1960
2    Afghanistan,1962,10267083,Asia,31.997,853.10071, 1965
3    Afghanistan,1967,11537966,Asia,34.02,836.1971382, 1970
4    Afghanistan,1972,13079460,Asia,36.088,739.9811058, 1975


"""
