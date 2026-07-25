# -*- coding: utf-8 -*-
"""
    @author: 数模加油站
    @time  : 2025/8/1 16:58
    @file  : approx.py
"""
from distribute.Hypergeom import HyperGeom
from distribute.binom import Binom
from distribute.poisson import Poisson


def b2poisson(n, p):
    """
    二项分布的泊松近似
    Parameters
    ----------
    n: int
        二项分布的参数n，即抽样次数
    p: float
        二项分布的参数p，即成功率

    Returns
    -------
    返回对应的泊松分布类
    """
    # lambda = np
    return Poisson(n * p)


def h2binom(N, M, n):
    """

    Parameters
    ----------
    N: int
        样本总数
    M: int
        某一类别的样本数目
    n: int
        抽取个数
    Returns
    -------
    返回对应的二项分布类
    """
    # p = M / N
    return Binom(n, M / N)

n, p = 1000, 0.003
poi = b2poisson(n, p)  # λ=3
# 比较二项分布和泊松分布概率，k=0,1,2,3,4
binom = Binom(n, p)
print("二项分布与泊松近似（n=1000, p=0.003, λ=3）:")
print(f"k=5   Binom P(X=5)={binom.pmf(5):.5f}   Poisson P(X=5)={poi.pmf(5):.5f}")

# --- 案例2：超几何分布二项近似 ---
N, M, n_sample = 1000, 100, 10
hg = HyperGeom(N, M, n_sample)
bino = h2binom(N, M, n_sample)
print("超几何分布与二项近似（N=1000, M=100, n=10）:")
print(f"k=5   HyperGeom P(X=5)={hg.pmf(5):.5f}   Binom P(X=5)={bino.pmf(5):.5f}")
