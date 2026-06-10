# SCNet

**论文**: [openaccess.thecvf.com](https://openaccess.thecvf.com/content_CVPR_2020/papers/Liu_Improving_Convolutional_Networks_With_Self-Calibrated_Convolutions_CVPR_2020_paper.pdf)

## 模块简介

本文提出了一种新颖的自校正卷积，该卷积它可以通过特征的内在通信达到扩增卷积感受野的目的，进而增强输出特征的多样性。不同于标准卷积采用小尺寸核（例如3×3卷积）同时融合空间维度域与通道维度的信息，本文所设计的SCConv可以通过自校正操作自适应地在每个空间位置周围建立了远程空间和通道间依存关系。因此，它可以帮助CNN生成更具判别能力的特征表达，因其具有更丰富的信息
