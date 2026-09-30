# group  by  : 
"""
ex : 

id    name   department     salary  

1     Rahul  Sales          30000  
2     Priya  IT             45000  
3     Amit   HR             35000  
4     Neha   IT             40000  
5     Karan  IT             50000

print total salary  of  IT department  : ----> employees 
select sum(salary) ,department 
from employees
group by department 

sales : 30000 
IT    : 135000
HR    : 35000

"""

import pandas as pd

"""
df =pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'name': ['Rahul', 'Priya', 'Amit', 'Neha', 'Karan'],
    'department': ['Sales', 'IT', 'HR', 'IT', 'IT'],
    'salary': [30000, 45000, 35000, 40000, 50000]
})
"""
# print total salary  of  department wise  

"""
department_wise_salary  = df.groupby('department')['salary'].sum()
print(department_wise_salary)
"""
# department  wise  salary  min  salary or  max  salary  :
"""
department_wise_salary_min_max_avg_salary  = df.groupby('department')['salary'].agg(['min','max','mean'])
print(department_wise_salary_min_max_avg_salary)
"""

import pandas as pd

customers = pd.DataFrame({
    "Customer_ID": [101, 102, 103, 104, 105, 106],
    "Customer_Name": ["Rahul", "Priya", "Amit", "Neha", "Karan", "Sneha"],
    "City": ["Ahmedabad", "Mumbai", "Delhi", "Pune", "Ahmedabad", "Mumbai"],
    "Age": [25, 32, 28, 35, 24, 30]
})

# print("customers  : \n",customers)


orders = pd.DataFrame({
    "Order_ID": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009],
    "Customer_ID": [101, 102, 101, 103, 104, 105, 102, 106, 101],
    "Product": [
        "Laptop",
        "Mobile",
        "Headphones",
        "Laptop",
        "Tablet",
        "Mobile",
        "Laptop",
        "Headphones",
        "Mouse"
    ],
    "Quantity": [1, 2, 1, 1, 2, 1, 1, 3, 2],
    "Amount": [55000, 30000, 2000, 60000, 40000, 25000, 58000, 6000, 1500]
})

# print("orders  : \n",orders)

# join  : inner  
customer_orders = pd.merge(
    customers,
    orders,
    on = "Customer_ID",
    how = "inner"
    
)
# print("customer_orders  : \n",customer_orders)

"""
customer_orders  : 
    Customer_ID Customer_Name       City  Age  Order_ID     Product  Quantity  Amount total_sales
0          101         Rahul  Ahmedabad   25      1001      Laptop         1   55000    55000
1          101         Rahul  Ahmedabad   25      1003  Headphones         1    2000    2000
2          101         Rahul  Ahmedabad   25      1009       Mouse         2    1500    3000
3          102         Priya     Mumbai   32      1002      Mobile         2   30000    60000
4          102         Priya     Mumbai   32      1007      Laptop         1   58000    58000
5          103          Amit      Delhi   28      1004      Laptop         1   60000    60000
6          104          Neha       Pune   35      1005      Tablet         2   40000    80000
7          105         Karan  Ahmedabad   24      1006      Mobile         1   25000    25000
8          106         Sneha     Mumbai   30      1008  Headphones         3    6000    18000

1. add col  total  sales  : qty *amt 
2. city  wise  total  sales 
3. product  wise  total  sales
4. customer  wise  total  sales
5. top  3 customers  with  highest  total  sales
6. bottom  3 customers  with  lowest  total  sales
"""
# 1. 
customer_orders['total_sales'] = customer_orders['Quantity'] * customer_orders['Amount']
# print("customer_orders  : \n",customer_orders)

#2 . city wise  total sales : 
"""
city_wise =customer_orders.groupby('City')['total_sales'].sum()
print("city_wise  : \n",city_wise)
"""

# 3. product wise  total sales :
"""product_wise =customer_orders.groupby('Product')['total_sales'].sum()
print("product_wise  : \n",product_wise)
"""

# 4 . customer wise  total sales :
"""customer_wise =customer_orders.groupby('Customer_Name')['total_sales'].sum()
print("customer_wise  : \n",customer_wise)
"""

# 5. top  3 customers  with  highest  total  sales

"""
tops_3_customer  = customer_orders.groupby('Customer_Name')['total_sales'].sum().sort_values(ascending=False).head(3)
bottom_3_customer  = customer_orders.groupby('Customer_Name')['total_sales'].sum().sort_values(ascending=False).tail(3)

print("tops_3_customer  : \n",tops_3_customer)
print("bottom_3_customer  : \n",bottom_3_customer)
"""

# pivort : 