import  pandas as pd
import matplotlib.pyplot as plt


"""
df= pd.read_csv("matplotlib/regional_sales.csv")
print(len(df))

plt.bar(df['Region'],df['Revenue'],color="green",width=0.6)

for i in range(len(df)) : 
    plt.text(i,df['Revenue'][i],
             (df['Revenue'][i]),
            ha="center",
            va="bottom",
            fontsize=12
    )

plt.xlabel("region")
plt.ylabel("revenue")
plt.title("revenue vs region")
plt.show()
"""

# pie chart :
"""
df= pd.read_csv("matplotlib/regional_sales.csv")

plt.pie(df['Revenue'],
        labels=df['Region'],
        autopct='%1.1f%%',
        )
plt.show()
"""
# donut chart :

"""df= pd.read_csv("matplotlib/regional_sales.csv")

plt.pie(df['Revenue'],
        labels=df['Region'],
        autopct='%1.1f%%',
        wedgeprops={'width':0.3},
        )
plt.show()
"""

# histogram :
"""df= pd.read_csv("matplotlib/regional_sales.csv")

plt.hist(df['Revenue'],
         bins=3,
         color="green",
         alpha=0.2)
plt.xlabel("revenue")
plt.ylabel("frequency")
plt.title("revenue vs frequency")
plt.show()
"""

# barh  : 

df =pd.read_csv("matplotlib/regional_sales.csv")

plt.figure(figsize=(10,10))
plt.barh(df['Region'],df['Revenue'],color="green")
for i in range(len(df)) : 
    plt.text(df['Revenue'][i],i,
             (df['Revenue'][i]),
            ha="left",
            fontsize=12
    )

plt.xlabel("revenue")
plt.ylabel("region")
plt.title("revenue vs region")
plt.show()

# task  :1 
"""
1. top 5 movies with highest revenue : ---->bar  chart  ----> label 
2. top 5 directors with  highest  movies produce  (number  of  movies) ----> barh 


"""
