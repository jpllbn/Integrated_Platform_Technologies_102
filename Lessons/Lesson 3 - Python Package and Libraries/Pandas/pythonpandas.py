# Series Example
import pandas as pd

# data = {}
#
# df = pd.DataFrame(data)
#
# df = pd.read_csv('data.csv')

# data = pd.Series([10,20,30,40], index=['a', 'b', 'c', 'd'])
# print(data)
#
# print(data['b'])


# DataFrame Example
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25,30,35],
#     'Salary': [50000, 60000, 70000]
# }
#
# df = pd.DataFrame(data)
#
# print(df)


# Reading a CSV File using read_csv() function

# there are different ways to read a csv file

# Method 1
# df = pd.read_csv('data.csv')
# print(df)

# Method 2
# print(df.head())

# Method 3
# print(df.info())

# Method 4
# print(df.describe())

# Writing a CSV File using to_read() function
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25,30,35],
#     'Salary': [50000, 60000, 70000]
# }
#
# df = pd.DataFrame(data)
#
# df.to_csv('newdata.csv', index=False)


# Selecting a Filtering Data

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25,30,35],
#     'Salary': [50000, 60000, 70000]
# }
#
# df = pd.DataFrame(data)
#
# # Select a single column
# print('+*' * 5, "Single Column", '+*' * 5)
# print(df['Name'])
#
# print('+*' * 5, "Multiple Columns", '+*' * 5)
# print(df[['Name', 'Age']])
#
# print('+*' * 5, "Select Rows based", '+*' * 5)
# filter = df[df['Age']>30]
# print(filter)
#
# # Using loc
# print('+*' * 5, "Single Column", '+*' * 5)
# print(df.loc[1])
#
# print('+*' * 5, "Single Column", '+*' * 5)
# print(df.iloc[1])


# Displaying data without Primary Keys

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25,30,35],
#     'Salary': [50000, 60000, 70000]
# }
#
# df = pd.DataFrame(data)
#
# print(df.to_string(index=False))

#
# print(f"{df} \n")
# print(f"{df.isnull()} \n")
#
# print('+*' * 5, "dropna() function", '+*' * 5)
# dfCleaned = df.dropna()
# print(f"{dfCleaned} \n")
#
# # Filling in the missing value with aritificial number
# print('+*' * 5, "fillna() function", '+*' * 5)
# dfFilled = df.fillna(0)
# print(f"{dfFilled}")
#
# df['Name'].fillna('No Value', inplace = True)
# df['Age'].fillna('No Value', inplace = True)
# print(df)
#
# print("\n")
# # Fill specific row
# df.loc[0, 'Name'] = 'Alice'
# df.loc[1, 'Age']    = 30
# print(df)

# print("\n")
# df['Bonus'] = [1200,1300,1400,1500,1600,1700,1800]
# df['Salary with Tax'] = df['Salary']*0.9
# print(df)


# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'Eddy'],
#     'Age': [25,30,35, 31],
#     'Salary': [50000, 60000, 70000, 80000]
# }
#
# df = pd.DataFrame(data)
#
# newdata = {
#     'Name': ['David', 'Eva'],
#     'Age': [28, 22],
#     'Salary': [50000, 60000]
# }
#
# newDf = pd.DataFrame(newdata)
#
# newDf.to_csv('newdata.csv', mode='a', header=False, index=False)
# print("New data has been appended to 'newdata.csv'")


data = {}


# df = pd.read_csv('data.csv')
# print(df)
#
# sum = df['Salary'].sum()
# mean = df['Salary'].mean()
# median = df['Salary'].median()
# std = df['Salary'].std()
# var = df['Salary'].var()
#
#
# print(f"Sum: {sum}")
# print(f"Mean: {mean}")
# print(f"Median: {median}")
# print(f"Standard Deviation: {std}")
# print(f"Variance: {var:2F}")
#
#
# # Sorting Data
# print(df.sort_values(by='Salary'))
# print(df.sort_values(by='Age'))


# Merge and Join

df1 = pd.DataFrame({'Key': ['A', 'B', 'C'], 'Value1':[1,2,3]})
df2 = pd.DataFrame({'Key': ['A', 'B', 'D'], 'Value1':[4,5,6]})

# dfMerged = pd.merge(df1, df2, on='Key')

# usage of how='outer' parameter
dfMerged = pd.merge(df1, df2, on='Key', how = 'outer')

print(df1)
print(df2)
print(dfMerged)




