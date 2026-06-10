"""
注意：此代码提取自学术论文，MinerU PDF转换过程中可能丢失了部分缩进，
使用前请手动修复 class/def 内部的缩进问题。
原始论文代码通过后可正常运行，此处仅做模块结构参考。

空洞卷积 - Python Implementation

Paper: MULTI-SCALE CONTEXT AGGREGATION BY DILATED CONVOLUTIONS
Source: MinerU markdown extraction
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn import init
import numpy as np



# 定义一个包含空洞卷积、批量归一化和ReLU激活函数的子模块
class ASPPConv(nn.Sequential):
    def __init__(self, in_channels, out_channels, dilation):
    modules = [
    # 空洞卷积，通过调整dilation参数来捕获不同尺度的信息
    nn.Conv2d(in_channels, out_channels, 3, padding=dilation, dilation=dilation, bias=False),
    nn.BatchNorm2d(out_channels), # 批量归一化
    nn.ReLU()  # ReLU激活函数
    ]
    super(ASPPConv, self).__init__(*modules)


# --- Block 2 ---

class ASPPPooling(nn.Sequential):
    def __init__(self, in_channels, out_channels):
    super(ASPPPooling, self).__init__(nn.AdaptiveAvgPool2d(1), # 全局平均池化
    nn.Conv2d(in_channels, out_channels, 1, bias=False), # 1x1卷积
    nn.BatchNorm2d(out_channels), # 批量归一化
    nn.ReLU()) # ReLU激活函数

def forward(self, x):
    size = x.shape[-2:] # 保存输入特征图的空间维度
    x = super(ASPPPooling, self).forward(x)
    # 通过双线性插值将特征图大小调整回原始输入大小
    return F.interpolate(x, size=size, mode='bilinear', align_corners=False)


# --- Block 3 ---

class ASPP(nn.Module):
    def __init__(self, in_channels, atrous_rates):
    super(ASPP, self).__init__()
    out_channels = 256 # 输出通道数
    modules = []
    modules.append(nn.Sequential(
    nn.Conv2d(in_channels, out_channels, 1, bias=False), # 1x1卷积用于降维
    nn.BatchNorm2d(out_channels),
    nn.ReLU()))


# --- Block 4 ---

for rate in atrous_rates:
modules.append(ASPPConv(in_channels, out_channels, rate))


# --- Block 5 ---

modules.append(ASPPPooling(in_channels, out_channels))


# --- Block 6 ---

self.convs = nn.ModuleList(modules)


# --- Block 7 ---

self.project = nn.Sequential(
    nn.Conv2d(5 * out_channels, out_channels, 1, bias=False), # 融合特征后
降维


# --- Block 8 ---

def forward(self, x):
    res = []
    # 对每个模块的输出进行收集
    for conv in self.convs:
    res.append(conv(x))


# --- Block 9 ---

res = torch.cat(res, dim=1)


# --- Block 10 ---

return self.project(res)


# --- Block 11 ---

# 示例使用ASPP模块
aspp = ASPP(256, [6, 12, 18])
x = torch.rand(2, 256, 13, 13)
print(aspp(x).shape) # 输出处理后的特征图维度
