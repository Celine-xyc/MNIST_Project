import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader

from mnist import MNISTModel
from data_loader import load_images, load_labels


# 1. 读取训练数据和测试数据
print("正在读取 MNIST 数据...")

train_images = load_images("train-images-idx3-ubyte.gz")
train_labels = load_labels("train-labels-idx1-ubyte.gz")

test_images = load_images("t10k-images-idx3-ubyte.gz")
test_labels = load_labels("t10k-labels-idx1-ubyte.gz")

# 2. 把图片和标签整理成批次
train_dataset = TensorDataset(train_images, train_labels)
test_dataset = TensorDataset(test_images, test_labels)

train_loader = DataLoader(
    train_dataset, batch_size=64, shuffle=True
)
test_loader = DataLoader(
    test_dataset, batch_size=64, shuffle=False
)

# 3. 创建神经网络模型
model = MNISTModel()

# 4. 设置学习方法
loss_function = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(
    model.parameters(), lr=0.001
)

# 5. 开始训练
epochs = 3

for epoch in range(epochs):
    model.train()
    total_loss = 0.0

    for images, labels in train_loader:
        # 根据图片进行预测
        outputs = model(images)

        # 计算预测结果与正确答案的差距
        loss = loss_function(outputs, labels)

        # 清空之前的梯度
        optimizer.zero_grad()

        # 计算梯度
        loss.backward()

        # 更新模型参数
        optimizer.step()

        total_loss += loss.item()

    average_loss = total_loss / len(train_loader)

    print(
        f"Epoch [{epoch + 1}/{epochs}], "
        f"Loss: {average_loss:.4f}"
    )

# 6. 使用测试数据检查准确率
model.eval()
correct = 0
total = 0

with torch.no_grad():
    for images, labels in test_loader:
        outputs = model(images)
        predictions = outputs.argmax(dim=1)

        correct += (predictions == labels).sum().item()
        total += labels.size(0)

accuracy = 100 * correct / total

print(f"测试集准确率：{accuracy:.2f}%")

# 7. 保存训练好的模型
torch.save(model.state_dict(), "model.pth")

print("训练完成！模型已保存为 model.pth")