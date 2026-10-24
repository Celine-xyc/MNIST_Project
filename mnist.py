import torch
import torch.nn as nn

class MNISTModel(nn.Module):
    def __init__(self):
        super().__init__()

        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(784,128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128,10)
    def forward(self,x):
        x = self.flatten(x)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
if __name__ == "__main__":
    model = MNISTModel()
    print("模型创建成功！")
model = MNISTModel()
x = torch.randn(1,1,28,28)
output = model(x)

print("输出形状：",x.shape)
print("输出形状：",output.shape)