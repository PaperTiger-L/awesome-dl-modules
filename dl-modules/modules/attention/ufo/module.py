"""
注意：此代码提取自学术论文，MinerU PDF转换过程中可能丢失了部分缩进，
使用前请手动修复 class/def 内部的缩进问题。
原始论文代码通过后可正常运行，此处仅做模块结构参考。

UFO - Python Implementation

Paper: UFO-ViT: High Performance Linear Vision Transformer without Softmax
Source: MinerU markdown extraction
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn import init
import numpy as np


from torch.functional import norm


# --- Block 2 ---

def XNorm(x, gamma):
    norm_tensor = torch.norm(x, 2, -1, True)
    return x * gamma / norm_tensor


# --- Block 3 ---

# UFOAttention类继承自nn.Module
class UFOAttention(nn.Module):


# --- Block 4 ---

def __init__(self, d_model, d_k, d_v, h, dropout=.1):
    '''
    :param d_model: 模型的维度
    :param d_k: 查询和键的维度
    :param d_v: 值的维度
    :param h: 注意力头数
    '''
    super(UFOAttention, self).__init__()
# 初始化四个线性层：为查询、键、值和输出转换使用
self.fc_q = nn.Linear(d_model, h * d_k)
self.fc_k = nn.Linear(d_model, h * d_k)
self.fc_v = nn.Linear(d_model, h * d_v)
self.fc_o = nn.Linear(h * d_v, d_model)
self.dropout = nn.Dropout(dropout)
# gamma参数用于规范化
self.gamma = nn.Parameter(torch.randn((1, h, 1, 1)))

self.d_model = d_model
self.d_k = d_k
self.d_v = d_v
self.h = h

self.init_weights()


# --- Block 5 ---

def init_weights(self):
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


# --- Block 6 ---

def forward(self, queries, keys, values):
    b_s, nq = queries.shape[:2]
    nk = keys.shape[1]


# --- Block 7 ---

# 通过线性层将查询、键、值映射到新的空间
q = self.fc_q(queries).view(b_s, nq, self.h, self.d_k).permute(0, 2, 1, 3)
k = self.fc_k(keys).view(b_s, nk, self.h, self.d_k).permute(0, 2, 3, 1)
v = self.fc_v(values).view(b_s, nk, self.h, self.d_v).permute(0, 2, 1, 3)

# 计算键和值的乘积，然后对结果进行规范化
kv = torch.matmul(k, v) # bs,h,c,c
kv_norm = XNorm(kv, self.gamma) # bs,h,c,c
q_norm = XNorm(q, self.gamma) # bs,h,n,c
out = torch.matmul(q_norm, kv_norm).permute(0, 2, 1, 3).contiguous().view(b_s, nq, self.h * self.d_v)
out = self.fc_o(out) # (b_s, nq, d_model)

return out

if __name__ == '__main__':
    # 示例用法
    block = UFOAttention(d_model=512, d_k=512, d_v=512, h=8).cuda()
    input = torch.rand(64, 64, 512).cuda()
    output = block(input, input, input)
    print(output.shape)
