# Link for YouTube: https://www.youtube.com/watch?v=skGwKh1dAdk
# from io import StringIO

import pandas as pd
from sentiment import analyse_comments

# making data frame from csv file
data = pd.read_excel(r"C:\Users\eyob\PycharmProjects\bunsen_reviews.xlsx")

# retrieving rows by iloc method
rows = data.iloc[0:170, 1]

# checking data type of rows
print(type(rows))

# display
print(rows)

analyse_comments(rows)
print("")













