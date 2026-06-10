# FastICENet

**论文**: [www.sciencedirect.com](https://www.sciencedirect.com/science/article/abs/pii/S0165168423002244)

## 模块简介

本文提出了一种实时、准确的河冰语义分割网络，命名为FastICENet。 总体架构由两个分支组成，即浅层高分辨率空间分支和深层上下文语义分支，针对遥感图像中河冰的尺度多样性和不规则形状进行了精心设计。 然后，在上下文分支中采用新颖的下采样模块和基于轻量级Ghost模块的密集连接块来降低计算成本。 此外，采用可学习的上采样策略DUpsampling来代替常用的双线性插值，以提高分割精度。
