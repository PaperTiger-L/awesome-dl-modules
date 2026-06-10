# AFFNet

**论文**: [arxiv.org](https://arxiv.org/pdf/2307.14008v1)

## 模块简介

AFFNet 设计了一种自适应频段过滤算子：Adaptive Frequency Filtering token mixer。视觉 Transformer，Large-Kernel CNN 和 MLP 在很多视觉任务上面都取得了成功，归功于它们的 token mixer 在全局范围内的信息融合。但是这些 token mixer 的成本较高，在移动设备上的高效部署存在一定的挑战。自适应频段过滤算子就是为了解决这个问题，它通过傅里叶变换 (Fourier transform) 将特征变换到频域，并利用下面关系在数学上的等价：  在频域中 "通过逐位置的乘法操作过滤不同频段的特征"。  在空域中 "用一个动态卷积核执行特征混合操作，卷积核的大小为特征的大小"。
