# -*- coding: utf-8 -*-
"""
    @author: 数模加油站
    @time  : 2025/8/1 10:20
    @file  : gamma.py
"""

import math

class Gamma:
    """
    伽马分布类（Gamma Distribution）

    属性
    ------
    k : float
        形状参数 k > 0
    lam : float
        速率参数 λ > 0

    方法
    ------
    pdf(x)               概率密度函数 f(x)
    cdf(x, steps=1000)   累积分布函数 F(x)
    expectation()        返回期望 E[X]
    variance()           返回方差 Var[X]
    std_dev()            返回标准差 Std[X]
    coef_variation()     变异系数 CV = Std[X]/E[X]
    raw_moment(m)        m 阶原点矩 E[X^m]
    central_moment(m)    m 阶中心矩 E[(X - μ)^m]
    quantile(q, tol=1e-6, max_iter=100)  分位数 Q(q)
    skewness()           偏度 Skew[X]
    kurtosis(excess=False) 峰度 Kurt[X] 或 超额峰度
    __str__()            分布概要信息
    """

    def __init__(self, k, lam):
        """
        初始化伽马分布对象

        参数
        ------
        k : float
            形状参数 k > 0
        lam : float
            速率参数 λ > 0
        """
        if k <= 0 or lam <= 0:
            raise ValueError("参数 k 和 λ 必须都大于 0")
        self.k = k
        self.lam = lam

        self.E = self.expectation()
        self.Var = self.variance()
        self.std = self.std_dev()
        self.coef = self.coef_variation()
        self.skew = self.skewness()
        self.kurt = self.kurtosis()

    def pdf(self, x):
        """
        概率密度函数 PDF：f(x) = λ^k / Γ(k) * x^(k-1) * e^(-λ x)

        参数
        ------
        x : float, x > 0

        返回
        ------
        float : f(x)
        """
        if x <= 0:
            return 0.0
        return (self.lam**self.k) * (x**(self.k - 1)) * math.exp(-self.lam * x) / math.gamma(self.k)

    def cdf(self, x, steps=1000):
        """
        累积分布函数 CDF：F(x)=∫0^x f(t) dt
        使用梯形法数值积分

        参数
        ------
        x : float, 上限
        steps : int, 分割步数

        返回
        ------
        float : F(x)
        """
        if x <= 0:
            return 0.0
        a, b = 0.0, x
        h = (b - a) / steps
        total = 0.5 * (self.pdf(a) + self.pdf(b))
        for i in range(1, steps):
            t = a + i * h
            total += self.pdf(t)
        return total * h

    def expectation(self):
        """
        返回期望 E[X] = k / λ
        """
        return self.k / self.lam

    def variance(self):
        """
        返回方差 Var[X] = k / λ^2
        """
        return self.k / (self.lam**2)

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
        m 阶原点矩 E[X^m] = Γ(k + m) / (Γ(k) * λ^m)
        """
        return math.gamma(self.k + m) / (math.gamma(self.k) * (self.lam**m))

    def central_moment(self, m):
        """
        m 阶中心矩 E[(X - μ)^m]，通过二项展开
        """
        mu = self.E
        total = 0.0
        for i in range(m + 1):
            total += math.comb(m, i) * ((-mu)**(m - i)) * self.raw_moment(i)
        return total

    def quantile(self, q, tol=1e-6, max_iter=100):
        """
        分位数 Q(q)，解 F(x)=q，使用二分法

        参数
        ------
        q : float, ∈ [0, 1]
        tol : float, 容差
        max_iter : int, 最大迭代次数

        返回
        ------
        float : 分位数
        """
        if not 0 <= q <= 1:
            raise ValueError("q 必须在 [0, 1] 之间")
        lo, hi = 0.0, max(self.k / self.lam * 10, 1.0)
        for _ in range(max_iter):
            mid = (lo + hi) / 2
            if self.cdf(mid) < q:
                lo = mid
            else:
                hi = mid
            if hi - lo < tol:
                break
        return (lo + hi) / 2

    def skewness(self):
        """
        偏度 Skew[X] = 2 / sqrt(k)
        """
        return 2 / math.sqrt(self.k)

    def kurtosis(self, excess=False):
        """
        峰度 Kurt 或 超额峰度

        参数
        ------
        excess : bool, 是否返回超额峰度

        返回
        ------
        float
        """
        ex = 6 / self.k
        return ex if excess else ex + 3

    def __str__(self):
        """
        返回分布概要信息
        """
        return f"""$伽马分布：X~Ga(\\alpha={self.k}, \\lambda={self.lam})$
            期望: {self.E}
            方差: {self.Var}
            变异系数: {self.coef}
            偏度: {self.skew}
            峰度: {self.kurt}
        """
