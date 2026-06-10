"""
注意：此代码提取自学术论文，MinerU PDF转换过程中可能丢失了部分缩进，
使用前请手动修复 class/def 内部的缩进问题。
原始论文代码通过后可正常运行，此处仅做模块结构参考。

深度可分离卷积 - Python Implementation

Paper: DeepLab V3
Source: MinerU markdown extraction
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn import init
import numpy as np


class DepthwiseSeparableConv(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size=3, stride=1, padding=1):
    super(DepthwiseSeparableConv, self).__init__()

    # 深度卷积层
    self.depthwise = nn.Sequential(nn.Conv2d(in_channels, in_channels, kernel_size,
    stride, padding,
    groups=in_channels),
    nn.BatchNorm2d(in_channels),
    # activation_layer
    nn.LeakyReLU(0.1, inplace=True)


# --- Block 2 ---

self.pointwise = nn.Sequential(nn.Conv2d(in_channels, out_channels, 1), nn.BatchNorm2d(out_channels), # activation_layer nn.LeakyReLU(0.1, inplace=True)


# --- Block 3 ---

x = self.depthwise(x)
x = self.pointwise(x)
return x
