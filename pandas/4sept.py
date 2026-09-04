import pandas as pd 
# dataframe :

"""
2 ways  to  create the dataframe : 

1. list 
2. dict 
"""

# ex :1 create  dataframe : 

"""
df = pd.DataFrame({
    "id" : [101,102,103,104,105],
    "name" :["ram","sita","ravan","laxman","bhudev"],
    "salary" :[1000,2000,3000,4000,5000]
})
print(df)
"""
# list : 

"""
df =pd.DataFrame([
    [101,"ram",1000],
    [102,"sita",2000],
    [103,"ravan",3000],
    [104,"laxman",4000],
    [105,"bhudev",5000]
],columns =['id','name','salary'])
print(df)"""

# head ,tail ,info,describe,describe(include =all), : 
"""
df = pd.DataFrame({
    "id" : [101,102,103,104,105],
    "name" :["ram","sita","ravan","laxman","bhudev"],
    "salary" :[1000,2000,3000,4000,5000]
})

print(df)
print(df.head(2))  # by default  print first 5 rows
print(df.tail(2))  # by default  print last 5 rows
print(df.info())
print(df.describe()) # note : only numeric columns
print(df.describe(include ='all'))
"""

# read csv file  :   customer_data

"""df =pd.read_csv("pandas/customer_data (1).csv")
print(df)
print(df.head(3))
print(df.tail(3))
print(df.info())
print(df.describe())
print(df.describe(include ='all'))
"""
# read excel  file  : 

"""df =pd.read_excel("pandas/Sales_Filter_Slicer.xlsx")
print(df)
print(df.head(3))
print(df.tail(3))
print(df.info())
"""

# tsv : tab separated values file 

df =pd.read_csv("pandas/students.tsv",sep ="\t")
print(df)