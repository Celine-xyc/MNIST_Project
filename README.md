# MNIST 手写数字识别

使用 PyTorch 实现的一个简单神经网络，对 MNIST 手写数字（0–9）进行分类。

## 项目结构

| 文件 | 说明 |
|------|------|
| `train.py` | 训练主程序：读取数据、训练模型、测试准确率、保存权重 |
| `mnist.py` | 神经网络模型定义（`MNISTModel`：784 → 128 → 10） |
| `data_loader.py` | 读取并解析 MNIST 的 `.gz` 数据文件 |
| `main.py` | Python 基础练习代码（变量、列表、函数、字典等） |
| `calculator.py` | 简单的 `add` 函数示例 |

## 环境依赖

- Python 3.x
- PyTorch（`torch`、`torch.nn`）

安装依赖：

```bash
pip install torch
```

## 准备数据集

项目使用 MNIST 原始数据，需将以下 4 个文件放入 `data/` 目录（该目录已被 `.gitignore` 忽略，不会上传）：

```
data/
├── train-images-idx3-ubyte.gz
├── train-labels-idx1-ubyte.gz
├── t10k-images-idx3-ubyte.gz
└── t10k-labels-idx1-ubyte.gz
```

可从此处下载：<http://yann.lecun.com/exdb/mnist/>

## 运行

```bash
python train.py
```

训练完成后会：

- 打印每个 epoch 的损失值
- 输出测试集准确率
- 将模型权重保存为 `model.pth`（本地文件，不上传）

## 模型结构

```
Flatten → Linear(784, 128) → ReLU → Linear(128, 10)
```
