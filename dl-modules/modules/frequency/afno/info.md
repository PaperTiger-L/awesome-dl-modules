# AFNO模块

**论文**: [arxiv.org](https://arxiv.org/pdf/2111.13587v2)

## 模块简介

本文提出了一种借助傅里叶变换的高效 token mixer，AFNO。模型可以灵活地适应输入分辨率的变化，并且随着输入分辨率的增加呈 quasi-linear 增长。AFNO 通过对复数权重进行分块操作，一方面融合不同 channel 的信息，另一方面控制参数量的增
