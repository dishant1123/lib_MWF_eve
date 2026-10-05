# plot  : -----> graph 
# pip install matplotlib
# pip install seaborn

"""
2 lib  : 
1. matplotlib  : simple  plot ,graph   ----> line chart , bar chat , histogram 
2. seaborn     : statistical presentation  , vilonplot  , kde plot 

properties/ method : 

1. plt.plot :   line graph 
2. plt.bar :    bar chart 
3. plt.hist : histogram 
4. plt.pie : pie chart
5. plt.boxplot : box plot
6. plt.scatter : scatter plot

plt.xlabel : x label 
plt.ylabel : y label
plt.title : title  
plt.legend : legend
plt.xtricks :  font  resize 
plt.ytricks :  font  resize
plt.grid :  grid line

"""
import matplotlib.pyplot as plt
import pandas as pd
# line graph : 

"""
days =[1,2,3,4,5,6,7,8,9,10]
sales =[100,200,900,400,500,200,1200,1000,1100,900]


plt.plot(days,sales,color="red",marker="x",linestyle="--",linewidth=2,label="sales",markersize=10,markeredgewidth=2)
plt.xlabel("days")
plt.ylabel("sales")
plt.title("sales vs days")
plt.grid(True)
plt.show()
"""

# line  graph  with   using  csv file  : 
"""
df= pd.read_csv("matplotlib/days_sales.csv")

plt.plot(df['Day'],df['Sales'],color="red",marker="x",linestyle="--",linewidth=2)
plt.xlabel("days")
plt.ylabel("sales")
plt.title("sales vs days")
plt.grid(True)
plt.show()
"""

# bar chart  :  

name =['ram','sita','ravan','laxman','bhudev']
marks =[91,90,84,78,67]

plt.bar(name,marks,color="red",width=0.7)
plt.xlabel("name")
plt.ylabel("marks")
plt.title("marks vs name")
plt.xticks(rotation=45)
plt.show()
