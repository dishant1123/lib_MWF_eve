"""
1. customer_sales.csv 
2. countplot  : customer count by  gender 
3. barplot : avg sales by gender 
            estimator :summerize numerical values with each category
                       mean sales by product ,
                       total sales by product ---->sum 
4.KDE plot  
5.histplot :A histogram groups numerical values into intervals called bins and shows how many observations fall into each interval.

task : 
1.Create a countplot showing the number of customers in each region.
2.Create a barplot comparing average sales by product.
3.Create a barplot showing total sales by region.
4.Plot a histogram of sales using 5, 10, and 15 bins. Compare the results.
5.Create a KDE plot for sales and explain where values are most concentrated.
6.Combine the histogram and KDE curve, then explain the shape of the distribution.

"""
import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

# countplot :

"""
df = pd.read_csv("seaborn/customer_sales (1).csv")

sns.countplot(
    data=df,
    x="Gender",
    fill=False
    
)
plt.title("Customer Count by Gender")
plt.show()
"""

# barplot : 

df = pd.read_csv("seaborn/customer_sales (1).csv")

sns.barplot(
    data=df,
    x="Gender",
    y="Sales",
    hue="Product",
    errorbar=None,
    estimator='sum'
)
plt.title("Average Sales by Gender")
plt.show()