import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# scatter plot : 
"""df = pd.read_csv("matplotlib/advertising_spend_sales.csv")

X=df['Advertising_Spend']
Y=df['Sales']

plt.scatter(X,Y,color="red",s=80,label="Actual Sales")

# y = mx +c 
m,c=np.polyfit(X,Y,1)


# y_predict
y_predict=  m * X + c 

# plot  trend line  : 

plt.plot(X,y_predict,color="blue",linewidth=2,label="Trend Line")

plt.xlabel("Advertising Spend (₹ thousands)")
plt.ylabel("Sales (₹ thousands)")
plt.title("Advertising Spend vs Sales")
plt.grid(True)
plt.legend("Actual Sales","Trend Line")
plt.show()

# slope ,intercept : 
print("Slope:",round(m,2))
print("Intercept:",round(c,2))
"""

# sub  plot  : 

"""
df= pd.read_csv("matplotlib/monthly_sales_subplots.csv")

plt.figure(figsize=(10,10))

plt.subplot(2,1,1)
plt.plot(df['Month'],df['Sales'],marker="o",color="red")
plt.title("Monthly Sales")
plt.ylabel("Sales (₹ thousands)")
plt.grid(True)

plt.subplot(2,1,2)
plt.bar(df['Month'],df['Profit'],color="green")
plt.title("Monthly Profit")
plt.xlabel("Months")
plt.ylabel("Profit (₹ thousands)")
plt.grid(True)
plt.show()
"""

# using  axis : 

df= pd.read_csv("matplotlib/monthly_sales_subplots.csv")

fig,ax = plt.subplots(2,2,figsize=(10,10))

ax[0,0].plot(df['Month'],df['Sales'],marker="o",color="red")
ax[0,0].set_title("Monthly Sales")
ax[0,0].set_ylabel("Sales (₹ thousands)")
ax[0,0].grid(True)

ax[0,1].bar(df['Month'],df['Profit'],color="green")
ax[0,1].set_title("Monthly Profit")
ax[0,1].set_xlabel("Months")
ax[0,1].set_ylabel("Profit (₹ thousands)")

ax[1,0].bar(df['Month'],df['Expenses'],color="blue")
ax[1,0].set_title("Monthly Expenses")
ax[1,0].set_xlabel("Months")
ax[1,0].set_ylabel("Profit (₹ thousands)")

ax[1,1].plot(df['Sales'],df['Expenses'],marker="o",color="purple")
ax[1,1].set_title("Monthly sales vs Expenses")
ax[1,1].set_xlabel("Months")
ax[1,1].set_ylabel("Profit (₹ thousands)")

plt.tight_layout()
plt.show()


