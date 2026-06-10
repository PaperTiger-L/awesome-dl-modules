# SCConv

**论文**: [openaccess.thecvf.com](https://openaccess.thecvf.com//content/CVPR2023/papers/Li_SCConv_Spatial_and_Channel_Reconstruction_Convolution_for_Feature_Redundancy_CVPR_2023_paper.pdf)

## 模块简介

本文作者提出了一种名为 SCConv（Spatial and Channel reconstruction Convolution, 空间和通道重建卷积）的卷积模块，目的是减少卷积神经网络中特征之间的空间和通道冗余，从而压缩CNN模型并提高其性能。  作者设计的 SCConv 模块，包含两个单元。一个名为 SRU (Spatial Reconstruction Unit, 空间重构单元) ，一个名为 CRU (Channel Reconstruction Unit, 通道重构单元) 。其中 SRU 通过 分离-重构方法 来减少空间冗余，CRU 则使用 分割-转换-融合方法 来减少通道冗余。这两个单元协同工作，以减少CNN中特征的冗余信息。  作者指出，SCConv 是一种可以直接替代标准卷积操作的插件式卷积模块 ，可以应用于各种卷积神经网络中，从而降低冗余特征并减少计算复杂性。
