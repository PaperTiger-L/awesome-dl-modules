"""
注意：此代码提取自学术论文，MinerU PDF转换过程中可能丢失了部分缩进，
使用前请手动修复 class/def 内部的缩进问题。
原始论文代码通过后可正常运行，此处仅做模块结构参考。

AFT - Python Implementation

Paper: An Attention Free Transformer
Source: MinerU markdown extraction
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn import init
import numpy as np



class AFT_FULL(nn.Module):
    # 初始化AFT_FULL模块
    def __init__(self, d_model, n=49, simple=False):
    super(AFT_FULL, self).__init__()
    # 定义QKV三个线性变换层
    self.fc_q = nn.Linear(d_model, d_model)
    self.fc_k = nn.Linear(d_model, d_model)
    self.fc_v = nn.Linear(d_model, d_model)
    # 根据simple参数决定位置偏置的初始化方式
    if (simple):
    self.position_biases = torch.zeros((n, n))  # 简单模式下为零矩阵
    else:
    self.position_biases = nn.Parameter(torch.ones((n, n)))  # 非简单模式下为可学习的参数
    self.d_model = d_model
    self.n = n  # 输入序列的长度
    self.sigmoid = nn.Sigmoid()  # 使用Sigmoid函数
    self.init_weights()  # 初始化模型权重


# --- Block 2 ---

def init_weights(self):
    # 对模块中的参数进行初始化
    for m in self.modules():
    if isinstance(m, nn.Conv2d):
    init.kaiming_normal_(m.weight, mode='fan_out')
    if m.bias is not None:
    init.constant_(m.bias, 0)
    elif isinstance(m, nn.BatchNorm2d):
    init.constant_(m.weight, 1)
    init.constant_(m.bias, 0)
    elif isinstance(m, nn.Linear):
    init.normal_(m.weight, std=0.001)
    if m.bias is not None:
    init.constant_(m.bias, 0)

def forward(self, input):
    bs, n, dim = input.shape  # 输入的批大小、序列长度和特征维度

    # 通过QKV变换生成查询、键和值
    q = self.fc_q(input)  # bs, n, dim
    k = self.fc_k(input).view(1, bs, n, dim)  # 1, bs, n, dim，为了后续运算方便
    v = self.fc_v(input).view(1, bs, n, dim)  # 1, bs, n, dim

    # 使用位置偏置和键值对进行加权求和
    numerator = torch.sum(torch.exp(k + self.position_biases.view(n, 1, -1, 1)) * v, dim=2)  # n, bs, dim
    denominator = torch.sum(torch.exp(k + self.position_biases.view(n, 1, -1, 1)), dim=2)  # n, bs, dim

    # 计算加权求和的结果，并通过sigmoid函数调制查询向量
    out = (numerator / denominator)  # n, bs, dim
    out = self.sigmoid(q) * (out.permute(1, 0, 2))  # bs, n, dim，最后将结果重新排列

    return out

# 示例使用
if __name__ == '__main__':
    block = AFT_FULL(d_model=512, n=64).cuda()
    input = torch.rand(64, 64, 512).cuda()
    output = block(input)
    print(output.shape)
