# UniRepLKNet

**论文**: [arxiv.org](https://arxiv.org/pdf/2311.15599v2)

## 模块简介

用于大核CNN架构设计的四条guideline，一种名为UniRepLKNet的强力backbone（只用ImageNet-22K预训练，精度和速度SOTA，ImageNet达到88%, COCO达到56.4 box AP，ADE20K达到55.6 mIoU，实际测速优势很大），在时序预测的超大数据上用这一为图像设计的backbone达到SOTA水平（全球气温和风速预测，前SOTA是发在Nature子刊上专门为此设计的Transformer），在点云、音频、视频上凭着极为简单的预处理方式和毫无改变的模型结构均超过或接近SOTA水平。
