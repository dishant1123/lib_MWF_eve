# join  : 
"""
type  joins  : 

1. inner : two tables have one  common column then  inner  join possible. 

2. left  : two tables have one  common column then  but  left side  all  row  print  and  right  side only matching rows. 

3. right :two tables have one  common column then  but  right side  all  row  print  and  left  side only matching rows. 

4. outer : all row  print  left right  side if  not  match  then also print .


"""
import pandas as pd

customers = pd.DataFrame({
    'Customer_ID': [101, 102, 103, 104, 105],
    'Customer_Name': ['Rahul', 'Priya', 'Amit', 'Neha', 'Karan'],
    'City': ['Ahmedabad', 'Mumbai', 'Delhi', 'Pune', 'Surat']
})

# print(customers)

orders = pd.DataFrame({
    'Order_ID': [1001, 1002, 1003, 1004, 1005, 1006],
    'Customer_ID': [101, 102, 103, 101, 105, 106],
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Mouse', 'Keyboard', 'Monitor'],
    'Amount': [55000, 25000, 18000, 1200, 2500, 15000]
})

# print(orders) 

# inner  join  : 

"""inner_join= pd.merge(
    customers,
    orders,
    on = 'Customer_ID',
    how = 'inner'
)
print("inner  join  of two dataframe is  : \n",inner_join)
"""

# left join  : 

"""left_join= pd.merge(
    customers,
    orders,
    on = 'Customer_ID',
    how = 'left'
)
print("left  join  of two dataframe is  : \n",left_join)
"""

# right join  : 
"""
right_join= pd.merge(
    customers,
    orders,
    on = 'Customer_ID',
    how = 'right'
)
print("right  join  of two dataframe is  : \n",right_join)
"""
# outer join  :

"""outer_join= pd.merge(
    customers,
    orders,
    on = 'Customer_ID',
    how = 'outer'
)
print("outer  join  of two dataframe is  : \n",outer_join)
"""

# concate  :

"""import pandas as pd

df1 = pd.DataFrame({
    'Employee_ID': [101, 102, 103],
    'Employee_Name': ['Rahul', 'Priya', 'Amit'],
    'Department': ['Sales', 'IT', 'HR'],
    'Salary': [30000, 45000, 35000]
})

print(df1)

df2 = pd.DataFrame({
    'Employee_ID': [104, 105, 106],
    'Employee_Name': ['Neha', 'Karan', 'Riya'],
    'Department': ['Finance', 'IT', 'Sales'],
    'Salary': [40000, 50000, 32000]
})

print(df2)
# col wise  : 
concate_dataframe = pd.concat(
    [df1, df2],
    axis=1
)
# row wise  : 
concate_dataframe = pd.concat(
    [df1, df2],
    axis=0
)
print(concate_dataframe)
"""

# pivot  :

import pandas as pd
"""
df = pd.DataFrame({
    'Month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar', 'Mar','Mar'],
    'City': ['Ahmedabad', 'Mumbai', 'Ahmedabad', 'Mumbai', 'Ahmedabad', 'Mumbai','Ahmedabad'],
    'Product': ['Laptop', 'Laptop', 'Mobile', 'Mobile', 'Laptop', 'Mobile','Laptop'],
    'Sales': [50000, 60000, 30000, 40000, 55000, 45000,90000]
})

print(df)

pivort_summary  = df.pivot_table(
    index = 'Month',
    
    values = 'Sales',
    aggfunc = 'sum'
)
print(pivort_summary)
"""
# using titanic  data  :

"""df = pd.read_csv("pandas/Titanic-Dataset_2.csv")
print(df.head())

total_Survived = df.pivot_table(
    index = 'Sex',
    values = 'Survived',
    aggfunc = 'sum'
)
print("total survived  : \n",total_Survived)
"""


movies = pd.read_csv("pandas/movies.csv")
print(movies.head())

"""
task :1 movies and directors table  drop  unnamed col . 
task :2 join  with  director_id   and  print  the  movies  with  director  name .

"""
