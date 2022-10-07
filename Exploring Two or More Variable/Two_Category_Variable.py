import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Contingency_table_of_loan_grade.csv")
print(df)

#Describe the data
print(df.describe())

#Data info
print(df.info())

#Data types
print(df.dtypes)

#Code 1: Contingency Table showing correlation between Grades and loan status.
#   pandas.crosstab(index, columns, values=None, rownames=None, colnames=None, aggfunc=None, margins=False, margins_name='All', dropna=True, normalize=False)
# index: values to group by in the rows
# columns: values to group by in the columns
# margins: add row/column margins (subtotals). - default: False
# margins_name: name of the row/column that will contain the totals when margins is True - default: All
data_crosstab = pd.crosstab(df['grade'], df['loan_status'], margins = False)
print(data_crosstab)

#Code 2: Contingency Table showing correlation between Purpose and loan status.
data_crosstab = pd.crosstab(df["purpose"], df["loan_status"])
print(data_crosstab)

#Code 3: Contingency Table showing correlation between Grades+Purpose and loan status.
data_crosstab = pd.crosstab([df["purpose"], df["grade"]], df["loan_status"], margins = True, margins_name= "Total")
print(data_crosstab)