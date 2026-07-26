import pandas as pd

from utils import *

C_1 = 'first/C_1.xlsm'

print_sheet_names(C_1)

df = read_excel(
    C_1, 
    sheet_name='Sheet1',
    header=2,
    usecols='A:D'
)

print_df_info(df, "df")
