import pandas as pd

# in  this file we work for pandas some basics functions
# 1. Conditional Data Filtering & Sorting
# 2. Advance Filtering Using Regex
# 3. Aggregation Statics Function

# -------------------  load different types of files -------------#
# lets load first CSV file in the data frame
data_frame = pd.read_csv('pokemon_data.csv')
# -------------------- 1. Conditional Data Filtering & Sorting ----------------------

# filter on Name column
# note :{{
#           in pandas data filter Signs are {{ And {&} , or {|}, not {~} }}  used while filtering.
# }}
# data_frame=data_frame.loc[data_frame["Name"]=="Charizard"]
# this fetch all the rows while two condition join with and
# data_frame=data_frame.loc[(data_frame["Type 1"]=="Grass") & (data_frame["Speed"] > 100)]


# normal sorting

# data_frame = data_frame.sort_values("Name")  # this is default Ascending
# data_frame = data_frame.sort_values("Name", ascending=False)  # this is default Descending


# Filter + Sorting

# this fetch all the rows while two condition join with and sorting On {Name} field Ascending order
# data_frame=data_frame.loc[(data_frame["Type 1"]=="Grass") & (data_frame["Speed"] > 100)].sort_values(["Name"])
# this fetch all the rows while two condition join with and sorting On {speed} field Descending order
# data_frame=data_frame.loc[(data_frame["Type 1"]=="Grass") & (data_frame["Speed"] > 100)].sort_values(["Speed"], ascending=False)
# In this case sorting done on two column { Type 1 = asc} and { Hp = desc} order  1 = asc and 0= desc
# data_frame= data_frame.sort_values(['Type 1', 'HP'], ascending=[1,0]).head(100)

# ------------------------- 2.Advance Filtering  using Regular Expression {Regex} ---------------------

import re  # here we added regular expression {regex} package
# here we filter {NAME} string consist "Size" by regex
# data_frame = data_frame.loc[data_frame["Name"].str.contains("Nidoran", regex = True)]

# data_frame = data_frame.loc[data_frame["Name"].str.contains("size", regex = True)]  # case sensitive

# data_frame = data_frame.loc[data_frame["Name"].str.contains("size ", regex = True, flags = re.I)]
# regex = True   // its enable the regex
# flags = re.I   // if you add {re.I} its ignore the case sensitive , this is optional field but important

# --------------------- 3. Aggregation Statics Function -----------------
# this func describe all the detailed Statistic calculation
# print(data_frame.describe())
# this group all fields by "Attack" column and then calculate the mean
# data_frame=data_frame.groupby(["Attack"]).mean()
# this group all fields by "Attack" column and then calculate the mean and then after sort desc on "HP" field
# data_frame=data_frame.groupby(["Attack"]).mean().sort_values(["HP"],ascending=False)


print(data_frame)