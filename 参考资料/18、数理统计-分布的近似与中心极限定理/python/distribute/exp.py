# -*- coding: utf-8 -*-
"""
    @author: 数模加油站
    @time  : 2025/8/1 10:16
    @file  : exp.py
"""

import math

class Exp:
    """
    指数分布类（Exponential Distribution）

    属性
    ------
    lam : float
        事件发生的速率参数 λ（lambda），必须大于 0

    方法
    ------
    pdf(x)               概率密度函数 f(x)
    cdf(x)               累积分布函数 P(X <= x)
    expectation()        返回期望 E[X]
    variance()           返回方差 Var[X]
    std_dev()            返回标准差 Std[X]
    coef_variation()     变异系数 CV = Std[X]/E[X]
    raw_moment(k)        k 阶原点矩 E[X^k]
    central_moment(k)    k 阶中心矩 E[(X - μ)^k]
    quantile(q)          分位数 Q(q) = -ln(1-q)/λ
    skewness()           偏度 Skew[X]
    kurtosis(excess=False) 峰度 Kurt[X] 或 超额峰度
    """

    def __init__(self, lam):
        """
        初始化指数分布

        参数
        ------
        lam : float
            速率参数 λ（lambda），必须大于 0
        """
        if lam <= 0:
            raise ValueError("λ (lambda) 必须为正数")
        self.lam = lam

        self.E = self.expectation()
        self.Var = self.variance()
        self.std = self.std_dev()
        self.coef = self.coef_variation()
        self.skew = self.skewness()
        self.kurt = self.kurtosis()

    def pdf(self, x):
        """
        概率密度函数 PDF：f(x)

        参数
        ------
        x : float
            自变量 x ≥ 0

        返回
        ------
        float : 密度值 f(x)
        """
        if x < 0:
            return 0.0
        return self.lam * math.exp(-self.lam * x)

    def cdf(self, x):
        """
        累积分布函数 CDF：P(X <= x)

        参数
        ------
        x : float

        返回
        ------
        float : 累积概率 P(X <= x)
        """
        if x < 0:
            return 0.0
        return 1 - math.exp(-self.lam * x)

    def expectation(self):
        """
        返回期望 E[X] = 1 / λ
        """
        return 1 / self.lam

    def variance(self):
        """
        返回方差 Var[X] = 1 / λ^2
        """
        return 1 / (self.lam ** 2)

    def std_dev(self):
        """
        返回标准差 Std[X] = 1 / λ
        """
        return 1 / self.lam

    def coef_variation(self):
        """
        变异系数 CV = Std[X] / E[X]
        """
        mu = self.E
        return self.std / mu if mu != 0 else float('inf')

    def raw_moment(self, k):
        """
        k 阶原点矩 E[X^k] = k! / λ^k
        """
        return math.factorial(k) / (self.lam ** k)

    def central_moment(self, k):
        """
        k 阶中心矩 E[(X - μ)^k]
        使用原点矩与期望 μ 通过二项展开计算
        """
        mu = self.E
        total = 0.0
        for i in range(0, k + 1):
            coeff = math.comb(k, i) * ((-mu) ** (k - i))
            total += coeff * self.raw_moment(i)
        return total

    def quantile(self, q):
        """
        分位数 Q(q) = -ln(1 - q) / λ

        参数
        ------
        q : float, ∈ [0, 1]

        返回
        ------
        float : 分位数值
        """
        if not 0 <= q <= 1:
            raise ValueError("q 必须在 [0, 1] 之间")
        return -math.log(1 - q) / self.lam

    def skewness(self):
        """
        偏度 Skew[X] = 2
        """
        return 2

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
        ex = 6
        return ex if excess else ex + 3

    def __str__(self):
        """
        返回分布概要信息
        """
        return f"""$指数分布：X~Exp(\\lambda={self.lam})$
            期望: {self.E}
            方差: {self.Var}
            变异系数: {self.coef}
            偏度: {self.skew}
            峰度: {self.kurt}
        """
