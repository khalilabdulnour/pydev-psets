"""
46. How to set the number of rows and columns displayed in the output?
"""
"""
Difficulty Level: L2
"""
"""
Change the pamdas display settings on printing the dataframe df it shows a maximum of 10 rows and 10 columns.
"""
"""
Input
"""
"""
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
"""

# Input
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

# Solution
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)
# df

# Show all available options
# pd.describe_option()