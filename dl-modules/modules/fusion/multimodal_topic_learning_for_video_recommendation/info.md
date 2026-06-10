# Multimodal Topic Learning for Video Recommendation

**论文**: [arxiv.org](https://arxiv.org/pdf/2010.13373v1)

**代码地址**: > 模块简介：模型架构上半部分是普通推荐架构。使用视频的封面图和标题在经典多任务模型的MMoE架构下做优化。下半部分是topic生成。左边是构建标签图找标签之间的关系得到表示，然后使用视频的相应tag和封面，标题信息一起构成视频特征，然后用k-means做聚类生成topic

## 模块简介

模型架构上半部分是普通推荐架构。使用视频的封面图和标题在经典多任务模型的MMoE架构下做优化。下半部分是topic生成。左边是构建标签图找标签之间的关系得到表示，然后使用视频的相应tag和封面，标题信息一起构成视频特征，然后用k-means做聚类生成topic
