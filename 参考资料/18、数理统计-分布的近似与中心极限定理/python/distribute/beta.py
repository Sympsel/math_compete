# -*- coding: utf-8 -*-
"""
    @author: 数模加油站
    @time  : 2025/8/1 10:22
    @file  : beta.py
"""

import math

class Beta:
    """
    贝塔分布类（Beta Distribution）

    属性
    ------
    alpha : float
        形状参数 α > 0
    beta : float
        形状参数 β > 0

    方法
    ------
    pdf(x)                 概率密度函数 f(x)
    cdf(x, steps=1000)     累积分布函数 F(x)
    expectation()          期望 E[X]
    variance()             方差 Var[X]
    std_dev()              标准差 Std[X]
    coef_variation()       变异系数 CV = Std[X]/E[X]
    raw_moment(k)          k 阶原点矩 E[X^k]
    central_moment(k)      k 阶中心矩 E[(X - μ)^k]
    quantile(q, tol, max_iter)  分位数 Q(q) 使 F(Q) = q
    skewness()             偏度 Skew[X]
    kurtosis(excess=False) 峰度 Kurt[X] 或 超额峰度
    """

    def __init__(self, alpha, beta):
        """
        初始化贝塔分布对象

        参数
        ------
        alpha : float
            α > 0
        beta : float
            β > 0
        """
        if alpha <= 0 or beta <= 0:
            raise ValueError("alpha 和 beta 必须都大于 0")
        self.alpha = alpha
        self.beta = beta

        self.E = self.expectation()
        self.Var = self.variance()
        self.std = self.variance()
        self.coef = self.coef_variation()
        self.skew = self.skewness()
        self.kurt = self.kurtosis()

    def _beta_function(self, a, b):
        """计算贝塔函数 B(a, b) = Γ(a)Γ(b)/Γ(a+b)"""
        return math.gamma(a) * math.gamma(b) / math.gamma(a + b)

    def pdf(self, x):
        """
        概率密度函数 PDF

        参数
        ------
        x : float, 定义在 (0, 1)

        返回
        ------
        float : f(x)
        """
        if x <= 0 or x >= 1:
            return 0.0
        coeff = 1 / self._beta_function(self.alpha, self.beta)
        return coeff * x**(self.alpha - 1) * (1 - x)**(self.beta - 1)

    def cdf(self, x, steps = 1000):
        """
        累积分布函数 CDF：P(X <= x)
        使用梯形法数值逼近

        参数
        ------
        x : float, ∈ [0, 1]
        steps : int
            积分精度（步数）

        返回
        ------
        float : F(x)
        """
        if x <= 0:
            return 0.0
        if x >= 1:
            return 1.0
        a, b = 0.0, x
        h = (b - a) / steps
        total = 0.5 * (self.pdf(a) + self.pdf(b))
        for i in range(1, steps):
            t = a + i * h
            total += self.pdf(t)
        return total * h

    def expectation(self):
        """期望 E[X] = α / (α + β)"""
        return self.alpha / (self.alpha + self.beta)

    def variance(self):
        """方差 Var[X] = αβ / [(α+β)^2 (α+β+1)]"""
        a, b = self.alpha, self.beta
        return (a * b) / ((a + b)**2 * (a + b + 1))

    def std_dev(self):
        """标准差 Std[X] = sqrt(Var[X])"""
        return math.sqrt(self.variance())

    def coef_variation(self):
        """变异系数 CV = Std[X] / E[X]"""
        mu = self.expectation()
        return self.std_dev() / mu if mu != 0 else float('inf')

    def raw_moment(self, k):
        """
        k 阶原点矩 E[X^k]
        解析：E[X^k] = B(α+k, β) / B(α, β)
        """
        a, b = self.alpha, self.beta
        return self._beta_function(a + k, b) / self._beta_function(a, b)

    def central_moment(self, k):
        """
        k 阶中心矩 E[(X - μ)^k]
        通过二项展开：sum_{i=0}^k C(k,i) (-μ)^{k-i} E[X^i]
        """
        mu = self.expectation()
        total = 0.0
        for i in range(0, k + 1):
            coeff = math.comb(k, i) * ((-mu)**(k - i))
            total += coeff * self.raw_moment(i)
        return total

    def quantile(self, q, tol = 1e-6, max_iter = 100):
        """
        分位数 Q(q)，解 F(x) = q
        使用二分查找

        参数
        ------
        q : float, ∈ [0, 1]
        tol : float
            误差容限
        max_iter : int
            最大迭代次数

        返回
        ------
        float : Q，使得 CDF(Q) ≈ q
        """
        if not 0 <= q <= 1:
            raise ValueError("q 必须在 [0, 1] 之间")
        lo, hi = 0.0, 1.0
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
        偏度 Skew[X]
        解析公式：
        2*(β-α)*sqrt(α+β+1) / [ (α+β+2)*sqrt(αβ) ]
        """
        a, b = self.alpha, self.beta
        num = 2 * (b - a) * math.sqrt(a + b + 1)
        den = (a + b + 2) * math.sqrt(a * b)
        return num / den

    def kurtosis(self, excess = False) -> float:
        """
        峰度 Kurt[X] 或 超额峰度（excess=True）
        解析公式（超额峰度）：
        6*[(α-β)^2*(α+β+1) - αβ*(α+β+2)]
          / [αβ(α+β+2)(α+β+3)]
        总峰度 = excess + 3
        """
        a, b = self.alpha, self.beta
        excess_k = 6 * (((a - b)**2 * (a + b + 1)) - (a * b * (a + b + 2))) \
                   / (a * b * (a + b + 2) * (a + b + 3))
        return excess_k if excess else excess_k + 3

    def __str__(self):
        return f"""$贝塔分布：X~Be(\\alpha={self.alpha}, \\beta={self.beta})$
            期望: {self.E}
            方差：{self.Var}
            变异系数：{self.coef}
            偏度：{self.skew}
            峰度：{self.kurt}
        """

