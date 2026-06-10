"""
注意：此代码提取自学术论文，MinerU PDF转换过程中可能丢失了部分缩进，
使用前请手动修复 class/def 内部的缩进问题。
原始论文代码通过后可正常运行，此处仅做模块结构参考。

CrissCrossAttention - Python Implementation

Paper: CROSSFORMER: A VERSATILE VISION TRANSFORMER HINGING ON CROSS-SCALEATTENTION
Source: MinerU markdown extraction
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn import init
import numpy as np


from torch.nn import Softmax

# 定义一个无限小的矩阵，用于在注意力矩阵中屏蔽特定位置
def INF(B, H, W):
    return -torch.diag(torch.tensor(float("inf")).repeat(H), 0).unsqueeze(0).repeat(B * W, 1, 1)

class CrissCrossAttention(nn.Module):
    """Criss-Cross Attention Module"""
    def __init__(self, in_dim):
    super(CrissCrossAttention, self).__init__()
    # Q, K, V转换层
    self.query_conv = nn.Conv2d(in_channels=in_dim, out_channels=in_dim // 8, kernel_size=1)
    self.key_conv = nn.Conv2d(in_channels=in_dim, out_channels=in_dim // 8, kernel_size=1)


# --- Block 2 ---

self.value_conv = nn.Conv2d(in_channels=in_dim, out_channels=in_dim, kernel_size=1)
    # 使用softmax对注意力分数进行归一化
    self.softmax = Softmax(dim=3)
    self.INF = INF
    # 学习一个缩放参数，用于调节注意力的影响
    self.gamma = nn.Parameter(torch.zeros(1))

def forward(self, x):
    m_batchsize, _, height, width = x.size()
    # 计算查询(Q)、键(K)、值(V)矩阵
    proj_query = self.query_conv(x)
    proj_query_H = proj_query.permute(0, 3, 1, 2).contiguous().view(m_batchsize * width, -1, height).permute(0, 2, 1)
    proj_query_W = proj_query.permute(0, 2, 1, 3).contiguous().view(m_batchsize * height, -1, width).permute(0, 2, 1)

    proj_key = self.key_conv(x)
    proj_key_H = proj_key.permute(0, 3, 1, 2).contiguous().view(m_batchsize * width, -1, height)
    proj_key_W = proj_key.permute(0, 2, 1, 3).contiguous().view(m_batchsize * height, -1, width)

    proj_value = self.value_conv(x)
    proj_value_H = proj_value.permute(0, 3, 1, 2).contiguous().view(m_batchsize * width, -1, height)
    proj_value_W = proj_value.permute(0, 2, 1, 3).contiguous().view(m_batchsize * height, -1, width)


# --- Block 3 ---

energy_H = (torch.bmm(proj_query_H, proj_key_H) + self.INF(m_batchsize, height, width)).view(m_batchsize, width, height, height).permute(0, 2, 1, 3)
energy_W = torch.bmm(proj_query_W, proj_key_W).view(m_batchsize, height, width, width)


# --- Block 4 ---

concatate = self.softmax(torch.cat([energy_H, energy_W], 3))


# --- Block 5 ---

att_H = concatenate[:, :, :, 0:height].permute(0, 2, 1, 3).contiguous().view(m_batchsize * width, height, height)
att_W = concatenate[:, :, :, height:height + width].contiguous().view(m_batchsize * height, width, width)


# --- Block 6 ---

out_H = torch.bmm(proj_value_H, att_H.permute(0, 2, 1)).view(m_batchsize, width, -1, height).permute(0, 2, 3, 1)
out_W = torch.bmm(proj_value_W, att_W.permute(0, 2, 1)).view(m_batchsize, height, -1, width).permute(0, 2, 1, 3)

return self.gamma * (out_H + out_W) + x


# --- Block 7 ---

if __name__ == '__main__':
    block = CrissCrossAttention(64)
    input = torch.rand(1, 64, 64, 64)
    output = block(input)


# --- Block 8 ---

print(output.shape)
