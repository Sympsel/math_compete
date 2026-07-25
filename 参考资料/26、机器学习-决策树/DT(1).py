import matplotlib.pyplot as plt  # 导入 matplotlib，用于绘制决策树和混淆矩阵图形
import seaborn as sns           # 导入 seaborn，用于更美观的热力图
import pandas as pd             # 导入 pandas，用于数据处理和 DataFrame 操作

from sklearn.datasets import load_iris        # 导入 scikit-learn 自带的 Iris 数据集加载函数
from sklearn.model_selection import train_test_split  # 导入数据集拆分函数
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree  # 导入决策树分类器、文本导出和可视化函数
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix  # 导入评估指标函数

# === 1. 加载 Iris 数据集 ===
iris = load_iris()  # 加载数据，返回 Bunch 对象，包含 data、target、feature_names、target_names 等
# 将特征矩阵转换为 DataFrame，列名使用 feature_names，便于后续处理和可视化
X = pd.DataFrame(iris.data, columns=iris.feature_names)
# 将目标向量转换为 Series，并命名为 'species'
y = pd.Series(iris.target, name="species")

# === 2. 拆分训练集和测试集 ===#
# train_test_split 将数据按给定比例随机拆分为训练集和测试集
# test_size=0.2 表示 20% 数据作为测试集，stratify=y 则保证拆分后各类别比例一致
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# === 3. 初始化决策树分类器 ===#
clf = DecisionTreeClassifier(
    criterion="gini",        # 分裂标准：'gini' 基尼不纯度，也可选 'entropy' 信息增益
    max_depth=None,            # 树的最大深度，None 表示不限制深度
    min_samples_split=2,       # 内部节点再分裂所需的最小样本数
    min_samples_leaf=1,        # 叶子节点最少要有的样本数
    random_state=42            # 随机种子，保证结果可复现
)

# === 4. 训练模型 ===#
clf.fit(X_train, y_train)  # 在训练集上训练决策树模型

# === 5. 在测试集上进行预测 ===#
y_pred = clf.predict(X_test)  # 使用训练好的模型对测试集进行预测，返回预测标签

# === 6. 模型评估 ===#
# 6.1 计算并打印准确率
acc = accuracy_score(y_test, y_pred)  # 计算预测正确的比例
print(f"Test Accuracy: {acc:.4f}")

# 6.2 打印更详细的分类报告，包括 precision、recall、f1-score
print(classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names  # 把数字标签映射成对应的花种名称
))

# === 7. 文本格式导出决策树规则 ===#
rules = export_text(clf, feature_names=iris.feature_names)  # 将决策树按文本形式导出，便于阅读规则
print("Decision Tree Rules:\n", rules)  # 打印导出的规则

# === 8. 可视化决策树结构 ===#
plt.figure(figsize=(12, 8))  # 设置图形大小
plot_tree(
    clf,
    feature_names=iris.feature_names,      # 特征名称，用于节点标签
    class_names=iris.target_names,         # 类别名称，用于叶节点标签
    filled=True,                           # 根据类别填充颜色
    rounded=True,                          # 节点框为圆角
    fontsize=10                            # 字体大小
)
plt.title("Decision Tree on Iris Dataset")  # 设置标题
plt.show()  # 显示图形

# === 9. 混淆矩阵计算与可视化 ===#
# 9.1 计算混淆矩阵，行表示真实标签，列表示预测标签
cm = confusion_matrix(y_test, y_pred)

# 9.2 使用 seaborn 绘制热力图，annot=True 在方格内标出数值，fmt='d' 显示整数
plt.figure(figsize=(6, 5))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    xticklabels=iris.target_names,  # X 轴标签为类别名称
    yticklabels=iris.target_names,  # Y 轴标签为类别名称
    cbar=False                      # 不显示颜色条
)
plt.xlabel("Predicted Label")  # 设置 X 轴标签
plt.ylabel("True Label")       # 设置 Y 轴标签
plt.title("Confusion Matrix on Iris")  # 设置图形标题
plt.tight_layout()  # 调整布局，防止标签被截断
plt.show()  # 显示图形
