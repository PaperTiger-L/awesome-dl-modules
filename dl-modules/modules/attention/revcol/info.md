# RevCol

**论文**: [arxiv.org](https://arxiv.org/pdf/2212.11696v3)

## 模块简介

提出以 reversible column 为单元来传递信息，既保证特征解耦，同时信息在网络中的传递不受到损失。整个网络结构包括了多个子网络（我们称为 column），column 间加入可逆的连接，通过将输入反复接入 column，逐渐分离 low-level 的纹理细节和 semantic 语义信息
