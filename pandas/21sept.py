"""
duplicates :
outlier   :
    1.  IQR method  ----> inter quartile range
    2.  z score method  ----> z score
    
apply :
    1. apply 
    2. map
    3. lambda 
string  function  : lower ,upper, split ,
"""
# outlier : 

import  pandas as pd
import numpy as np
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
    ]
}

df = pd.DataFrame(data)
print(df)

# outlier  IQR method  ----> inter quartile range 

Q1 = np.quantile(df['Price'],0.25) 
Q3 = np.quantile(df['Price'],0.75)

print("Q1: ",Q1)
print("Q3: ",Q3)
IQR = Q3 -Q1 

print("IQR: ",IQR)

lower_limit = Q1 - 1.5 * IQR   #  2500 - 1.5 12500  =====> -16250
upper_limit = Q3 + 1.5 * IQR   #  15000 + 1.5 12500  =====>33750

print("lower_limit: ",lower_limit)  # -16250 
print("upper_limit: ",upper_limit)  # 33750

result = df[(df['Price'] < lower_limit) | (df['Price'] > upper_limit)]
print(result)

# box plot  : 
"""
import matplotlib.pyplot as plt
box_plot =df.boxplot(column='Price')
plt.show()
"""

#z_score method :
"""from scipy.stats import zscore

df['Z_score'] =zscore(df['Price'])
print(df)

outlier = df[df['Z_score'] > 1.5]
print(outlier)
"""

# duplicate : 

"""
result  =df.duplicated(subset=['Price'])
print(result)
"""
# drop_duplicates :

"""
df = df.drop_duplicates(subset=['Price'])
print(df)

result =df.duplicated(subset=['Price']).sum()
print(result)
"""

# new col  :  revenue = price * qty

df['revenue'] = df['Price'] * df['Qty']
print(df)

# discount  : 

"""def discount_revenue(revenue):
    if revenue > 50000 :
        return revenue * 0.1
    else :
        return revenue * 0.05
    
df['discount'] =df['revenue'].apply(discount_revenue)
print(df)
"""
# lambda function  : lambda  arg : expression 
# lambda x : ()  if    else  

"""
df['discount']= df['revenue'].apply(lambda x :x * 0.1  if x >50000 else x * 0.05)
print(df)
"""

# map  : 
product_name = {
    "Laptop":"lap",
    "Mouse":"mous",
    "Keyboard":"key",
    "Monitor":"mon",
    "Headphone":"head"
}

df['product_name'] =df['Product'].map(product_name)
print(df)