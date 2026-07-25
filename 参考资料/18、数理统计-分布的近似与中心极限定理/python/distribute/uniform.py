# -*- coding: utf-8 -*-
"""
    @author: 数模加油站
    @time  : 2025/8/1 10:15
    @file  : uniform.py
"""

import math

class Uniform:
    """
    连续型均匀分布类（Uniform Distribution）

    表示一个在 [a, b] 区间上均匀分布的随机变量

    属性
    ------
    a : float
        区间左端点
    b : float
        区间右端点（必须 a < b）

    方法
    ------
    pdf(x)               概率密度函数 f(x)
    cdf(x)               累积分布函数 P(X <= x)
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

    def __init__(self, a, b):
        """
        初始化均匀分布对象

        参数
        ------
        a : float
            区间起点
        b : float
            区间终点，需满足 b > a
        """
        if b <= a:
            raise ValueError("区间参数必须满足 b > a")
        self.a = a
        self.b = b

        self.E = self.expectation()
        self.Var = self.variance()
        self.std = self.std_dev()
        self.coef = self.coef_variation()
        self.skew = self.skewness()
        self.kurt = self.kurtosis()

    def pdf(self, x):
        """
        概率密度函数 f(x)

        参数
        ------
        x : float

        返回
        ------
        float : 对应的密度值
        """
        if self.a <= x <= self.b:
            return 1 / (self.b - self.a)
        return 0.0

    def cdf(self, x):
        """
        累积分布函数 P(X <= x)

        参数
        ------
        x : float

        返回
        ------
        float : 累计概率
        """
        if x < self.a:
            return 0.0
        if x > self.b:
            return 1.0
        return (x - self.a) / (self.b - self.a)

    def expectation(self):
        """
        返回期望 E[X] = (a + b) / 2
        """
        return (self.a + self.b) / 2

    def variance(self):
        """
        返回方差 Var[X] = (b - a)^2 / 12
        """
        return ((self.b - self.a) ** 2) / 12

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

    def raw_moment(self, m, steps=1000):
        """
        m 阶原点矩 E[X^m] = ∫_a^b x^m f(x) dx（数值积分）

        参数
        ------
        m : int 阶数
        steps : int 分割步数
        """
        a, b = self.a, self.b
        h = (b - a) / steps
        total = 0.5 * ((a ** m) * self.pdf(a) + (b ** m) * self.pdf(b))
        for i in range(1, steps):
            x = a + i * h
            total += (x ** m) * self.pdf(x)
        return total * h

    def central_moment(self, m, steps=1000):
        """
        m 阶中心矩 E[(X - μ)^m] = ∫_a^b (x - μ)^m f(x) dx（数值积分）

        参数
        ------
        m : int 阶数
        steps : int 分割步数
        """
        mu = self.E
        a, b = self.a, self.b
        h = (b - a) / steps
        total = 0.5 * (((a - mu) ** m) * self.pdf(a) + ((b - mu) ** m) * self.pdf(b))
        for i in range(1, steps):
            x = a + i * h
            total += ((x - mu) ** m) * self.pdf(x)
        return total * h

    def quantile(self, q, tol=1e-6, max_iter=100):
        """
        分位数 Q(q)，解 F(x) = q，使用二分法

        参数
        ------
        q : float, ∈ [0, 1]
        tol : float 容差
        max_iter : int 最大迭代次数
        """
        if not 0 <= q <= 1:
            raise ValueError("q 必须在 [0, 1] 之间")
        lo, hi = self.a, self.b
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
        峰度 Kurt[X] 或 超额峰度

        参数
        ------
        excess : bool 是否返回超额峰度
        """
        ex = -6/5
        return ex if excess else ex + 3

    def __str__(self):
        """
        返回分布概要信息
        """
        return f"""$均匀分布：X~U(a={self.a}, b={self.b})$
            期望: {self.E}
            方差: {self.Var}
            变异系数: {self.coef}
            偏度: {self.skew}
            峰度: {self.kurt}
        """
