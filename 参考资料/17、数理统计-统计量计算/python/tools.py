# -*- coding: utf-8 -*-
"""
    @author: 数模加油站
    @time  : 2025/8/1 11:30
    @file  : chebyshev.py
"""

import math


def bound_deviation(var, deviation):
    """
    切比雪夫不等式：计算 P(|X - μ| ≥ deviation) 的上界

    参数
    ------
    var : float
        随机变量的方差，必须非负
    deviation : float
        偏差大小 |X - μ|，也即是公式中的ε，必须大于 0

    返回
    ------
    float
        上界值，= min(1, var / deviation^2)
    """
    if var < 0:
        raise ValueError("方差 var 必须非负")
    if deviation <= 0:
        raise ValueError("deviation 必须大于 0")
    return min(1.0, var / (deviation ** 2))


def bound_k(k):
    """
    切比雪夫不等式：计算 P(|X - μ| ≥ k·σ) 的上界

    参数
    ------
    k : float
        标准差倍数，必须大于 0

    返回
    ------
    float
        上界值，= min(1, 1 / k^2)
    """
    if k <= 0:
        raise ValueError("k 必须大于 0")
    return min(1.0, 1.0 / (k ** 2))


def cov(x, y, sample=True):
    """
    计算协方差 Cov(X, Y)

    参数
    ------
    x : list of float
        自变量序列 X
    y : list of float
        因变量序列 Y，长度需与 x 相同
    sample : bool
        是否使用样本协方差（除以 N-1），默认 True；若 False，则除以 N 计算总体协方差

    返回
    ------
    float
        Cov(X, Y)
    """
    n = len(x)
    if n != len(y):
        raise ValueError("x, y 长度必须相同")
    if sample and n < 2:
        raise ValueError("样本协方差要求 n >= 2")
    # 计算均值
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    # 计算 ∑(xi - mean_x)*(yi - mean_y)
    total = 0.0
    for xi, yi in zip(x, y):
        total += (xi - mean_x) * (yi - mean_y)
    # 样本用 n-1，总体用 n
    return total / (n - 1 if sample else n)


def corr(x, y, sample=True):
    """
    计算皮尔逊相关系数 ρ(X, Y)

    参数
    ------
    x : list of float
        自变量序列 X
    y : list of float
        因变量序列 Y，长度需与 x 相同
    sample : bool
        是否使用样本相关系数（对应样本协方差），默认 True

    返回
    ------
    float
        Pearson 相关系数，范围 [-1, 1]
    """
    # 协方差
    cova = cov(x, y, sample=sample)
    # 计算标准差
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    var_x = sum((xi - mean_x) ** 2 for xi in x) / (n - 1 if sample else n)
    var_y = sum((yi - mean_y) ** 2 for yi in y) / (n - 1 if sample else n)
    std_x = math.sqrt(var_x)
    std_y = math.sqrt(var_y)
    if std_x == 0 or std_y == 0:
        raise ValueError("标准差为零，无法计算相关系数")
    return cova / (std_x * std_y)


# ========== 使用示例 ==========
# 方差为 4 时，偏差 3 以上的概率上界
print("P(|X-μ|>=3) <=", bound_deviation(4, 3))
# k=2 时，2σ 以上的概率上界
print("P(|X-μ|>=2σ) <=", bound_k(2))

x1 = [2.1, 2.5, 3.6, 4.0]
y1 = [8.0, 10.1, 12.5, 14.2]
print("样本协方差 =", cov(x1, y1))
print("总体协方差 =", cov(x1, y1, sample=False))
print("样本相关系数 =", corr(x1, y1))
print("总体相关系数 =", corr(x1, y1, sample=False))
