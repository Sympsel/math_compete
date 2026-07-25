# -*- coding: utf-8 -*-
"""
    @author: 数模加油站
    @time  : 2025/8/1 09:33
    @file  : norm.py
"""

import math

class Norm:
    r"""
    正态分布类（Normal Distribution）

    属性
    ------
    mu : float
        均值（期望），决定曲线中心位置
    sigma : float
        标准差，决定曲线宽度，必须 > 0

    方法
    ------
    pdf(x)               返回概率密度函数 f(x)
    cdf(x)               返回累积分布函数 P(X <= x)
    expectation()        返回期望 E[X]
    variance()           返回方差 Var[X]
    std_dev()            返回标准差 Std[X]
    coef_variation()     变异系数 CV = Std[X]/E[X]
    raw_moment(m, steps) m 阶原点矩 E[X^m]（数值积分）
    central_moment(m, steps) m 阶中心矩 E[(X - μ)^m]
    quantile(q, tol, max_iter) 分位数 Q(q) 使 F(Q)=q
    skewness()           偏度 Skew[X]
    kurtosis(excess=False) 峰度 Kurt[X] 或 超额峰度
    __str__()            分布概要信息
    """

    def __init__(self, mu=0.0, sigma=1.0):
        """
        初始化正态分布

        参数
        ------
        mu : float
            分布均值（μ）
        sigma : float
            分布标准差（σ），必须为正数
        """
        if sigma <= 0:
            raise ValueError("sigma 必须为正数")
        self.mu = mu
        self.sigma = sigma

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

        返回
        ------
        float : 密度值
        """
        coeff = 1 / (self.sigma * math.sqrt(2 * math.pi))
        exponent = -((x - self.mu) ** 2) / (2 * self.sigma ** 2)
        return coeff * math.exp(exponent)

    def cdf(self, x):
        """
        累积分布函数 CDF：P(X <= x)

        参数
        ------
        x : float

        返回
        ------
        float : 累计概率
        """
        z = (x - self.mu) / (self.sigma * math.sqrt(2))
        return 0.5 * (1 + math.erf(z))

    def expectation(self):
        """
        返回期望 E[X] = μ
        """
        return self.mu

    def variance(self):
        """
        返回方差 Var[X] = σ^2
        """
        return self.sigma ** 2

    def std_dev(self):
        """
        返回标准差 Std[X] = σ
        """
        return self.sigma

    def coef_variation(self):
        """
        变异系数 CV = Std[X] / E[X]
        """
        return self.std / self.E if self.E != 0 else float('inf')

    def raw_moment(self, m, steps=1000):
        """
        m 阶原点矩 E[X^m] = ∫ x^m f(x) dx (数值积分)

        参数
        ------
        m : int 阶数
        steps : int 分割步数

        返回
        ------
        float
        """
        a = self.mu - 5 * self.sigma
        b = self.mu + 5 * self.sigma
        h = (b - a) / steps
        total = 0.5 * ((a ** m) * self.pdf(a) + (b ** m) * self.pdf(b))
        for i in range(1, steps):
            t = a + i * h
            total += (t ** m) * self.pdf(t)
        return total * h

    def central_moment(self, m, steps=1000):
        """
        m 阶中心矩 E[(X - μ)^m] (数值积分)

        参数
        ------
        m : int 阶数
        steps : int 分割步数

        返回
        ------
        float
        """
        a = self.mu - 5 * self.sigma
        b = self.mu + 5 * self.sigma
        h = (b - a) / steps
        total = 0.5 * (((a - self.mu) ** m) * self.pdf(a) + ((b - self.mu) ** m) * self.pdf(b))
        for i in range(1, steps):
            t = a + i * h
            total += ((t - self.mu) ** m) * self.pdf(t)
        return total * h

    def quantile(self, q, tol=1e-6, max_iter=100):
        """
        分位数 Q(q)，解 F(x)=q，使用二分法

        参数
        ------
        q : float, ∈ [0, 1]
        tol : float, 容差
        max_iter : int 最大迭代次数

        返回
        ------
        float
        """
        if not 0 <= q <= 1:
            raise ValueError("q 必须在 [0, 1] 之间")
        lo = self.mu - 5 * self.sigma
        hi = self.mu + 5 * self.sigma
        for _ in range(max_iter):
            mid = 0.5 * (lo + hi)
            if self.cdf(mid) < q:
                lo = mid
            else:
                hi = mid
            if hi - lo < tol:
                break
        return 0.5 * (lo + hi)

    def skewness(self):
        """
        偏度 Skew[X] = 0
        """
        return 0.0

    def kurtosis(self, excess=False):
        """
        峰度 Kurt 或 超额峰度

        参数
        ------
        excess : bool
            是否返回超额峰度

        返回
        ------
        float
        """
        ex = 0.0
        return ex if excess else ex + 3

    def __str__(self):
        """
        返回分布概要信息
        """
        return f"""$正态分布：X~N(\\mu={self.mu}, \\sigma={self.sigma})$
            期望: {self.E}
            方差: {self.Var}
            变异系数: {self.coef}
            偏度: {self.skew}
            峰度: {self.kurt}
        """
