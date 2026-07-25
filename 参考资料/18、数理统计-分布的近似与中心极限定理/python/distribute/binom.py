# -*- coding: utf-8 -*-
"""
    @author: 数模加油站
    @time  : 2025/8/1 08:44
    @file  : binom.py
"""

import math

class Binom:
    """
    二项分布

    Property
    ------
    n : int
        重复试验的次数
    p : float
        每次试验成功的概率，必须满足 0 <= p <= 1

    Method
    ------
    pmf(k)
        计算概率质量函数 P(X = k)
    cdf(k)
        计算累积分布函数 P(X <= k)
    expectation()
        返回期望 E[X]
    variance()
        返回方差 Var[X]
    std_dev()
        返回标准差 Std[X]
    coef_variation()
        变异系数 CV = Std[X]/E[X]
    raw_moment(k)
        k 阶原点矩 E[X^k]
    central_moment(k)
        k 阶中心矩 E[(X - μ)^k]
    quantile(q)
        分位数 Q(q) = min{k: CDF(k) >= q}
    skewness()
        偏度 Skew[X]
    kurtosis(excess=False)
        峰度 Kurt[X] 或 超额峰度
    """

    def __init__(self, n, p):
        """
        初始化二项分布对象

        Parameters
        ------
        n : int
            总的独立重复试验次数
        p : float
            每次成功的概率，0 <= p <= 1
        """
        if not isinstance(n, int) or n <= 0:
            raise ValueError("实验次数 n 必须为正整数")
        if not (0 <= p <= 1):
            raise ValueError("成功概率 p 必须在 [0, 1] 区间内")

        self.n = n
        self.p = p

        self.E = self.expectation()
        self.Var = self.variance()
        self.Std = self.std_dev()
        self.coef = self.coef_variation()
        self.skew = self.skewness()
        self.kurt = self.kurtosis()

    def _combination(self, n, k):
        """
        计算组合数 C(n, k) = n! / (k! * (n-k)!)

        使用迭代法避免阶乘溢出
        """
        if k < 0 or k > n:
            return 0
        if k == 0 or k == n:
            return 1

        k = min(k, n - k)
        result = 1
        for i in range(1, k + 1):
            result *= n - i + 1
            result //= i
        return result

    def pmf(self, k):
        """
        概率质量函数（PMF）

        参数
        ------
        k : int
            成功的次数

        返回
        ------
        float : P(X = k) 的概率
        """
        if k < 0 or k > self.n:
            return 0.0

        comb = self._combination(self.n, k)
        return comb * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """
        累积分布函数（CDF）

        参数
        ------
        k : int
            成功次数阈值

        返回
        ------
        float : P(X <= k) 的累积概率
        """
        if k < 0:
            return 0.0
        if k >= self.n:
            return 1.0

        total = 0.0
        for i in range(0, k + 1):
            total += self.pmf(i)
        return total

    def expectation(self):
        """
        返回期望值 E[X] = n * p
        """
        return self.n * self.p

    def variance(self):
        """
        返回方差 Var[X] = n * p * (1 - p)
        """
        return self.n * self.p * (1 - self.p)

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
        return self.Std / mu if mu != 0 else float('inf')

    def raw_moment(self, k):
        """
        k 阶原点矩 E[X^k]
        通过 ∑ i^k * P(X=i) 计算
        """
        total = 0.0
        for i in range(self.n + 1):
            total += (i ** k) * self.pmf(i)
        return total

    def central_moment(self, k):
        """
        k 阶中心矩 E[(X - μ)^k]
        通过 ∑ (i - μ)^k * P(X=i) 计算
        """
        mu = self.E
        total = 0.0
        for i in range(self.n + 1):
            total += ((i - mu) ** k) * self.pmf(i)
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
        for i in range(self.n + 1):
            cum += self.pmf(i)
            if cum >= q:
                return i
        return self.n

    def skewness(self):
        """
        偏度 Skew[X] = (1 - 2p) / sqrt(n p (1 - p))
        """
        return (1 - 2 * self.p) / math.sqrt(self.n * self.p * (1 - self.p))

    def kurtosis(self, excess=False):
        """
        峰度 Kurt[X] 或 超额峰度

        参数
        ------
        excess : bool
            是否返回超额峰度，默认 False

        返回
        ------
        float : 峰度值
        """
        ex_k = (1 - 6 * self.p * (1 - self.p)) / (self.n * self.p * (1 - self.p))
        return ex_k if excess else ex_k + 3

    def __str__(self):
        """
        返回分布概要信息
        """
        return f"""$二项分布：X~B(n={self.n}, p={self.p})$
            期望: {self.E}
            方差: {self.Var}
            变异系数: {self.coef}
            偏度: {self.skew}
            峰度: {self.kurt}
        """
