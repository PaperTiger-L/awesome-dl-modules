# Low-rank-Multimodal-Fusion

**论文**: [arxiv.org](https://arxiv.org/pdf/1806.00064v1)

## 模块简介

为了解决基于张量的多模态融合方法计算效率差的问题，文章提出了一种低秩多模态融合的方法(Low-rank Multimodal Fusion, LMF)的方法。通过将张量和权重并行分解，利用模态特定的低阶因子来执行多模态融合。避免计算高维的张量，降低了内存开销，将指数级的时间复杂度降低到了线性。
