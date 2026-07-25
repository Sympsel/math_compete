# -*- coding: utf-8 -*-
"""
    @author: 数模加油站
    @time  : 2025/8/2 11:20
    @file  : chi2.py
"""

import math

def normal_cdf(z):
    """
    计算标准正态分布的左侧累计概率

    Parameters
    ----------
    z : float
        z分数

    Returns
    -------
    float
        P(Z <= z)
    """
    # math.erf是误差函数，与标准正态分布累积概率密切相关
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))

def chi2_test(table, alpha=0.05):
    """
    任意r×c列联表的卡方独立性检验，p值用正态近似。

    Parameters
    ----------
    table : list of list of int/float
        任意r×c观测频数表（二维列表）。
    alpha : float, optional
        显著性水平，默认为0.05。

    Returns
    -------
    chi2 : float
        卡方统计量。
    df : int
        自由度（(行数-1)*(列数-1)）。
    p : float
        p值（右尾概率）。
    reject : bool
        是否拒绝独立性假设。
    """
    rows = len(table)  # 行数
    cols = len(table[0])  # 列数
    # 计算每一行的合计
    row_totals = [sum(row) for row in table]
    # 计算每一列的合计
    col_totals = [sum(table[i][j] for i in range(rows)) for j in range(cols)]
    # 所有元素之和（总样本量）
    total = sum(row_totals)
    # 计算每个单元格的理论频数 E_ij
    expected = [
        [row_totals[i] * col_totals[j] / total for j in range(cols)]
        for i in range(rows)
    ]
    # 计算卡方统计量
    chi2 = 0.0
    for i in range(rows):
        for j in range(cols):
            # 仅在期望频数大于0时计算
            if expected[i][j] > 0:
                # (观测-期望)^2/期望
                chi2 += (table[i][j] - expected[i][j]) ** 2 / expected[i][j]
    # 计算自由度
    df = (rows - 1) * (cols - 1)
    # 正态分布近似计算p值
    if df > 0:
        # Z分数 = (卡方统计量 - 自由度) / sqrt(2*自由度)
        z = (chi2 - df) / math.sqrt(2 * df)
        # p值为右尾概率 = 1 - 左侧累计概率
        p = 1 - normal_cdf(z)
    else:
        # 如果自由度为0，p值直接设为1
        p = 1.0
    # 比较p值与显著性水平，判断是否拒绝独立性假设
    reject = p < alpha
    return chi2, df, p, reject

# ==========================
# 使用示例
# ==========================
# 你的2x2列联表数据
table = [
    [10, 40],
    [30, 20]
]
# 执行卡方独立性检验
chi2, df, p, reject = chi2_test(table, alpha=0.05)
# 输出统计量、自由度、p值和结论
print(f"卡方统计量 = {chi2:.4f}")
print(f"自由度 = {df}")
print(f"p值 = {p}")
print("结论：", "拒绝独立性假设" if reject else "不拒绝独立性假设")
