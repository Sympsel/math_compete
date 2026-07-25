# -*- coding: utf-8 -*-
"""
    @author: 数模加油站
    @time  : 2025/8/2 10:53
    @file  : t_test.py
"""
import math


def t_cdf(t, df, steps=10000):
    """
    计算t分布的累积分布函数（CDF）

    Parameters
    ----------
    t : float
        统计量取值。
    df : int
        自由度。
    steps : int, optional
        数值积分的步数，步数越大越精确，默认为10000。

    Returns
    -------
    float
        P(T <= t)，即t分布左侧累计概率。
    """
    def t_pdf(x, df):
        # t分布的概率密度函数
        num = math.gamma((df + 1) / 2)
        den = math.sqrt(df * math.pi) * math.gamma(df / 2)
        return num / den * (1 + x ** 2 / df) ** (-(df + 1) / 2)
    a, b = -20, t  # 积分下限为-20保证覆盖全部概率质量
    h = (b - a) / steps
    area = 0.5 * (t_pdf(a, df) + t_pdf(b, df))
    # 梯形法累加积分
    for i in range(1, steps):
        area += t_pdf(a + i * h, df)
    return area * h

def t_test_1samp(xs, mu0=0, alpha=0.05, alternative='two-sided'):
    """
    单样本t检验，支持双尾、左尾、右尾

    Parameters
    ----------
    xs : list of float
        样本观测值。
    mu0 : float, optional
        原假设下的均值μ_0，默认为0。
    alpha : float, optional
        显著性水平，默认为0.05。
    alternative : {'two-sided', 'less', 'greater'}, optional
        检验类型：
            'two-sided'  —— 双尾检验 H1: mu != mu0
            'less'       —— 左尾检验 H1: mu < mu0
            'greater'    —— 右尾检验 H1: mu > mu0

    Returns
    -------
    t_stat : float
        计算得到的t统计量。
    df : int
        自由度。
    p : float
        检验的p值。
    reject : bool
        是否拒绝原假设（p < alpha）。

    Notes
    -----
    t统计量公式：
        t = (x̄ - μ0) / (s / sqrt(n))
    其中：
        x̄ 为样本均值
        s 为样本标准差
        n 为样本容量
    """
    n = len(xs)
    # 计算样本均值
    xbar = sum(xs) / n
    # 计算样本方差（无偏估计）
    s2 = sum((x - xbar) ** 2 for x in xs) / (n - 1)
    s = math.sqrt(s2)
    # 计算t统计量
    t_stat = (xbar - mu0) / (s / math.sqrt(n))
    df = n - 1
    # 计算累积概率
    cdf_val = t_cdf(t_stat, df)
    # 计算不同检验方式下的p值
    if alternative == 'two-sided':
        # 双尾：p = 2 * min{P(T <= t), P(T >= t)}
        p = 2 * min(cdf_val, 1 - cdf_val)
    elif alternative == 'less':
        # 左尾：p = P(T <= t)
        p = cdf_val
    elif alternative == 'greater':
        # 右尾：p = P(T >= t) = 1 - P(T <= t)
        p = 1 - cdf_val
    else:
        raise ValueError("alternative 仅能取 'two-sided', 'less', 'greater'")
    # 是否拒绝原假设
    reject = p < alpha
    return t_stat, df, p, reject

def t_test_ind(xs1, xs2, alpha=0.05, alternative='two-sided', equal_var=True):
    """
    独立样本t检验（两组独立样本均值比较）

    Parameters
    ----------
    xs1 : list of float
        第一组样本观测值。
    xs2 : list of float
        第二组样本观测值。
    alpha : float, optional
        显著性水平，默认为0.05。
    alternative : {'two-sided', 'less', 'greater'}, optional
        检验类型：
            'two-sided'  —— 双尾检验 H1: mu1 != mu2
            'less'       —— 左尾检验 H1: mu1 < mu2
            'greater'    —— 右尾检验 H1: mu1 > mu2
    equal_var : bool, optional
        是否假定两组样本方差相等（默认True，使用标准独立样本t检验；若为False，使用Welch's t检验）

    Returns
    -------
    t_stat : float
        计算得到的t统计量。
    df : int
        自由度。
    p : float
        检验的p值。
    reject : bool
        是否拒绝原假设（p < alpha）。

    Notes
    -----
    方差相等时的t检验（pooled）统计量公式：
        t = (x̄1 - x̄2) / sqrt(Sp^2 * (1/n1 + 1/n2))
        其中 Sp^2 为合并样本方差
        Sp^2 = [ (n1-1)*s1^2 + (n2-1)*s2^2 ] / (n1+n2-2)
        自由度 df = n1 + n2 - 2

    方差不等时（Welch's t检验）：
        t = (x̄1 - x̄2) / sqrt(s1^2/n1 + s2^2/n2)
        df = (s1^2/n1 + s2^2/n2)^2 / [ (s1^2/n1)^2/(n1-1) + (s2^2/n2)^2/(n2-1) ]
    """
    n1, n2 = len(xs1), len(xs2)
    mean1 = sum(xs1) / n1
    mean2 = sum(xs2) / n2
    # 计算两组样本方差
    s2_1 = sum((x - mean1) ** 2 for x in xs1) / (n1 - 1)
    s2_2 = sum((x - mean2) ** 2 for x in xs2) / (n2 - 1)

    if equal_var:
        # 方差相等情形（标准独立样本t检验）
        # 合并方差
        sp2 = ((n1 - 1) * s2_1 + (n2 - 1) * s2_2) / (n1 + n2 - 2)
        se = math.sqrt(sp2 * (1 / n1 + 1 / n2))  # 标准误
        t_stat = (mean1 - mean2) / se
        df = n1 + n2 - 2
    else:
        # 方差不等情形（Welch's t检验）
        se = math.sqrt(s2_1 / n1 + s2_2 / n2)
        t_stat = (mean1 - mean2) / se
        # Welch–Satterthwaite公式近似自由度
        numerator = (s2_1 / n1 + s2_2 / n2) ** 2
        denominator = ((s2_1 / n1) ** 2) / (n1 - 1) + ((s2_2 / n2) ** 2) / (n2 - 1)
        df = numerator / denominator

    # 计算累积概率
    cdf_val = t_cdf(t_stat, df)
    if alternative == 'two-sided':
        # 双尾：p = 2 * min{P(T <= t), P(T >= t)}
        p = 2 * min(cdf_val, 1 - cdf_val)
    elif alternative == 'less':
        # 左尾：p = P(T <= t)
        p = cdf_val
    elif alternative == 'greater':
        # 右尾：p = 1 - P(T <= t)
        p = 1 - cdf_val
    else:
        raise ValueError("alternative 仅能取 'two-sided', 'less', 'greater'")

    reject = p < alpha
    return t_stat, df, p, reject

