# -*- coding: utf-8 -*-
"""
    @author: 数模加油站
    @time  : 2025/8/2 08:59
    @file  : clt.py
"""
import math


def _normal_cdf(z):
    """
    标准正态分布累积分布函数 Φ(z)
    """
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def lindeberg_levy_cdf(x, mu, var, n):
    """
    利用林德伯格–莱维中心极限定理近似计算 P(S_n ≤ x)

    math::
        S_n = X_1 + ... + X_n
        μ = E[X_i], Var = Var[X_i]

    参数
    ------
    x : float
        S_n 的上界
    mu : float
        每个 X_i 的均值
    var : float
        每个 X_i 的方差，必须 ≥ 0
    n : int
        独立同分布随机变量的个数，n ≥ 1

    返回
    ------
    float
        近似的 P(S_n ≤ x) = Φ( (x - n·μ) / sqrt(n·Var) )
    """
    if var < 0:
        raise ValueError("var 必须非负")
    if n < 1:
        raise ValueError("n 必须 ≥ 1")
    sigma_n = math.sqrt(n * var)
    z = (x - n * mu) / sigma_n
    return _normal_cdf(z)


def de_moivre_laplace_cdf(k, n, p):
    """
    利用德莫弗—拉普拉斯中心极限定理近似计算二项分布的累积分布函数

    X ~ Binom(n, p)

    参数
    ------
    k : int
        X 的上界
    n : int
        试验次数
    p : float
        每次成功的概率，0 < p < 1

    返回
    ------
    float
        近似的 P(X ≤ k) ≈ Φ( (k + 0.5 - n·p) / sqrt(n·p·(1-p)) )
        （使用连续性校正 +0.5）
    """
    if not (0 < p < 1):
        raise ValueError("p 必须在 (0, 1) 之间")
    if n < 1:
        raise ValueError("n 必须 ≥ 1")
    mu = n * p
    sigma = math.sqrt(n * p * (1 - p))
    # 连续校正
    z = (k + 0.5 - mu) / sigma
    return _normal_cdf(z)


# 林德伯格-莱维CLT
print("P(S_100 ≤ 220) ≈", lindeberg_levy_cdf(220, mu=2, var=4, n=100))

# 德莫弗—拉普拉斯 CLT：Binom(50, 0.3)
print("P(X ≤ 20) ≈", de_moivre_laplace_cdf(20, n=50, p=0.3))
