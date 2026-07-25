# -*- coding: utf-8 -*-
"""
    @author: 数模加油站
    @time  : 2025/8/1 09:38
    @file  : geom.py
"""

import math

class Geom:
    """
    几何分布类：表示第一次成功所需的试验次数（X ∈ {1, 2, 3, ...}）

    属性
    ------
    p : float
        每次伯努利试验成功的概率（0 < p <= 1）

    方法
    ------
    pmf(k)               返回 P(X = k)：第 k 次试验才成功的概率
    cdf(k)               返回 P(X <= k)：在前 k 次试验中至少成功一次的概率
    expectation()        返回期望 E[X]
    variance()           返回方差 Var[X]
    std_dev()            返回标准差 Std[X]
    coef_variation()     变异系数 CV = Std[X]/E[X]
    raw_moment(m)        m 阶原点矩 E[X^m] = Σ k^m P(X=k)
    central_moment(m)    m 阶中心矩 E[(X - μ)^m] = Σ (k-μ)^m P(X=k)
    quantile(q)          分位数 Q(q) = min{k: CDF(k) >= q}
    skewness()           偏度 Skew[X] = (2 - p) / sqrt(1 - p)
    kurtosis(excess=False)
                         峰度 Kurt[X] 或 超额峰度
    """

    def __init__(self, p):
        """
        初始化几何分布对象

        参数
        ------
        p : float
            每次试验成功的概率，必须满足 0 < p <= 1
        """
        if not (0 < p <= 1):
            raise ValueError("成功概率 p 必须在 (0, 1] 区间内")
        self.p = p

        self.E = self.expectation()
        self.Var = self.variance()
        self.std = self.std_dev()
        self.coef = self.coef_variation()
        self.skew = self.skewness()
        self.kurt = self.kurtosis()

    def pmf(self, k):
        """
        概率质量函数：P(X = k)

        参数
        ------
        k : int
            第 k 次才成功

        返回
        ------
        float : P(X = k)
        """
        if k < 1:
            return 0.0
        return (1 - self.p) ** (k - 1) * self.p

    def cdf(self, k):
        """
        累积分布函数：P(X <= k)

        参数
        ------
        k : int
            最大尝试次数

        返回
        ------
        float : P(X <= k)
        """
        if k < 1:
            return 0.0
        return 1 - (1 - self.p) ** k

    def expectation(self):
        """
        返回期望 E[X] = 1 / p
        """
        return 1 / self.p

    def variance(self):
        """
        返回方差 Var[X] = (1 - p) / p^2
        """
        return (1 - self.p) / (self.p ** 2)

    def std_dev(self):
        """
        返回标准差 Std[X] = sqrt(Var[X])
        """
        return math.sqrt(self.variance())

    def coef_variation(self):
        """
        变异系数 CV = Std[X] / E[X]
        """
        mu = self.E
        return self.std / mu if mu != 0 else float('inf')

    def raw_moment(self, m):
        """
        m 阶原点矩 E[X^m] = Σ k^m P(X=k)
        """
        total = 0.0
        k = 1
        while True:
            pk = self.pmf(k)
            if pk == 0:
                break
            total += (k ** m) * pk
            k += 1
        return total

    def central_moment(self, m):
        """
        m 阶中心矩 E[(X - μ)^m] = Σ (k - μ)^m P(X=k)
        """
        mu = self.E
        total = 0.0
        k = 1
        while True:
            pk = self.pmf(k)
            if pk == 0:
                break
            total += ((k - mu) ** m) * pk
            k += 1
        return total

    def quantile(self, q):
        """
        分位数 Q(q) = min{k: CDF(k) >= q}

        参数
        ------
        q : float, ∈ [0, 1]

        返回
        ------
        int : 分位数 k
        """
        if not 0 <= q <= 1:
            raise ValueError("q 必须在 [0, 1] 之间")
        cum = 0.0
        k = 1
        while True:
            cum += self.pmf(k)
            if cum >= q:
                return k
            k += 1

    def skewness(self):
        """
        偏度 Skew[X] = (2 - p) / sqrt(1 - p)
        """
        return (2 - self.p) / math.sqrt(1 - self.p)

    def kurtosis(self, excess=False):
        """
        峰度 Kurt[X] 或 超额峰度

        参数
        ------
        excess : bool
            是否返回超额峰度

        返回
        ------
        float : 峰度值
        """
        ex = (6 + self.p ** 2 / (1 - self.p))
        return ex if excess else ex + 3

    def __str__(self):
        """
        返回分布概要信息
        """
        return f"""$几何分布：X~Geom(p={self.p})$
            期望: {self.E}
            方差: {self.Var}
            变异系数: {self.coef}
            偏度: {self.skew}
            峰度: {self.kurt}
        """
