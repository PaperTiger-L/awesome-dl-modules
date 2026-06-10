"""
注意：此代码提取自学术论文，MinerU PDF转换过程中可能丢失了部分缩进，
使用前请手动修复 class/def 内部的缩进问题。
原始论文代码通过后可正常运行，此处仅做模块结构参考。

可变性卷积 - Python Implementation

Paper: InternImage: Exploring Large-Scale Vision Foundation Models with DeformableConvolutions
Source: MinerU markdown extraction
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn import init
import numpy as np



class DeformConv2d(nn.Module):
    def __init__(self, inc, outc, kernel_size=3, padding=1, stride=1, bias=None, modulation=False):
    """
    Args:
    moduleation(bool, optional): If True, Modulated Defromable Convolution(Deformable ConvNets v2).


# --- Block 2 ---

"""
super(DeformConv2d, self).__init__()
self.kernel_size = kernel_size
self.padding = padding
self.stride = stride
self.zero_padding = nn.ZeroPad2d(padding)
self.conv = nn.Conv2d(inc, outc, kernel_size=kernel_size,
stride=kernel_size, bias=bias)

# self.p_conv偏置层，学习公式（2）中的偏移量。
# 2*kernel_size*kernel_size: 代表了卷积核中所有元素的偏移坐标，因为同时存在x和y的偏移，故要乘以2。
self.p_conv = nn.Conv2d(inc, 2 * kernel_size * kernel_size,
kernel_size=3, padding=1, stride=stride)
nn.init.constant_(self.p_conv.weight, 0)
# register_backward_hook是为了方便查看这几层学出来的结果，对网络结构无影响。
self.p_conv.register_backward_hook(self._set_lr)

self.modulation = modulation
if modulation:
    # self.m_conv权重学习层，是后来提出的第二个版本的卷积也就是公式（3）描述的卷积。
    # kernel_size*kernel_size: 代表了卷积核中每个元素的权重。
    self.m_conv = nn.Conv2d(inc, kernel_size * kernel_size,
kernel_size=3, padding=1, stride=stride)
    nn.init.constant_(self.m_conv.weight, 0)
    # register_backward_hook是为了方便查看这几层学出来的结果，对网络结构无影响。
    self.m_conv.register_backward_hook(self._set_lr)

@staticmethod
def _set_lr(module, grad_input, grad_output):
    grad_input = (grad_input[i] * 0.1 for i in range(len(grad_input)))
    grad_output = (grad_output[i] * 0.1 for i in range(len(grad_output)))

# 生成卷积核的邻域坐标
def _get_p_n(self, N, dtype):
    """
    torch.meshgrid():Creates grids of coordinates specified by the 1D inputs
in attr:tensors.
    功能是生成网格，可以用于生成坐标。
    函数输入两个数据类型相同的一维张量，两个输出张量的行数为第一个输入张量的元素个数，
    列数为第二个输入张量的元素个数，当两个输入张量数据类型不同或维度不是一维时会报错。

其中第一个输出张量填充第一个输入张量中的元素，各行元素相同；
第二个输出张量填充第二个输入张量中的元素各列元素相同。


# --- Block 3 ---




# --- Block 4 ---




# --- Block 5 ---

# 双线性插值公式里的四个系数。即bilinear kernel。

# 作者代码为了保持整齐，每行的变量计算形式一样，所以计算需要做一点对应变量的对应变化。


# --- Block 6 ---

# 计算双线性插值的四个坐标对应的像素值。


# --- Block 7 ---

# 双线性插值的最后计算
