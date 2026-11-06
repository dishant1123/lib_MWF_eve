import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
"""
 ----> using relational regression  sales.csv 
1. scatter plot :sales vs  profit 
2. lineplot : month vs sales  ----> identify the  trend of sales over the months
3. relplot : sales v s profit 

4. reg plot : relartionship  ---->discount vs  sales
5  lmplot() : dis vs sales ----> diff category 

styling  : 

    1.set_theme() : darkgrid, whitegrid, dark, white, ticks
    2.set_style() : darkgrid, whitegrid, dark, white, ticks
    3.set_palette() : deep, muted, bright, pastel, dark, colorblind
    4.set_context() : paper, notebook, talk, poster

"""
# scatter plot :sales vs  profit

df =pd.read_csv("seaborn/seaborn_relational_regression_sales.csv")

"""sns.scatterplot(
    data=df,
    x="Sales",
    y="Profit",
    hue="Category",
    sizes=20
    
)
plt.title("Scatter plot : sales vs profit")
plt.show()
"""
# line  plot  : sale vs  month 
"""
sns.lineplot(
    data=df,
    x="Month",
    y="Sales",
    style="Category",
    markers=True,
    errorbar=None
    
    
)
plt.title("Line plot : month vs sales")
plt.show()
"""

# relplot : sales vs profit

"""sns.relplot(
    data=df,
    x="Sales",
    y="Profit",
    kind="line",
    errorbar=None
    
    
)
plt.title("Relplot : sales vs profit")
plt.show()
"""

# reg plot : relartionship  ---->discount vs  sales

"""sns.regplot(
    data=df,
    x="Discount",
    y="Sales",
    marker="o",
    color="green"
    
)
plt.title("Regplot : discount vs sales")
plt.show()
"""

# styling  :
# sns.set_theme(style="dark",  
#               font="sans-serif", 
#                   font_scale=1, 
#                   color_codes=True)

sns.set_context("poster")
sns.lineplot(
    data=df,
    x="Month",
    y="Sales",
    style="Category",
    markers=True,
    errorbar=None
    
)
plt.title("Line plot : month vs sales")
plt.show()


# bar plot : sales  
# sns.set_style("darkgrid")
# sns.set_palette("pastel")
 
"""sns.set_context("notebook")
sns.barplot(
    data=df,
    x="Category",
    y="Sales",
    errorbar=None
    
)
plt.title("Bar plot : sales")
plt.show()"""