def t_test_paired(xs1, xs2, alpha=0.05, alternative='two-sided'):
    """
    配对样本t检验（Paired Sample t-Test）

    Parameters
    ----------
    xs1 : list of float
        第一组配对观测值。
    xs2 : list of float
        第二组配对观测值。
    alpha : float, optional
        显著性水平，默认为0.05。
    alternative : {'two-sided', 'less', 'greater'}, optional
        检验类型：
            'two-sided'  —— 双尾 H1: mu_diff != 0
            'less'       —— 左尾 H1: mu_diff < 0
            'greater'    —— 右尾 H1: mu_diff > 0

    Returns
    -------
    t_stat : float
        t统计量。
    df : int
        自由度。
    p : float
        p值。
    reject : bool
        是否拒绝原假设（p < alpha）。

    Notes
    -----
    对每对观测$(x_i, y_i)$，差值$d_i = x_i - y_i$。
    t统计量公式：
        t = d̄ / (s_d / sqrt(n))
    其中d̄为差值均值，s_d为差值标准差，n为配对数量。
    """
    if len(xs1) != len(xs2):
        raise ValueError("两组样本数量必须一致（配对样本）")
    n = len(xs1)
    # 计算每对观测的差值
    ds = [x - y for x, y in zip(xs1, xs2)]
    d_bar = sum(ds) / n
    s2_d = sum((d - d_bar) ** 2 for d in ds) / (n - 1)
    s_d = math.sqrt(s2_d)
    # 计算t统计量
    t_stat = d_bar / (s_d / math.sqrt(n))
    df = n - 1
    cdf_val = t_cdf(t_stat, df)
    if alternative == 'two-sided':
        p = 2 * min(cdf_val, 1 - cdf_val)
    elif alternative == 'less':
        p = cdf_val
    elif alternative == 'greater':
        p = 1 - cdf_val
    else:
        raise ValueError("alternative 仅能取 'two-sided', 'less', 'greater'")
    reject = p < alpha
    return t_stat, df, p, reject

# ==========================
# 示例
# ==========================
xs = [55, 52, 48, 50, 53, 56, 49, 51, 58, 54]
mu0 = 50.0
t_stat, df, p, reject = t_test_1samp(xs, mu0, alpha=0.05, alternative='greater')
print(f"t统计量 = {t_stat:.4f}")
print(f"自由度 = {df}")
print(f"p值 = {p:.4f}")
print(f"结论：{'拒绝H0' if reject else '不拒绝H0'}")
print()
xs1 = [65, 68, 70, 63, 72, 67, 69, 71, 64, 66]
xs2 = [82, 78, 85, 80, 83, 77, 86, 79, 84, 81]

t_stat, df, p, reject = t_test_ind(xs1, xs2, alpha=0.05, alternative='less', equal_var=True)
print(f"【左侧检验】 t={t_stat:.4f},\n自由度={df:.2f},\np值={p}，\n结论：{'拒绝H0' if reject else '不拒绝H0'}")
print()

xs1 = [45, 60, 50, 55, 40, 65, 48, 70, 52, 58]
xs2 = [20, 25, 18, 28, 22, 30, 26, 15, 23, 19]
t_stat, df, p, reject = t_test_paired(xs1, xs2, alpha=0.05, alternative='greater')
print(f"【左侧检验】 t={t_stat:.4f}, \n自由度={df}, \np值={p}，\n结论：{'拒绝H0' if reject else '不拒绝H0'}")
