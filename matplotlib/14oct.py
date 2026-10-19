
import pandas as pd
import matplotlib.pyplot as plt
"""
Example 1: Stacked bar chart : bar chart 
Purpose: Compare sales from Electronics, Clothing, and Furniture for every month.

Example 2: Area chart : stackchart 
Purpose: Show how sales for each product category change throughout the year.

Example 3: Error bars
Purpose: Display monthly total sales with an illustrative uncertainty range of 5%.
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("matplotlib/monthly_sales.csv")

"""plt.bar(df['Month'],df['Electronics'],label="Electronics")
plt.bar(df['Month'],df['Clothing'],
        bottom=df['Electronics'],
        label="Clothing")
plt.bar(df['Month'],df['Furniture'],
        bottom=df['Electronics']+df['Clothing'],
        label="Furniture")

plt.xlabel("Months")
plt.ylabel("Sales (₹ thousands)")
plt.title("Monthly Sales")
plt.legend(loc="upper left")
plt.grid(True)
plt.tight_layout() 
plt.show()
"""

# stacked bar chart :
"""
plt.figure(figsize=(10,10))

plt.stackplot(df['Month'],
              df[['Electronics','Clothing','Furniture']].values.T,
                  labels=["Electronics","Clothing","Furniture"])

plt.xlabel("Months")
plt.ylabel("Sales (₹ thousands)")
plt.title("Monthly Sales")
plt.legend(loc="upper left")
plt.grid(True)
plt.tight_layout() 
plt.show()

"""

# error bars :

df['Total_Sales'] = df[['Electronics','Clothing','Furniture']].sum(axis=1)

error = df['Total_Sales'] * 0.05  # 1300 

plt.figure(figsize=(10,10))

plt.errorbar(df['Month'],df['Total_Sales'],
             yerr=error,
             fmt='o',
             color='red',
             capsize=10,
             label="Actual Sales")

plt.xlabel("Months")
plt.ylabel("Sales (₹ thousands)")
plt.title("Monthly Sales")
plt.legend(loc="upper left")
plt.grid(True)
plt.tight_layout()
plt.show()