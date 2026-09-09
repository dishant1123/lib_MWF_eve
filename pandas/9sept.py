import  pandas as pd 


"""df =pd.read_csv("pandas/mckinsey.csv")
print(df)
"""
# task :2 in  mckinsey.csv dataset add new column col_name = next_year +3 display like  this  : 

"""df['next_year'] = df['year']+3 
print(df.head(10))
"""

# task  :3 country ==Egypt  , life_exp >50 . 
# task :4 print only those  country  which gdp_cap is  more than 800 

# df.query() : 

"""
egypt = df.query("country =='Egypt' and life_exp >50")[['country','gdp_cap']]
print(egypt)

gdp = df.query("gdp_cap >800")[['country','gdp_cap']]
print(gdp)
"""

# sort_values() : sort 

df =pd.DataFrame({
    'id' : [10,20,30,40,50,60],
    'name':['a','b','c','d','e','f'],
    'age' :[21,23,20,19,29,30],
    'salary':[10000,20000,15000,10000,50000,55000]
    
})

# print(df)

# salary  sort : 
"""df.sort_values(by="salary",inplace=True)  # inplace=True  to sort in place
df = df.sort_values(by="age",ascending=False)  # desc to asc 
print(df)
"""

# sort_index() : 
"""df.index=[1,3,5,2,4,6]
print("original : \n",df)

index_wise_sort = df.sort_index(ascending=False)
index_wise_sort = df.sort_index()
print("index_wise_sort : \n",index_wise_sort)
"""

# reset_index() :

"""salary_wise_sort = df.sort_values(by="salary",ascending=False)
print("salary_wise_sort : \n",salary_wise_sort)

result = salary_wise_sort.reset_index(drop=True)
print("reset index : \n",result)
"""

# hw  : 
"""
1. head , tail  
2. info ,describe 
3. iloc ,loc 
4. query 
5. sort_values , sort_index, reset_index
"""

