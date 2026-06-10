"""
注意：此代码提取自学术论文，MinerU PDF转换过程中可能丢失了部分缩进，
使用前请手动修复 class/def 内部的缩进问题。
原始论文代码通过后可正常运行，此处仅做模块结构参考。

fcanet - Python Implementation

Paper: FcaNet: Frequency Channel Attention Networks
Source: MinerU markdown extraction
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn import init
import numpy as np


# Fcanet: Frequency channel attention networks (ICCV 2021)
import math


# --- Block 2 ---

self.fc = nn.Sequential(
    nn.Linear(channel, channel // reduction, bias=False),
    nn.ReLU(),
    nn.Linear(channel // reduction, channel, bias=False),
    nn.Sigmoid()
)
self.avgpool = nn.AdaptiveAvgPool2d((self.dct_h, self.dct_w))

def forward(self, x):
    n, c, h, w = x.shape
    x_pooled = x
    if h != self.dct_h or w != self.dct_w:
    x_pooled = self.avgpool(x)
    # If you have concerns about one-line-change, don't worry. :)
    # In the ImageNet models, this line will never be triggered.
    # This is for compatibility in instance segmentation and object detection.
    y = self.dct_layer(x_pooled)

    y = self.fc(y).view(n, c, 1, 1)
    return x * y.expand_as(x)

class MultiSpectralDCTLayer(nn.Module):
    """
    Generate dct filters
    """

    def __init__(self, height, width, mapper_x, mapper_y, channel):
    super(MultiSpectralDCTLayer, self).__init__()

    assert len(mapper_x) == len(mapper_y)
    assert channel % len(mapper_x) == 0

    self.num_freq = len(mapper_x)

    # fixed DCT init
    self.weight = self.get_dct_filter(
    height, width, mapper_x, mapper_y, channel)

def forward(self, x):
    assert len(x.shape) == 4, 'x must been 4 dimensions, but got ' + \
    str(len(x.shape))
    # n, c, h, w = x.shape

    x = x * self.weight
    result = torch.sum(torch.sum(x, dim=2), dim=2)
    return result

def build_filter(self, pos, freq, POS):
    result = math.cos(math.pi * freq * (pos + 0.5) / POS) / math.sqrt(POS)
    if freq == 0:
    return result
    else:
    return result * math.sqrt(2)


# --- Block 3 ---

def get_dct_filter(self, tile_size_x, tile_size_y, mapper_x, mapper_y, channel):
    dct_filter = torch.zeros((channel, tile_size_x, tile_size_y))

    c_part = channel // len(mapper_x)

    for i, (u_x, v_y) in enumerate(zip(mapper_x, mapper_y)):
    for t_x in range(tile_size_x):
    for t_y in range(tile_size_y):
    dct_filter[i * c_part: (i + 1) * c_part, t_x, t_y] = self.build_filter(
    t_x, u_x, tile_size_x) * self.build_filter(t_y, v_y, tile_size_y)

    return dct_filter

# 输入 NCHW，输出 NCHW
if __name__ == '__main__':
    block = MultiSpectralAttentionLayer(64, 16, 16)
    input = torch.rand(1, 64, 64, 64)
    output = block(input)
    print(output.shape)
