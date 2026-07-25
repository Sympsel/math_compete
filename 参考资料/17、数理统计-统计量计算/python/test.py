# -*- coding: utf-8 -*-
"""
    @author: 数模加油站
    @time  : 2025/8/1 15:01
    @file  : test.py
"""

from distribute.binom import Binom
from distribute.poisson import Poisson
from distribute.Hypergeom import HyperGeom
from distribute.geom import Geom
from distribute.norm import Norm
from distribute.uniform import Uniform
from distribute.exp import Exp
from distribute.gamma import Gamma
from distribute.beta import Beta

# 1. 二项分布示例
b = Binom(10, 0.3)
print(b)

# 2. 泊松分布示例
p = Poisson(4.5)
print(p)

# 3. 超几何分布示例
hg = HyperGeom(50, 10, 5)
print(hg)

# 4. 几何分布示例
g = Geom(0.2)
print(g)

# 5. 正态分布示例
n = Norm(0, 1)
print(n)

# 6. 均匀分布示例
u = Uniform(2, 8)
print(u)

# 7. 指数分布示例
e = Exp(0.5)
print(e)

# 8. 伽马分布示例
gm = Gamma(2, 0.5)
print(gm)

# 9. 贝塔分布示例
be = Beta(2, 5)
print(be)

