# GhostNet

**论文**: [arxiv.org](https://arxiv.org/pdf/1911.11907v2)

## 模块简介

GhostNet是一种轻量级的深度学习模型，通过GhostModule和GhostBottleNeck实现高效特征提取。GhostModule通过1x1卷积和深度可分离卷积生成更多特征图，减少参数量。GhostBottleNeck则是GhostModule的瓶颈结构，用于构建网络深度。GhostNet适用于资源有限的场景，如移动设备上的图像分类任务。
