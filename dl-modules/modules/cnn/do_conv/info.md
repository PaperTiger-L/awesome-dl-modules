# DO-Conv

**论文**: [arxiv.org](https://arxiv.org/pdf/2006.12030v1)

## 模块简介

在这篇文章中，作者通过在一个普通的卷积层中加入额外的depthwise卷积操作，构成一个over-parameterized的卷积层，并将其命名为DO-Conv，通过实验证明，使用DO-Conv不仅能够加速网络的训练过程，还能在多种计算机视觉任务中取得比使用传统卷积层更好的结果。在推理时，DO-Conv可以转换为传统的卷积操作，因此将一个网络中的传统卷积替换为DO-Conv并不会增加计算需求。
