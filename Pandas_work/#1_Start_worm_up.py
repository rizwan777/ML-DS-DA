import pandas as pd

# in  this file we work for pandas some basics functions
# 1. load different types of files {csv,excel,text,etc}
# 2. Basics Operation with Data
# 3. Create file of your operations
# 4. Add/Delete Columns { Fields }

# ------------------- 1 . load different types of files -------------#
# lets load first CSV file in the data frame
data_frame = pd.read_csv('pokemon_data.csv')
# lets load excel data
# data_frame = pd.read_excel('pokemon_data.xlsx')
# lets load text file data
# data_frame = pd.read_csv('pokemon_data.txt', delimiter="\t")
# print data
# print(data_frame)

# note : {{
#           1. csv => {{ pd.read_csv }} , didn't need any dependency package to install
#           2. excel => {{ pd.read_excel}}, file may need to install {xlrd} packages
#           3. text => {{pd.read_csv }}, this files separated with the tabs { \t } so give delimiter value as {"\t"}
# }}

# ------------------ 2. Basics Operation with Data ---------------------
# data_frame= data_frame.columns     # this load all the titles of the columns
# data_frame = data_frame.head(5)  # this load first 5 rows
# data_frame = data_frame.tail(5)  # this load last 5 rows
# data_frame = data_frame["Name"].head(5)  # this load first 5 rows with only name
# data_frame = data_frame["Name"].tail(5)  # this load last 5 rows with only name
# data_frame = data_frame[["Name","Type 1","Type 2"]]  # this load multiple columns
# data_frame = data_frame.iloc[3]  # this load specified row
# data_frame = data_frame.iloc[1:4]  # this load multiple row ,here index {2 ,4}
# data_frame = data_frame.iloc[1:4, 1]  # this load multiple row ,here index {2 ,4} and 1st column values
# data_frame= data_frame.iloc[10,1] # this grab exact value of the position here 10th row 1st column

# if you want to print for each row == {{ print row  by row }}

# for index, row in data_frame.iterrows():
#     print(index,row)                # this print row by row

    # print(index,row["Name"])      # this print row by row only { Name} field
    # print(index,row[2:4])         # this print row by row with multiple columns based on index value
# ------------------------- 3. Create file of your operations----------------------
# data_frame = data_frame[["Name","Type 1","HP"]].head(10)  # this grab first 10 rows with three defined columns
# data_frame.to_csv("TenRows.csv")   # this create text file and store above 10 rows
# data_frame.to_csv("TenRows.txt", sep="\t")   # this create text file and store above 10 rows
# data_frame.to_excel("TenRows.xlsx")   # this create excel file and store above 10 rows

# --------------------------- 4. Add/Delete Columns { Fields }-------------------------
# lets add {Total} column which consist data of HP, Attack, Defense, Speed
# print(data_frame.columns)
# you first check the data frames Titles then try it
# {Total} columns added to the database
# data_frame["Total"] = data_frame["HP"] +data_frame["Attack"]+data_frame["Defense"] +data_frame["Speed"]

# Another way to add column in to the data frame using column index number
#note :
# {{
#       in the iloc function => iloc[rows,colums].method(axis={0,1})
#       in rows = you need to give index values from where to where how many rows you want?
#       in columns = you need to give index values from where to where how many columns you want?
#       in method = sum , subtract , multiplication or division
#       in axis = Add field vertically= 0 or horizontally =1
# }}
# print(data_frame.columns)  # display all heads so we can counts the index no. from where to where?

# print(data_frame.iloc[:,4:10])  # here we give selected all rows and columns index selected from 4 to 9

# data_frame["Total"] = data_frame.iloc[:,4:9].sum(axis=0)

# data_frame.drop(columns=["Total"])

# Delete column from the Data Frame
# data_frame.drop(columns=["Total"])

print(data_frame)

