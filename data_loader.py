import gzip
import struct
from pathlib import Path

import torch


# 找到项目里的 data 文件夹
DATA_DIR = Path(__file__).parent / "data"


def load_images(filename):
    path = DATA_DIR / filename

    with gzip.open(path, "rb") as f:
        magic, count, rows, cols = struct.unpack(">IIII", f.read(16))
        data = bytearray(f.read())

    images = torch.frombuffer(data, dtype=torch.uint8).clone()
    images = images.reshape(count, 1, rows, cols).float() / 255.0

    return images


def load_labels(filename):
    path = DATA_DIR / filename

    with gzip.open(path, "rb") as f:
        magic, count = struct.unpack(">II", f.read(8))
        data = bytearray(f.read())

    labels = torch.frombuffer(data, dtype=torch.uint8).clone().long()

    return labels


if __name__ == "__main__":
    train_images = load_images("train-images-idx3-ubyte.gz")
    train_labels = load_labels("train-labels-idx1-ubyte.gz")

    test_images = load_images("t10k-images-idx3-ubyte.gz")
    test_labels = load_labels("t10k-labels-idx1-ubyte.gz")

    print("训练图片形状：", train_images.shape)
    print("训练标签形状：", train_labels.shape)
    print("测试图片形状：", test_images.shape)
    print("测试标签形状：", test_labels.shape)

    print("图片像素范围：", train_images.min().item(),
          "到", train_images.max().item())
    print("第一张图片的数字标签：", train_labels[0].item())
    print("MNIST 数据读取成功！")