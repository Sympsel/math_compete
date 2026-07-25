# -*- coding: utf-8 -*-
"""
    @author: 数模加油站
    @time  : 2025/8/2 10:31
    @file  : hypothesis.py
"""

def basic_hypothesis_test(T_obs, T_null_dist, alpha=0.05, alternative='greater'):
    """
   最基础的假设检验（右尾、左尾、双尾）—— 支持任意检验统计量和分布
    支持如下检验方式：
        - 右尾（单尾）检验：H1: T_obs > T_null
        - 左尾（单尾）检验：H1: T_obs < T_null
        - 双尾检验：H1: T_obs 与 H0下均值的偏差绝对值更大

    参数
    ------
    T_obs : float
        实际观测到的检验统计量
    T_null_dist : list of float
        H0（原假设）下，统计量T的模拟分布（通过理论、模拟或置换方法得到）
    alpha : float
        显著性水平（常用0.05）
    alternative : str
        'greater'  —— 右尾检验（大于为极端）
        'less'     —— 左尾检验（小于为极端）
        'two-sided'—— 双尾检验（绝对偏离均值为极端）

    返回
    ------
    p : float
        p值（极端概率）
    reject : bool
        是否拒绝原假设（p < alpha）

    公式说明
    ------
    右尾检验：
        H0: T ≤ T0
        H1: T > T0
        p = P(T ≥ T_obs | H0) ≈ (模拟分布中 ≥ T_obs 的比例)

    左尾检验：
        H0: T ≥ T0
        H1: T < T0
        p = P(T ≤ T_obs | H0) ≈ (模拟分布中 ≤ T_obs 的比例)

    双尾检验：
        H0: T = T0
        H1: T ≠ T0
        p = P(|T - μ0| ≥ |T_obs - μ0| | H0) ≈ (模拟分布中绝对偏差更极端的比例)
        其中 μ0 = E[T | H0]
    """
    n = len(T_null_dist)
    if alternative == 'greater':
        # 右尾检验
        p = sum(1 for t in T_null_dist if t >= T_obs) / n
    elif alternative == 'less':
        # 左尾检验
        p = sum(1 for t in T_null_dist if t <= T_obs) / n
    elif alternative == 'two-sided':
        # 双尾：两侧概率
        T_mean = sum(T_null_dist) / n
        diff = abs(T_obs - T_mean)
        p = sum(1 for t in T_null_dist if abs(t - T_mean) >= diff) / n
    else:
        raise ValueError("alternative 只能取 'greater', 'less', 'two-sided'")
    reject = p < alpha
    return p, reject

# ==========================
# 示例：检验一组样本的均值是否大于/小于、等于72
# ==========================
import random
random.seed(0)
# 原假设：均值为0，检验统计量T为均值
T_obs = 75
# H0下分布：生成10000组N(72,10)样本（理论均值为72）
T_null_dist = [sum(random.gauss(72,10) for _ in range(100)) / 100 for _ in range(10000)]
# 单尾右侧检验
p, reject = basic_hypothesis_test(T_obs, T_null_dist, alpha=0.05, alternative='less')
print(f"观测统计量 T_obs = {T_obs:.3f}")
print(f"p值 = {p}")
print("结论：", "拒绝H0" if reject else "不拒绝H0")

