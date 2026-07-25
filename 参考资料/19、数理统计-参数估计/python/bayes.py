# -*- coding: utf-8 -*-
"""
    @author: 数模加油站
    @time  : 2025/8/2 10:16
    @file  : bayes.py
"""

def bayes_estimate(xs, theta_grid, prior_func, likelihood_func):
    """
    通用贝叶斯估计（后验均值，适用于一维参数/有限格点）
    xs: 观测数据
    theta_grid: 参数网格（如[0.01, 0.02, ..., 0.99]）
    prior_func: 先验概率函数（输入theta，返回概率密度）
    likelihood_func: 似然函数（输入xs, theta，返回似然）
    返回：后验分布（dict），后验均值估计
    """
    posterior = {}
    total = 0.0
    for theta in theta_grid:
        prob = prior_func(theta) * likelihood_func(xs, theta)
        posterior[theta] = prob
        total += prob
    # 归一化
    for theta in posterior:
        posterior[theta] /= total
    # 后验均值
    mean = sum(theta * posterior[theta] for theta in posterior)
    return posterior, mean

# ==== 使用例子 ====
xs = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 均匀分布先验（Uniform(0,1)）
def prior(p): return 1.0 if 0 <= p <= 1 else 0.0
# 伯努利似然
def likelihood(xs, p):
    n = len(xs)
    s = sum(xs)
    return (p**s) * ((1-p)**(n-s))
# 参数网格
grid = [i/100 for i in range(1, 100)]
posterior, post_mean = bayes_estimate(xs, grid, prior, likelihood)
print(f"均匀先验下后验均值估计 = {post_mean:.4f}")


