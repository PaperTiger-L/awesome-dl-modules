# PSA

**论文**: [arxiv.org](https://arxiv.org/pdf/2107.00782v2)

## 模块简介

作者提出了一个即插即用的模块——极化自注意力机制（ Polarized Self-Attention(PSA)），用于解决像素级的回归任务，相比于其他注意力机制，极化自注意力机制主要有两个设计上的亮点：  1）极化滤波（ Polarized filtering）：在通道和空间维度保持比较高的resolution（在通道上保持C/2的维度，在空间上保持\[H,W\]的维度 ），这一步能够减少降维度造成的信息损失；  2）增强（Enhancement）：采用细粒度回归输出分布的非线性函数。
