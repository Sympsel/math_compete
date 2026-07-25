# -*- coding: utf-8 -*-
"""
    @author: 数模加油站
    @time  : 2025/8/1 09:33
    @file  : HyperGeom.py
"""

import math

class HyperGeom:
    """
    超几何分布类：用于模拟从有限总体中不放回抽样的概率问题

    属性
    ------
    N : int
        总体总数
    M : int
        总体中感兴趣的元素数量（“成功”元素）
    n : int
        抽样数量（样本容量）

    方法
    ------
    pmf(k)               计算概率质量函数 P(X = k)
    cdf(k)               计算累积分布函数 P(X <= k)
    expectation()        返回期望 E[X]
    variance()           返回方差 Var[X]
    std_dev()            返回标准差 Std[X]
    coef_variation()     变异系数 CV = Std[X]/E[X]
    raw_moment(m)        m 阶原点矩 E[X^m] = Σ k^m P(X=k)
    central_moment(m)    m 阶中心矩 E[(X - μ)^m] = Σ (k-μ)^m P(X=k)
    quantile(q)          分位数 Q(q) = min{k: CDF(k) >= q}
    skewness()           偏度 Skew[X] = E[(X-μ)^3]/Std^3
    kurtosis(excess=False) 峰度 Kurt[X] 或 超额峰度
    __str__()            分布概要信息
    """

    def __init__(self, N, M, n):
        """
        初始化超几何分布参数

        参数
        ------
        N : int
            总体总数（必须 >= 1）
        M : int
            总体中成功元素数量（0 <= M <= N）
        n : int
            抽样数量（0 <= n <= N）
        """
        if not (0 <= M <= N):
            raise ValueError("M 必须满足 0 <= M <= N")
        if not (0 <= n <= N):
            raise ValueError("n 必须满足 0 <= n <= N")
        self.N = N
        self.M = M
        self.n = n

        self.E = self.expectation()
        self.Var = self.variance()
        self.std = self.std_dev()
        self.coef = self.coef_variation()
        self.skew = self.skewness()
        self.kurt = self.kurtosis()


    def pmf(self, k):
        """
        概率质量函数 P(X = k)
        """
        if k < 0 or k > self.n or k > self.M or self.n - k > self.N - self.M:
            return 0.0
        num = math.comb(self.M, k) * math.comb(self.N - self.M, self.n - k)
        den = math.comb(self.N, self.n)
        return num / den

    def cdf(self, k):
        """
        累积分布函数 P(X <= k)
        """
        total = 0.0
        low = max(0, self.n + self.M - self.N)
        high = min(k, self.n, self.M)
        for i in range(low, high + 1):
            total += self.pmf(i)
        return total

    def expectation(self):
        """
        返回期望 E[X] = n * M / N
        """
        return self.n * self.M / self.N

    def variance(self):
        """
        返回方差 Var[X] = n*(M/N)*(1-M/N)*(N-n)/(N-1)
        """
        return (self.n * (self.M / self.N) * (1 - self.M / self.N)
                * (self.N - self.n) / (self.N - 1))

    def std_dev(self):
        """
        返回标准差 Std[X]
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
        m 阶原点矩 E[X^m]
        """
        total = 0.0
        low = max(0, self.n + self.M - self.N)
        high = min(self.n, self.M)
        for i in range(low, high + 1):
            total += (i ** m) * self.pmf(i)
        return total

    def central_moment(self, m):
        """
        m 阶中心矩 E[(X-μ)^m]
        """
        mu = self.E
        total = 0.0
        low = max(0, self.n + self.M - self.N)
        high = min(self.n, self.M)
        for i in range(low, high + 1):
            total += ((i - mu) ** m) * self.pmf(i)
        return total

    def quantile(self, q):
        """
        分位数 Q(q) = min{k: CDF(k) >= q}
        """
        if not 0 <= q <= 1:
            raise ValueError("q 必须在 [0, 1] 之间")
        cum = 0.0
        low = max(0, self.n + self.M - self.N)
        high = min(self.n, self.M)
        for i in range(low, high + 1):
            cum += self.pmf(i)
            if cum >= q:
                return i
        return high

    def skewness(self):
        """
        偏度 Skew[X] = E[(X-μ)^3] / Std[X]^3
        """
        return self.central_moment(3) / (self.std ** 3)

    def kurtosis(self, excess=False):
        """
        峰度 Kurt[X] 或 超额峰度
        """
        k4 = self.central_moment(4) / (self.std ** 4)
        return (k4 - 3) if excess else k4

    def __str__(self):
        """
        返回分布概要信息
        """
        return f"""$超几何分布：X~HG(N={self.N}, M={self.M}, n={self.n})$
            期望: {self.E}
            方差: {self.Var}
            变异系数: {self.coef}
            偏度: {self.skew}
            峰度: {self.kurt}
        """
