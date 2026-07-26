import pandas as pd

mileTokm = 1.60934

def print_sheet_names(filename):
    """
    打印Excel文件中的所有工作表名称
    
    filename: Excel文件名
    """
    xls = pd.ExcelFile(filename, engine='openpyxl')
    print("所有Sheet名称：", xls.sheet_names)

def read_excel(filename, sheet_name, header=0, usecols='A:D'):
    """
    读取Excel文件并返回DataFrame对象
    
    filename: Excel文件名
    sheet_name: 工作表名称
    header: 数据的标题行索引
    usecols: 需要读取的列范围
    
    返回:
    DataFrame对象
    """
    df = pd.read_excel(
        filename, 
        sheet_name=sheet_name,
        engine='openpyxl',
        header=header,
        usecols=usecols
    )
    # 删除所有值为NaN的行
    df = df.dropna(how='all')
    return df

def print_df_info(df, df_name):
    print(f"\nDataFrame: {df_name}")
    print(f"总行数：{len(df)}")
    print(f"总列数：{len(df.columns)}")
    print(f"\n所有数据：")
    print(df)
    print(f"数据类型：{typename(df)}")

def typename(tp):
    return type(tp).__name__


def 计算排放率(里程排放量, 汽车瞬时速度):
    """
    里程排放量: g/mile
    汽车瞬时速度: mile/h
    排放率: g/s
    """
    return 里程排放量 * 汽车瞬时速度 / 3600


def 计算CO里程排放量(CO百分含量):
    '''
    返回:
    CO里程排放量: g/mile
    '''
    return 11.1 * CO百分含量 + 21.3


def 计算HC里程排放量(HC百分含量):
    '''
    返回:
    HC里程排放量: g/mile
    '''
    return 63.3 * HC百分含量 + 1.7

def ft_to_mile(ft):
    return ft / 5280
