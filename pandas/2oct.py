# EDA :
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # pip install matplotlib.pyplot
import seaborn as sns
import ydata_profiling as ydp  # pip install ydata-profiling
 
"""
exploratory data analysis  :

1.univariate  :
    1.  histogram  
    2.  box plot 
    3.  scatter plot
2.bivariate  :
    1. correlation 
    2. insights 
"""

movies = pd.read_csv("pandas/movies.csv")
directors = pd.read_csv("pandas/directors.csv")

movies.drop(columns=['Unnamed: 0'], inplace=True)
directors.drop(columns=['Unnamed: 0'], inplace=True)

# print(movies.head())
# print(directors.head())

movies_directors = pd.merge(
    movies,
    directors,
    right_on = 'id',
    left_on = 'director_id',
    how = 'left'
    
)
print(movies_directors.head())

# top 5 movies with highest revenue :

"""
top_5_movies = movies_directors.sort_values(by ='revenue', ascending=False).head(5)[['title','revenue','director_name']]
print(top_5_movies)
"""
# graph :
"""
plt.figure(figsize=(9,5))
plt.bar(x=top_5_movies['title'], height=top_5_movies['revenue'])
plt.xlabel('Revenue')
plt.ylabel('Movie')
plt.xticks(rotation=90)
plt.yticks(rotation=45)
plt.title('Top 5 Movies with Highest Revenue')
plt.show()
"""

# correlation  :

"""
correlation = movies_directors.corr(numeric_only=True)
"""
# heatmap : 

"""
plt.figure(figsize=(9,5))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
"""

# EDA report using  ydata_profiling  :
"""
result = ydp.ProfileReport(movies_directors, title='EDA report',explorative=True)
result.to_file("pandas/EDA_report.html")

"""

import sweetviz as sv
report =sv.compare(movies,directors)
report.to_file("pandas/EDA_report.html")

