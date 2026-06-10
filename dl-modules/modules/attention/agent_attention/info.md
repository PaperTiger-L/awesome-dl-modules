# Agent Attention

**论文**: [arxiv.org](https://arxiv.org/pdf/2312.08874v3)

## 模块简介

本文提出一种新型Transformer模型，它结合了Linear Attention和Softmax Attention的优点，在计算效率和表示能力之间取得良好的平衡。具体来说，Agent Attention，表示为四元组，在传统的Attention模块中引入了一组额外的Agent token A。Agent token首先作为Query token Q的代理，从K和V中聚合信息，然后将信息广播回Q。代理令牌的数量可以设计得比查询令牌的数量小得多，从而减少了时间复杂度。本文证明了所提出的代理注意等同于线性注意的广义形式。
