# -*- coding: utf-8 -*-
"""
    @author: 数模加油站
    @time  : 2025/8/1 09:24
    @file  : poisson.py
"""

import math

class Poisson:
    """
    泊松分布类：使用纯数学方法计算泊松分布的概率特性

    属性
    ------
    lam : float
        单位时间（或单位面积、体积）内的平均事件发生次数 λ（lambda）

    方法
    ------
    pmf(k)               计算概率质量函数 P(X = k)
    cdf(k)               计算累积分布函数 P(X <= k)
    expectation()        返回期望 E[X]
    variance()           返回方差 Var[X]
    std_dev()            返回标准差 Std[X]
    coef_variation()     变异系数 CV = Std[X]/E[X]
    raw_moment(m)        m 阶原点矩 E[X^m]
    central_moment(m)    m 阶中心矩 E[(X - μ)^m]
    quantile(q)          分位数 Q(q) = min{k: CDF(k) >= q}
    skewness()           偏度 Skew[X]
    kurtosis(excess=False) 峰度 Kurt[X] 或 超额峰度
    """

    def __init__(self, lam):
        """
        初始化泊松分布对象

        参数
        ------
        lam : float
            平均事件发生率 λ，必须大于 0
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

    def _factorial(self, n):
        """
        计算阶乘 n!
        """
        if n < 0:
            raise ValueError("阶乘的输入必须是非负整数")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def pmf(self, k):
        """
        概率质量函数 PMF

        参数
        ------
        k : int
            事件发生的次数

        返回
        ------
        float : P(X = k)
        """
        if k < 0:
            return 0.0
        return (self.lam ** k) * math.exp(-self.lam) / self._factorial(k)

    def cdf(self, k):
        """
        累积分布函数 CDF

        参数
        ------
        k : int
            事件发生次数的上限

        返回
        ------
        float : P(X <= k)
        """
        if k < 0:
            return 0.0
        total = 0.0
        for i in range(0, k + 1):
            total += self.pmf(i)
        return total

    def expectation(self):
        """
        返回期望 E[X] = λ
        """
        return self.lam

    def variance(self):
        """
        返回方差 Var[X] = λ
        """
        return self.lam

    def std_dev(self):
        """
        返回标准差 Std[X] = sqrt(λ)
        """
        return math.sqrt(self.lam)

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
        k = 0
        while True:
            pk = self.pmf(k)
            if pk == 0:
                break
            total += (k ** m) * pk
            k += 1
        return total

    def central_moment(self, m):
        """
        m 阶中心矩 E[(X - μ)^m]
        """
        mu = self.E
        total = 0.0
        k = 0
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
        k = 0
        while True:
            cum += self.pmf(k)
            if cum >= q:
                return k
            k += 1

    def skewness(self):
        """
        偏度 Skew[X] = 1 / sqrt(λ)
        """
        return 1 / math.sqrt(self.lam)

    def kurtosis(self, excess=False):
        """
        峰度 Kurt[X] 或 超额峰度

        参数
        ------
        excess : bool
            是否返回超额峰度

        返回
        ------
        float
        """
        ex = 1 / self.lam
        return ex if excess else ex + 3

    def __str__(self):
        """
        返回分布概要信息
        """
        return f"""$泊松分布：X~P(\\lambda={self.lam})$
            期望: {self.E}
            方差: {self.Var}
            变异系数: {self.coef}
            偏度: {self.skew}
            峰度: {self.kurt}
        """
