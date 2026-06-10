# Rethinking Atrous Convolution for Semantic Image Segmentation

**论文**: [arxiv.org](https://arxiv.org/pdf/1706.05587v3)

## 模块简介

DeepLab系列在分割领域一直很受欢迎，知名度很高。单看DeepLabV3，其实真正的创新点没有前两篇丰富，没有增加新的模块，而是针对于前两个版本做了一下升华和总结。在文中作者也说了，为什么能在不加DenseCRF后处理的情况下超越前几个版本的性能，两点：1）Batch Normalization的引入；2）ASPP模块的探索，加入了image-level的特征。其实，我觉得本文主要的亮点在于对Atrous Convolution并行/串行两种应用方式的探索。从这个系列来看，DeepLabV1、V2工作很novelty，并且能达到不错的performance；V3其实在前面的工作上增加了一些小的点（batch normalization 和 Image-level feature），但很work。虽然novelty的工作很少，但是奈何performance牛逼啊，然后写作上注重消融实验。学术创新不易啊~
