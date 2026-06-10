"""
注意：此代码提取自学术论文，MinerU PDF转换过程中可能丢失了部分缩进，
使用前请手动修复 class/def 内部的缩进问题。
原始论文代码通过后可正常运行，此处仅做模块结构参考。

SE Net - Python Implementation

Paper: Squeeze-and-Excitation Networks
Source: MinerU markdown extraction
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn import init
import numpy as np




# --- Block 2 ---

class SEAttention(nn.Module):
    # 初始化SE模块，channel为通道数，reduction为降维比率
    def __init__(self, channel=512, reduction=16):
    super().__init__()
    self.avg_pool = nn.AdaptiveAvgPool2d(1)  # 自适应平均池化层，将特征图的空间维度压缩为1x1
    self.fc = nn.Sequential(  # 定义两个全连接层作为激励操作，通过降维和升维调整通道重要性
    nn.Linear(channel, channel // reduction, bias=False),  # 降维，减少参数数量和计算量
    nn.ReLU(inplace=True),  # ReLU激活函数，引入非线性
    nn.Linear(channel // reduction, channel, bias=False),  # 升维，恢复到原始通道数
    nn.Sigmoid()  # Sigmoid激活函数，输出每个通道的重要性系数
)


# --- Block 3 ---

def init_weights(self):
    for m in self.modules():  # 遍历模块中的所有子模块
    if isinstance(m, nn.Conv2d):  # 对于卷积层
    init.kaiming_normal_(m.weight, mode='fan_out')  # 使用Kaiming初始化方法初始化权重


# --- Block 4 ---

if m.bias is not None:
    init.constant_(m.bias, 0) # 如果有偏置项，则初始化为0
elif isinstance(m, nn.BatchNorm2d): # 对于批归一化层
    init.constant_(m.weight, 1) # 权重初始化为1
    init.constant_(m.bias, 0) # 偏置初始化为0
elif isinstance(m, nn.Linear): # 对于全连接层
    init.normal_(m.weight, std=0.001) # 权重使用正态分布初始化
    if m.bias is not None:
    init.constant_(m.bias, 0) # 偏置初始化为0


# --- Block 5 ---

def forward(self, x):
    b, c, _, _ = x.size()  # 获取输入x的批量大小b和通道数c
    y = self.avg_pool(x).view(b, c)  # 通过自适应平均池化层后，调整形状以匹配全连接层的输入
    y = self.fc(y).view(b, c, 1, 1)  # 通过全连接层计算通道重要性，调整形状以匹配原始特征图的形状


# --- Block 6 ---

return x * y.expand_as(x) # 将通道重要性系数应用到原始特征图上，进行特征重新校准


# --- Block 7 ---

if __name__ == '__main__':
    input = torch.randn(50, 512, 7, 7) # 随机生成一个输入特征图
    se = SEAttention(channel=512, reduction=8) # 实例化SE模块，设置降维比率为8
    output = se(input) # 将输入特征图通过SE模块进行处理
    print(output.shape) # 打印处理后的特征图形状，验证SE模块的作用
