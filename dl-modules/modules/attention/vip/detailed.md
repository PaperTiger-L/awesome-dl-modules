# ViP - 详细讲解

> 论文: VISION PERMUTATOR: A PERMUTABLE MLP-LIKE ARCHITECTURE FOR VISUALRECOGNITION

## 1、作用

论文提出的Vision Permutator是一种简单、数据高效的类MLP（多层感知机）架构，用于视觉识别。不同于其他MLP类模型，它通过线性投影分别对特征表示在高度和宽度维度进行编码，能够保留2D特征表示中的位置信息，有效捕获沿一个空间方向的长距离依赖关系，同时保留另一方向上的精确位置信息。

## 2、机制

### 1、视觉置换器：

Vision Permutator采用与视觉变换器类似的令牌化操作，将输入图像均匀划分为小块，并通过线性投影将它们映射为令牌嵌入。随后，这些令牌嵌入被送入一系列Permutator块中进行特征编码。

### 2、Permute-MLP：

Permutator块包含一个用于空间信息编码的Permute-MLP和一个用于通道信息混合的Channel-MLP。Permute-MLP通过独立处理令牌表示沿高度和宽度的维度，生成具有特定方向信息的令牌，这对于视觉识别至关重要。

### 3、加权Permute-MLP：

在简单的Permute-MLP基础上，引入加权Permute-MLP来重新校准不同分支的重要性，进一步提高模型性能。

## 3、独特优势

### 1、空间信息编码：

Vision Permutator通过在高度和宽度维度上分别对特征进行编码，相比于其他将两个空间维度混合为一个进行处理的MLP类模型，能够更有效地保留空间位置信息，从而提高模型对图像中对象的识别能力。

### 2、性能提升：

实验表明，即使在不使用额外大规模训练数据的情况下，Vision Permutator也能达到81.5%的ImageNet顶级-1准确率，并且仅使用25M可学习参数，这比大多数同等大小模型的CNNs和视觉变换器都要好。

### 3、模型高效：

Vision Permutator的结构简单、数据高效，在确保高准确性的同时提高了训练和推理速度，展现了MLP类模型在视觉识别任务中的潜力。

---

> 代码文件: [module.py](module.py)
