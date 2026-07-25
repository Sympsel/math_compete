import torch  # 导入 PyTorch 主模块
import torch.nn as nn  # 导入神经网络相关模块
import torch.optim as optim  # 导入优化器模块
from torch.utils.data import DataLoader, TensorDataset  # 导入数据加载和张量数据集工具
from sklearn.model_selection import train_test_split  # 导入数据集拆分工具
from sklearn.preprocessing import StandardScaler  # 导入标准化工具
import pandas as pd  # 导入 pandas，用于处理 CSV 数据


# 定义一个包含三层的神经网络模型
class ThreeLayerNet(nn.Module):
    def __init__(self, input_dim=4, hidden1=16, hidden2=8, output_dim=3):
        super(ThreeLayerNet, self).__init__()  # 调用父类构造函数
        self.layer1 = nn.Linear(input_dim, hidden1)  # 输入层到第一隐藏层
        self.layer2 = nn.Linear(hidden1, hidden2)  # 第一隐藏层到第二隐藏层
        self.layer3 = nn.Linear(hidden2, output_dim)  # 第二隐藏层到输出层
        self.relu = nn.ReLU()  # 使用 ReLU 激活函数

    def forward(self, x):  # 定义前向传播过程
        x = self.relu(self.layer1(x))  # 第1层 + ReLU
        x = self.relu(self.layer2(x))  # 第2层 + ReLU
        x = self.layer3(x)  # 输出层（不加 Softmax，CrossEntropyLoss 会处理）
        return x


# 准备数据函数，从 CSV 读取数据并进行预处理
def prepare_data(csv_path="iris.csv", test_size=0.2, batch_size=16, device=None):
    df = pd.read_csv(csv_path)  # 从本地 CSV 文件读取数据

    # 指定特征列名称（与 iris.csv 文件列名一致）
    feature_cols = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    X = df[feature_cols].values  # 提取特征
    y = df['target'].values  # 提取标签

    scaler = StandardScaler()  # 创建标准化器
    X = scaler.fit_transform(X)  # 对特征进行标准化

    # 拆分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42, stratify=y
    )

    # 将数据转换为 PyTorch Tensor，并指定类型为 float32，移动到指定设备
    X_train = torch.tensor(X_train, dtype=torch.float32, device=device)
    y_train = torch.tensor(y_train, dtype=torch.long, device=device)
    X_test = torch.tensor(X_test, dtype=torch.float32, device=device)
    y_test = torch.tensor(y_test, dtype=torch.long, device=device)

    # 构建数据集对象
    train_ds = TensorDataset(X_train, y_train)
    test_ds = TensorDataset(X_test, y_test)

    # 构建数据加载器（支持批次读取和随机打乱）
    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_ds, batch_size=batch_size, shuffle=False)

    return train_loader, test_loader, scaler  # 返回训练加载器、测试加载器和标准化器


# 定义训练过程
def train(model, loader, criterion, optimizer):
    model.train()  # 设置模型为训练模式
    total_loss = 0.0  # 初始化损失
    for X_batch, y_batch in loader:  # 遍历每个批次
        logits = model(X_batch)  # 前向传播
        loss = criterion(logits, y_batch)  # 计算损失

        optimizer.zero_grad()  # 梯度清零
        loss.backward()  # 反向传播
        optimizer.step()  # 更新权重

        total_loss += loss.item() * X_batch.size(0)  # 累加总损失
    return total_loss / len(loader.dataset)  # 返回平均损失


# 定义评估过程（计算准确率）
def evaluate(model, loader):
    model.eval()  # 设置模型为评估模式
    correct = 0
    with torch.no_grad():  # 不计算梯度，节省内存
        for X_batch, y_batch in loader:
            logits = model(X_batch)  # 前向传播
            preds = logits.argmax(dim=1)  # 取每行最大值的索引作为预测类别
            correct += (preds == y_batch).sum().item()  # 累加预测正确数量
    return correct / len(loader.dataset)  # 返回准确率


# 主函数
def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")  # 自动选择设备

    # 准备数据（使用 iris.csv 文件）
    train_loader, test_loader, scaler = prepare_data(csv_path="iris.csv", device=device)

    # 初始化模型、损失函数、优化器，并移动到设备上
    model = ThreeLayerNet().to(device=device, dtype=torch.float32)
    criterion = nn.CrossEntropyLoss()  # 交叉熵损失用于分类任务
    optimizer = optim.Adam(model.parameters(), lr=0.01)  # Adam 优化器

    # 训练模型
    epochs = 50
    for epoch in range(1, epochs + 1):
        train_loss = train(model, train_loader, criterion, optimizer)  # 训练一次
        test_acc = evaluate(model, test_loader)  # 测试一次
        if epoch % 10 == 0 or epoch == 1:
            print(f"Epoch {epoch:02d}  Train Loss: {train_loss:.4f}  Test Acc: {test_acc:.4f}")

    # 单样本预测示例（需要标准化）
    raw_sample = [[5.1, 3.5, 1.4, 0.2]]  # 原始花朵测量数据
    sample_np = scaler.transform(raw_sample)  # 使用之前的 scaler 做标准化
    sample = torch.tensor(sample_np, dtype=torch.float32, device=device)  # 转换为 tensor

    model.eval()  # 设置为评估模式
    with torch.no_grad():
        logits = model(sample)  # 前向传播预测
        pred = logits.argmax(dim=1).item()  # 取预测类别

    # 输出预测结果
    print(f"Raw sample: {raw_sample}")
    print(f"Predicted class: {pred}  (0=setosa, 1=versicolor, 2=virginica)")


# 执行主函数
if __name__ == "__main__":
    main()
