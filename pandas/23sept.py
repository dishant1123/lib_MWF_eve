import  pandas as pd 
from datetime import date
# string  function  : 
"""
1. upper 
2. lower 
3. replace  
4. trim  
5. concate 
"""

data = {
    'Product': [
        'Laptop',
        'Mouse',
        'Keyboard',
        'Monitor',
        'Headphone'
    ],
    
    'Price': [
        55000,
        1200,
        2500,
        15000,
        1200
    ],
    
    'Qty': [
        2,
        5,
        3,
        2,
        4
    ],
    'pur_date':[
      "2021-01-02",
      "2022-02-24",
      "2023-05-12",
      "2024-11-26",
      "2025-12-27"
    ]
    
}

df =pd.DataFrame(data)
# print(df)

# result = df['Product'].str.lower()
# result = df['Product'].str.upper()
# df['Product'] = df['Product'].str.strip()

"""product_name = {
    "Laptop":"lap",
    "Mouse":"mous",
    "Keyboard":"key",
    "Monitor":"mon",
    "Headphone":"head"
}

df['product_name'] =df['Product'].map(product_name)
print(df)


# df['product_name'] =df['product_name'].str.replace("lap","Lap")
# df['product_name'] =df['product_name'].str.title()

df['new_name'] =df['Product']+"-"+df['product_name']
print(df)"""


df['pur_date'] =pd.to_datetime(df['pur_date'])

df['day'] =df['pur_date'].dt.day
df['month'] =df['pur_date'].dt.month
df['year'] =df['pur_date'].dt.year

df['today']=date.today()
df['today']=pd.to_datetime(df['today'])

df['duration'] =(df['today'] - df['pur_date']).dt.days
print(df)

"""
dataframe  :

id   name           joining_date   duration 
1    ram shah       2021-01-02     
2    shyam patel    2022-02-24     
3    ravan waghela  2023-05-12     
4    bhudev shah    2024-11-26     
5    bhuvan baam    2025-12-27

1. split  the first_name and  last_name  . 
2. first letter capital  for each name  
3. calculate the duration -----> today  ----> 23 - 9 -26


"""

