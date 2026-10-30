"""
What is Jointplot?
A Jointplot is used to visualize the relationship between two numerical variables.

It contains three parts:
1. Main plot - Shows the relationship between two variables.
2. Top distribution - Shows the distribution of the X-axis.
3. Right distribution - Shows the distribution of the Y-axis. 


=============== 

heat map :

Correlation Matrix using Pandas, Heatmap with Annotations, Diverging Color Palettes.
What is Correlation?
Correlation measures the strength and direction of the relationship between two numerical variables.

Correlation values range from -1 to +1.
Value	Meaning
+1	    Perfect positive correlation
0	    No linear correlation
-1	    Perfect negative correlation
"""

import  pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""
df =pd.read_csv("seaborn/seaborn_sales_profit_dataset.csv")

sns.jointplot(
    data =df,
    x='Profit',
    y='Revenue',
    kind='kde',
    height=5
)
plt.show()
"""
# heat map  : 

df =pd.read_csv("seaborn/seaborn_sales_profit_dataset.csv")

coorrelation_matrix = df.corr(numeric_only=True)

sns.heatmap( 
            coorrelation_matrix,
            annot=True,
            cmap='coolwarm', 
            fmt='.2f',
            linewidths=0.5, 
        linecolor='white',
        square=True
            
            )
plt.show()