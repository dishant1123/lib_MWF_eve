import  pandas as pd
import numpy as np

df =pd.DataFrame({
    "id" :[1,2,3,4,5,6,7],
    'name' : ["ram","sita","ravan","bhudev","sahdev","minaxi","yug"],
    "age" :[56,25,44,41,47,23,27],
    "salary":[10000,20000,np.nan,8580,np.nan,96000,np.nan]
})
print(df)

#isna : missing  true  ----> non missing value false
result =df.isna()
print(result)

# total col wise missing value :
total_missing_count = df.isna().sum()
print(total_missing_count)

# drop : remove the  col
# df = df.drop("age",axis=1)
# df = df.drop(1,axis=0)  #  1 is index so its remove the  rowwise
# print(df)


# dropna :
# df =df.dropna()  # remove all row  which contain missing values
# df =df.dropna(axis=1)  #remove the  whole col which contain the missing value
# df =df.dropna(axis=0)  # remove the  whole row which contain the missing value
# df =df.dropna(thresh=2)
# print(df)


print(df)

# fillna :

# df['salary'] = df['salary'].fillna(10000)
# df

df['salary'] = df['salary'].fillna(df['salary'].mean())
df

