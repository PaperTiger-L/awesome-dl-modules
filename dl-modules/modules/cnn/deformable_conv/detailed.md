# 可变性卷积 - 详细讲解

> 论文: InternImage: Exploring Large-Scale Vision Foundation Models with DeformableConvolutions

## 1、作用

该文档介绍了一种基于卷积神经网络（CNNs）的大规模视觉基础模型，名为InternImage。与近年来取得巨大进展的大规模视觉变换器（ViTs）不同，基于CNN的大规模模型仍处于早期阶段。InternImage通过采用可变形卷积作为核心运算符，不仅具有执行下游任务（如检测和分割）所需的大有效接收场，而且还能够根据输入和任务信息进行自适应空间聚合。

## 2、机制

InternImage利用可变形卷积（DCN），与传统CNN采用的大密集核心运算符不同，它是一种动态稀疏卷积，采用通常的3x3窗口大小。这使得模型能够从给定数据中动态学习合适的接收字段（可为长程或短程），并根据输入数据自适应调整采样偏移和调制标量，类似于ViTs，减少了常规卷积的过度归纳偏置。

## 3、独特优势

InternImage通过上述设计，可以高效地扩展到大规模参数，并从大规模训练数据中学习更强大的表示，从而在包括ImageNet、COCO和ADE20K在内的具有挑战性的基准测试中证明了模型的有效性。值得一提的是，InternImage-H在COCO test-dev上创造了新纪录，达到了65.4 mAP，在ADE20K上达到了62.9mIoU，超越了当前领先的CNN和ViTs。

---

> 代码文件: [module.py](module.py)
