from 第一次模拟.utils import *

print_sheet_names('C_2.xlsm')

df1 = read_excel(
    'C_2.xlsm', 
    sheet_name='Sheet1 (2)',
    header=3,
    usecols='A:C'
)

df2 = read_excel(
    'C_2.xlsm', 
    sheet_name='Sheet1 (2)',
    header=3,
    usecols='D:F'
)

print_df_info(df1, "df1")
print_df_info(df2, "df2")