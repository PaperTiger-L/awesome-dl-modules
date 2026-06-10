# Dynamic Convolution

**论文**: [arxiv.org](https://arxiv.org/pdf/1912.03458v2)

## 模块简介

轻量级卷积神经网络（light-weight convolutional neural network）因其较低的计算预算而限制了 CNN 的深度（卷积层数）和宽度（通道数），不仅导致模型性能下降，表示能力也会受到限制。为了解决这个问题，微软的研究员们提出了动态卷积，这种新的设计能够在不增加网络深度或宽度的情况下增加模型的表达能力（representation capacity）。动态卷积的基本思路就是根据输入图像，自适应地调整卷积参数。（所得卷积核与输入相关，即不同数据具有不同的卷积，这也就是动态卷积的由来。）
