# -*- coding: utf-8 -*-
"""
    @author: 数模加油站
    @time  : 2025/8/1 14:57
    @file  : test.py
"""
import Hypergeom
import beta
import binom
import gamma
import geom
import norm
import poisson
import uniform
import exp

# 1. 二项分布：n=10, p=0.3, P(X=3)
bd = binom.Binom(n=10, p=0.3)
print(f"Binomial PMF P(X=3) = {bd.pmf(3):.6f}")

# 2. 泊松分布：λ=4.5, P(X=3)
pois = poisson.Poisson(lam=4.5)
print(f"Poisson PMF P(X=3)  = {pois.pmf(3):.6f}")

# 3. 超几何分布：N=50, K=10, n=5, P(X=2)
hg = Hypergeom.HyperGeom(N=50, M=10, n=5)
print(f"Hypergeometric PMF P(X=2) = {hg.pmf(2):.6f}")

# 4. 几何分布：p=0.2, P(X=3)
geo = geom.Geom(p=0.2)
print(f"Geometric PMF P(X=3) = {geo.pmf(3):.6f}")

# 5. 正态分布：μ=0, σ=1, f(1)
nd = norm.Norm(mu=0, sigma=1)
print(f"Normal PDF f(1) = {nd.pdf(1):.6f}")

# 6. 均匀分布：[2,7], f(5)
ud = uniform.Uniform(a=2, b=7)
print(f"Uniform PDF f(5) = {ud.pdf(5):.6f}")

# 7. 指数分布：λ=0.5, f(3)
exp = exp.Exp(lam=0.5)
print(f"Exponential PDF f(3) = {exp.pdf(3):.6f}")

# 8. 伽马分布：k=2, λ=0.5, f(3)
gamma_dist = gamma.Gamma(k=2, lam=0.5)
print(f"Gamma PDF f(3) = {gamma_dist.pdf(3):.6f}")

# 9. 贝塔分布：α=2, β=5, f(0.3)
beta_dist = beta.Beta(alpha=2, beta=5)
print(f"Beta PDF f(0.3) = {beta_dist.pdf(0.3):.6f}")
