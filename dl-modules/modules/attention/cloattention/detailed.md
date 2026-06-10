# Cloattention - 详细讲解

> 论文: Rethinking Local Perception in Lightweight Vision Transformer

## 1、作用

CloFormer（Context-aware Local Enhancement Vision Transformer）是一种轻量级的视觉Transformer，用于在保持模型轻量化的同时，提高在各种视觉任务中的性能，包括图像分类、目标检测和语义分割。其主要目的是提升移动设备上的视觉模型性能，克服直接缩减标准ViT（VisionTransformer）模型尺寸导致的性能下降问题。

## 2、机制

CloFormer通过引入AttnConv（Attention Style Convolution Operator）来实现上下文感知的局部增强，从而有效捕获高频局部信息。该模型采用两分支结构：

### 1、局部分支：

利用AttnConv融合共享权重和上下文感知权重来聚合高频局部信息。首先，使用深度可分离卷积（Depthwise Convolution，DWconv）提取局部表示，然后部署上下文感知权重来增强局部特征。

### 2、全局分支：

采用标准的注意力机制，通过对K和V进行下采样来降低FLOPs，帮助模型捕捉低频全局信息。

## 3、独特优势

### 1、上下文感知的局部增强：

通过AttnConv，CloFormer有效地结合了共享权重和上下文感知权重的优势，实现了高质量的局部特征增强。

### 2、两分支结构：

通过同时捕获高频和低频信息，模型能够在不同的视觉任务中达到更好的性能。

### 3、轻量化设计：

CloFormer专为移动设备设计，通过精心的模型架构设计和权重共享机制，实现了在保持轻量化的同时提高模型性能。

---

> 代码文件: [module.py](module.py)
