import pandas as pd

from 第一次模拟.utils import *

print_sheet_names('C_1.xlsm')

df = read_excel(
    'C_1.xlsm', 
    sheet_name='Sheet1',
    header=2,
    usecols='A:D'
)

print_df_info(df, "df")
