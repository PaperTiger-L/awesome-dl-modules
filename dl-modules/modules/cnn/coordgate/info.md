# CoordGate

**论文**: CoordGate: Efficiently Computing Spatially-Varying Convolutions in Convolutional Neural Networks

**代码地址**: 未公开

## 模块简介

本文提出了CoordGate，一种新颖的轻量级模块，它通过使用乘法门和坐标编码网络，有效地计算卷积神经网络（CNN）中的空间变化卷积。CoordGate允许基于它们的空间位置选择性地放大或衰减过滤器，从而有效地像局部连接的神经网络一样行动。通过在U-Net架构中实施CoordGate，并将其应用于图像去模糊这一挑战性问题，实验结果表明CoordGate优于传统方法，为各种计算机视觉应用中的CNN提供了一个更加健壮且具有空间意识的解决方案。
