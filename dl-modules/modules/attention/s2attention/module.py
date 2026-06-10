"""
注意：此代码提取自学术论文，MinerU PDF转换过程中可能丢失了部分缩进，
使用前请手动修复 class/def 内部的缩进问题。
原始论文代码通过后可正常运行，此处仅做模块结构参考。

S2Attention - Python Implementation

Paper: S2-MLPV2: IMPROVED SPATIAL-SHIFT MLP ARCHITECTURE FOR VISION
Source: MinerU markdown extraction
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn import init
import numpy as np



def spatial_shift1(x):
    # 实现第一种空间位移，位移图像的四分之一块
    b, w, h, c = x.size()
    # 以下四行代码分别向左、向右、向上、向下移动图像的四分之一块
    x[:, 1:, :, :c // 4] = x[:, :w - 1, :, :c // 4]
    x[:, :w - 1, :, c // 4:c // 2] = x[:, 1:, :, c // 4:c // 2]
    x[:, :, 1:, c // 2:c * 3 // 4] = x[:, :, :h - 1, c // 2:c * 3 // 4]
    x[:, :, :h - 1, 3 * c // 4:] = x[:, :, 1:, 3 * c // 4:]
    return x


# --- Block 2 ---

# 实现第二种空间位移，逻辑与spatial_shift1相似，但位移方向不同
b, w, h, c = x.size()
# 对图像的四分之一块进行空间位移
x[:, :, 1:, :c // 4] = x[:, :, :h - 1, :c // 4]
x[:, :, :h - 1, c // 4:c // 2] = x[:, :, 1:, c // 4:c // 2]
x[:, 1:, :, c // 2:c * 3 // 4] = x[:, :w - 1, :, c // 2:c * 3 // 4]
x[:, :w - 1, :, 3 * c // 4:] = x[:, 1:, :, 3 * c // 4:]
return x


# --- Block 3 ---

def __init__(self, channel=512, k=3):
    super().__init__()
    self.channel = channel
    self.k = k  # 分割的块数
    # 定义MLP层和激活函数
    self.mlp1 = nn.Linear(channel, channel, bias=False)
    self.gelu = nn.GELU()
    self.mlp2 = nn.Linear(channel, channel * k, bias=False)
    self.softmax = nn.softmax(1)

def forward(self, x_all):
    # 计算分割注意力，并应用于输入特征
    b, k, h, w, c = x_all.shape
    x_all = x_all.reshape(b, k, -1, c)  # 重塑维度
    a = torch.sum(torch.sum(x_all, 1), 1)  # 聚合特征
    hat_a = self.mlp2(self.gelu(self.mlp1(a)))  # 通过MLP计算注意力权重
    hat_a = hat_a.reshape(b, self.k, c)  # 调整形状
    bar_a = self.softmax(hat_a)  # 应用softmax获取注意力分布
    attention = bar_a.unsqueeze(-2)  # 增加维度
    out = attention * x_all  # 将注意力权重应用于特征
    out = torch.sum(out, 1).reshape(b, h, w, c)  # 聚合并调整形状
    return out


# --- Block 4 ---

def __init__(self, channels=512):
    super().__init__()
# 定义MLP层
self.mlp1 = nn.Linear(channels, channels * 3)
self.mlp2 = nn.Linear(channels, channels)
self.split_attention = SplitAttention()


# --- Block 5 ---

b, c, w, h = x.size()
x = x.permute(0, 2, 3, 1) # 调整维度顺序
x = self.mlp1(x) # 通过MLP层扩展特征
x1 = spatial_shift1(x[:, :, :, :c]) # 应用第一种空间位移
x2 = spatial_shift2(x[:, :, :, c:c * 2]) # 应用第二种空间位移
x3 = x[:, :, :, c * 2:] # 保留原始特征的一部分
x_all = torch.stack([x1, x2, x3], 1) # 堆叠特征
a = self.split_attention(x_all) # 应用分割注意力
x = self.mlp2(a) # 通过另一个MLP层缩减特征维度
x = x.permute(0, 3, 1, 2) # 调整维度顺序回原始
return x


# --- Block 6 ---

if __name__ == '__main__':
    input = torch.randn(50, 512, 7, 7) # 创建输入张量
    s2att = s2Attention(channels=512) # 实例化s2注意力模块
    output = s2att(input) # 通过s2注意力模块处理输入
    print(output.shape) # 打印输出张量的形状
