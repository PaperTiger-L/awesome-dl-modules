# AutoFocusFormer

**论文**: [arxiv.org](https://arxiv.org/pdf/2304.12406v2)

## 模块简介

本文提出一种局部注意力 Transformer 图像识别 Backbone，即 AutoFocusFormer (AFF) 方法，执行自适应下采样来学习保留最重要的像素信息。由于自适应下采样会产生一些不规则的像素分布，因此放弃了经典的grid结构，而提出了一种新的基于点的局部注意力 block，由一个平衡聚类模块和一个可学习的聚类融合模块组成。实验表明 AFF 的性能很棒。
