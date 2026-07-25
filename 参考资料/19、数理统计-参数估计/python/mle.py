# -*- coding: utf-8 -*-
"""
    @author: 数模加油站
    @time  : 2025/8/2 09:59
    @file  : mle.py
"""

import math


def mle_generic(xs, param_grid, pmf_or_pdf):
    """
    对任意分布进行参数的极大似然估计（MLE，网格搜索法）

    参数
    ------
    xs : list
        观测样本
    param_grid : list
        需要搜索的参数点（如[0.1,0.2,...,0.9]），单参数为一维列表，多参数为元组列表
    pmf_or_pdf : function
        输入 x, theta，返回概率密度或概率质量（如 f(x, theta)）

    返回
    ------
    最优参数 θ^, 最大似然值 max_loglikelihood
    """
    best_param = None
    max_loglik = -float('inf')
    for theta in param_grid:
        loglik = 0.0
        for x in xs:
            p = pmf_or_pdf(x, theta)
            # 防止 log(0) 出错
            if p <= 0:
                loglik = -float('inf')
                break
            loglik += math.log(p)
        if loglik > max_loglik:
            max_loglik = loglik
            best_param = theta
    return best_param, max_loglik


def empirical_pmf(xs, value):
    """
    经验概率质量函数估计 P(X = value)
    xs: 观测样本（list）
    value: 要估计的值
    """
    n = len(xs)
    count = sum(1 for x in xs if x == value)
    return count / n if n > 0 else 0.0


def empirical_cdf(xs, value):
    """
    经验累积分布函数估计 P(X ≤ value)
    xs: 观测样本（list）
    value: 要估计的分位点
    """
    n = len(xs)
    count = sum(1 for x in xs if x <= value)
    return count / n if n > 0 else 0.0


# ===========================
# 示例：估计一个0-1分布的概率参数p
# ===========================
# 假设观测到伯努利样本
xs = [1, 0, 0, 1, 1, 0, 1, 1]
# 构建参数网格
p_grid = [i / 1000 for i in range(1, 1000)]


# 定义伯努利分布的pmf
def bern_pmf(x, p):
    return p if x == 1 else (1 - p)


# 执行MLE
p_hat, max_ll = mle_generic(xs, p_grid, bern_pmf)
print(f"MLE估计 p = {p_hat:.3f}, 最大对数似然 = {max_ll:.4f}")

print("经验概率 P(X=1):", empirical_pmf(xs, 1))
print("经验CDF P(X<=0):", empirical_cdf(xs, 0))
