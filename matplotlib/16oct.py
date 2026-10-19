import pandas as pd
import matplotlib.pyplot as plt

"""
Theme	    Purpose
default	     : Standard Matplotlib appearance
ggplot	     : Grid-based analytical charts
bmh	         : Clean, readable plots
fivethirtyeight: 	News-style statistical charts
dark_background : 	Dark-background charts
grayscale	 : Black-and-white charts

"""
"""
df =pd.read_csv("matplotlib/corporate_sales.csv")

plt.style.use("ggplot")
plt.figure(figsize=(12, 6))
plt.plot(df['Month'],
         df['Sales'],
         color='blue',
         marker='o',
         linewidth=2.5,
         label='Actual Sales',
         alpha=0.5
        )
plt.plot(df['Month'],
         df['Target'],
         color='orange',
         linestyle='--',
         linewidth=2,
         label='Sales Target',
         alpha=0.5,
         marker='s'
         )
plt.title('Monthly Sales Performance-2026',
          fontsize=17,
          fontweight='bold')
plt.xlabel("Month",fontsize=12)
plt.ylabel("Sales Revenue (Rs.₹)",fontsize=12)
plt.legend(loc='upper left',fontsize=10)
plt.grid(True,linestyle=':',alpha=0.5)
plt.tight_layout()
plt.savefig("sales.png",dpi=300)
plt.show()
"""
# annotation : 

df =pd.read_csv("matplotlib/corporate_sales.csv")
print(df)
max_index = df['Sales'].idxmax()
higest_month = df.loc[max_index,'Month']
higest_sales = df.loc[max_index,'Sales']

print("max_index : ",max_index)
print("higest_month : ",higest_month)
print("higest_sales : ",higest_sales)


plt.style.use("ggplot")
plt.figure(figsize=(12, 6))
plt.plot(df['Month'],
         df['Sales'],
         color='blue',
         marker='o',
         linewidth=2.5,
         label='Actual Sales',
         alpha=0.5
        )
plt.plot(df['Month'],
         df['Target'],
         color='orange',
         linestyle='--',
         linewidth=2,
         label='Sales Target',
         alpha=0.7,
         marker='s'
         )
plt.scatter(higest_month,
            higest_sales,
            color='red',
            s=180,
            zorder=5,
            label='Highest Sales',
            alpha=0.7
)
plt.annotate(f'Highest Sales\n{higest_month}: Rs. {higest_sales:,}',
             xy=(higest_month,higest_sales),
             xytext = (-100,-65),
             textcoords='offset points',
             arrowprops=dict(arrowstyle='->',
                             color='red',
                             linewidth=2
                             
             )
)
plt.title('Monthly Sales Performance-2026',
          fontsize=17,
          fontweight='bold')
plt.xlabel("Month",fontsize=12)
plt.ylabel("Sales Revenue (Rs.₹)",fontsize=12)
plt.legend(loc='upper left',fontsize=10)
plt.grid(True,linestyle=':',alpha=0.5)
plt.tight_layout()
plt.savefig("sales_annotation.png",dpi=500)
plt.show()
