# -*- coding: utf-8 -*-
"""
    @author: 数模加油站
    @time  : 2025/10/21 11:48
    @file  : SA_math.py
"""

import numpy as np
import matplotlib.pyplot as plt


# 1. 问题参数
def f(x):
    """目标函数（最小化）"""
    return x * np.sin(10 * np.pi * x) + 2.0


LB, UB = -1, 3  # 变量范围
INIT_TEMP = 100.0  # 初始温度（足够高，允许初期探索）
COOLING_RATE = 0.95  # 降温系数（接近1，缓慢降温）
MAX_ITER = 1000  # 总迭代次数
STEP_SIZE = 0.02  # 邻域搜索步长


# 2. 模拟退火主逻辑
def simulated_annealing():
    # 初始化当前解（随机在范围内取值）
    current_x = np.random.uniform(LB, UB)
    current_f = f(current_x)

    # 记录最优解
    best_x = current_x
    best_f = current_f

    # 记录每步最优值（用于绘图）
    best_history = [best_f]

    temp = INIT_TEMP  # 当前温度

    for i in range(MAX_ITER):
        # 生成邻域解（在当前解附近随机扰动）
        new_x = current_x + np.random.uniform(-STEP_SIZE, STEP_SIZE)
        new_x = np.clip(new_x, LB, UB)  # 确保在范围内
        new_f = f(new_x)

        # 计算能量差（目标函数差）
        delta_f = new_f - current_f  # 最小化问题：delta_f < 0 表示新解更优

        # Metropolis准则：接受新解的概率
        if delta_f < 0:
            # 新解更优，直接接受
            current_x, current_f = new_x, new_f
        else:
            # 新解较差，按概率接受（温度越高，接受概率越大）
            prob = np.exp(-delta_f / temp)
            if np.random.rand() < prob:
                current_x, current_f = new_x, new_f

        # 更新全局最优
        if current_f < best_f:
            best_x, best_f = current_x, current_f

        # 记录当前最优
        best_history.append(best_f)

        # 降温（指数衰减）
        temp *= COOLING_RATE

    return best_x, best_f, best_history


# 3. 运行并输出结果
best_x_manual, best_f_manual, history_manual = simulated_annealing()
print(f"手动SA最优解：x = {best_x_manual:.4f}, f(x) = {best_f_manual:.4f}")

plt.plot(history_manual, label="Manual SA")
plt.xlabel("Iteration")
plt.ylabel("Best Fitness (Minimization)")
plt.legend()
plt.show()
