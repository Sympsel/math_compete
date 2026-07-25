# -*- coding: utf-8 -*-
"""
    @author: 数模加油站
    @time  : 2025/10/21 11:48
    @file  : SA_sko.py
"""
import numpy as np
from matplotlib import pyplot as plt
from sko.SA import SA  # 从sko导入模拟退火

LB, UB = -1, 3  # 变量范围
INIT_TEMP = 100.0  # 初始温度（足够高，允许初期探索）
COOLING_RATE = 0.95  # 降温系数（接近1，缓慢降温）
MAX_ITER = 1000  # 总迭代次数
STEP_SIZE = 0.02  # 邻域搜索步长
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)  # 固定随机种子

# 1. 目标函数
def f(x):
    return x * np.sin(10 * np.pi * x) + 2.0


# 2. 配置sko的SA参数
sa_sko = SA(
    func=f,  # 目标函数
    x0=[0],  # 初始解
    T_max=INIT_TEMP,
    T_min=1e-5,  # 最低温度
    L=10,
    max_stay_counter=150,  # 连续不改进则停止
    lb=[LB],  # 下界
    ub=[UB],  # 上界
    step=STEP_SIZE,  # 邻域步长
)


# 3. 运行并记录历史最优
best_x_sko, best_f_sko = sa_sko.run()
# 提取每步最优值（sko的history是目标函数值列表）
history_sko = sa_sko.best_y_history[:MAX_ITER+1]  # 截取与手动实现相同长度


# 4. 输出结果
print(f"sko-SA最优解：x = {best_x_sko[0]:.4f}, f(x) = {best_f_sko[0]:.4f}")
plt.plot(history_sko, label="sko-SA")
plt.xlabel("Iteration")
plt.ylabel("Best Fitness (Minimization)")
plt.legend()
plt.show()
