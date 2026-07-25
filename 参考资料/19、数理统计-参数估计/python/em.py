# -*- coding: utf-8 -*-
"""
    @author: 数模加油站
    @time  : 2025/8/2 10:10
    @file  : em.py
"""

import math
import random


def norm_pdf(x, mu, sigma2):
    """一维正态分布的密度"""
    return (1.0 / math.sqrt(2 * math.pi * sigma2)) * math.exp(-(x - mu) ** 2 / (2 * sigma2))


def em_gmm_1d(xs, K=2, max_iter=100, tol=1e-4):
    """
    一维高斯混合模型（GMM）EM算法（2分量为例，可扩展）
    xs: 观测样本
    K: 分量个数（默认2）
    返回：每个分量的(pi, mu, sigma2)
    """
    n = len(xs)
    # --- 初始化参数 ---
    pis = [1.0 / K] * K
    mus = random.sample(xs, K)
    sigma2s = [1.0 for _ in range(K)]

    for it in range(max_iter):
        # ----- E 步 -----
        gammas = [[0.0] * K for _ in range(n)]  # gammas[i][k] = r_ik
        for i, x in enumerate(xs):
            probs = [pis[k] * norm_pdf(x, mus[k], sigma2s[k]) for k in range(K)]
            s = sum(probs)
            if s == 0:
                probs = [1.0 / K] * K  # 均分
                s = 1.0
            for k in range(K):
                gammas[i][k] = probs[k] / s
        # ----- M 步 -----
        Nk = [sum(gammas[i][k] for i in range(n)) for k in range(K)]
        for k in range(K):
            pis[k] = Nk[k] / n
            mus[k] = sum(gammas[i][k] * xs[i] for i in range(n)) / Nk[k]
            sigma2s[k] = sum(gammas[i][k] * (xs[i] - mus[k]) ** 2 for i in range(n)) / Nk[k]
        # --- 收敛判据 ---
        ll = sum(math.log(sum(pis[k] * norm_pdf(x, mus[k], sigma2s[k]) for k in range(K))) for x in xs)
        if it > 0 and abs(ll - last_ll) < tol:
            break
        last_ll = ll
    return pis, mus, sigma2s


# ========== 使用示例 ==========
# 构造测试数据（两个正态分布混合）
random.seed(42)
xs = [random.gauss(0, 1) for _ in range(50)] + [random.gauss(5, 1) for _ in range(50)]
pis, mus, sigma2s = em_gmm_1d(xs, K=2, max_iter=100, tol=1e-4)
print("混合系数:", pis)
print("均值:", mus)
print("方差:", sigma2s)
