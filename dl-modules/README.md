# 深度学习即插即用模块库

> 总计 123 个模块 | 来源: 阿文整理 (89) + MinerU详解 (45) - 重叠合并 (~10)
> 其中: 10 个模块有完整图文+代码, 79 个仅有图文, 34 个仅有详解+代码

---

## 分类概览

| 分类 | 模块数 | 说明 |
|------|--------|------|
| [Mamba系列模块](#mamba) | 5 | |
| [卷积（CNN）系列模块](#cnn) | 25 | |
| [频域系列模块](#frequency) | 10 | |
| [特征融合系列模块](#fusion) | 13 | |
| [下采样系列模块](#downsampling) | 8 | |
| [注意力系列模块](#attention) | 46 | |
| [时间序列模块](#timeseries) | 16 | |

---

## Mamba系列模块

| # | 模块 | 论文 | 图片 | 简介 | 详解 | 代码 |
|---|------|------|------|------|------|------|
| 1 | ConvSSM | [论文](https://arxiv.org/pdf/2310.19694v1) | [图片](modules/mamba/convssm/overview.png) | [简介](modules/mamba/convssm/info.md) | - | - |
| 2 | MambaIR | [论文](https://arxiv.org/pdf/2402.15648v3) | [图片](modules/mamba/mambair/overview.png) | [简介](modules/mamba/mambair/info.md) | - | - |
| 3 | MambaTab | [论文](https://arxiv.org/html/2401.08867v1) | [图片](modules/mamba/mambatab/overview.png) | [简介](modules/mamba/mambatab/info.md) | - | - |
| 4 | nnMamba | [论文](https://arxiv.org/pdf/2402.03526v2) | [图片](modules/mamba/nnmamba/overview.png) | [简介](modules/mamba/nnmamba/info.md) | - | - |
| 5 | ZigMa | [论文](https://arxiv.org/pdf/2403.13802v3) | [图片](modules/mamba/zigma/overview.png) | [简介](modules/mamba/zigma/info.md) | - | - |

---

## 卷积（CNN）系列模块

| # | 模块 | 论文 | 图片 | 简介 | 详解 | 代码 |
|---|------|------|------|------|------|------|
| 1 | ACNet | [论文](https://arxiv.org/pdf/1908.03930v3) | [图片](modules/cnn/acnet/overview.png) | [简介](modules/cnn/acnet/info.md) | - | - |
| 2 | AKConv | [论文](https://arxiv.org/pdf/2311.11587v1) | [图片](modules/cnn/akconv/overview.png) | [简介](modules/cnn/akconv/info.md) | - | - |
| 3 | CondConv | [论文](https://arxiv.org/pdf/1904.04971v3) | [图片](modules/cnn/condconv/overview.png) | [简介](modules/cnn/condconv/info.md) | - | - |
| 4 | CoordGate | CoordGate: Efficiently Computing Spatially-Varying Convolutions in Convolutional Neural Networks | [图片](modules/cnn/coordgate/overview.png) | [简介](modules/cnn/coordgate/info.md) | - | - |
| 5 | DCNv4 | [论文](https://arxiv.org/pdf/2401.06197v1) | [图片](modules/cnn/dcnv4/overview.png) | [简介](modules/cnn/dcnv4/info.md) | - | - |
| 6 | DO-Conv | [论文](https://arxiv.org/pdf/2006.12030v1) | [图片](modules/cnn/do_conv/overview.png) | [简介](modules/cnn/do_conv/info.md) | - | - |
| 7 | Drop an Octave | [论文](https://arxiv.org/pdf/1904.05049v3) | [图片](modules/cnn/drop_an_octave/overview.png) | [简介](modules/cnn/drop_an_octave/info.md) | - | - |
| 8 | Dynamic Convolution | [论文](https://arxiv.org/pdf/1912.03458v2) | [图片](modules/cnn/dynamic_convolution/overview.png) | [简介](modules/cnn/dynamic_convolution/info.md) | - | - |
| 9 | EfficientMod | [论文](https://arxiv.org/pdf/2403.19963v1) | [图片](modules/cnn/efficientmod/overview.png) | [简介](modules/cnn/efficientmod/info.md) | - | - |
| 10 | GhostNet | [论文](https://arxiv.org/pdf/1911.11907v2) | [图片](modules/cnn/ghostnet/overview.png) | [简介](modules/cnn/ghostnet/info.md) | - | - |
| 11 | HetConv | [论文](https://arxiv.org/pdf/1903.04120v2) | [图片](modules/cnn/hetconv/overview.png) | [简介](modules/cnn/hetconv/info.md) | - | - |
| 12 | Involution | [论文](https://arxiv.org/pdf/2103.06255v2) | [图片](modules/cnn/involution/overview.png) | [简介](modules/cnn/involution/info.md) | - | - |
| 13 | KernelWarehouse | [论文](https://arxiv.org/pdf/2308.08361v1) | [图片](modules/cnn/kernelwarehouse/overview.png) | [简介](modules/cnn/kernelwarehouse/info.md) | - | - |
| 14 | ODConv | [论文](https://arxiv.org/pdf/2209.07947v1) | [图片](modules/cnn/odconv/overview.png) | [简介](modules/cnn/odconv/info.md) | - | - |
| 15 | RefConv | [论文](https://arxiv.org/pdf/2310.10563v1) | [图片](modules/cnn/refconv/overview.png) | [简介](modules/cnn/refconv/info.md) | - | - |
| 16 | ResNeSt | [论文](https://arxiv.org/pdf/2004.08955v2) | [图片](modules/cnn/resnest/overview.png) | [简介](modules/cnn/resnest/info.md) | [详解](modules/cnn/resnest/detailed.md) | [代码](modules/cnn/resnest/module.py) |
| 17 | Run, Don't Walk | [论文](https://arxiv.org/pdf/2303.03667) | [图片](modules/cnn/run_don_t_walk/overview.png) | [简介](modules/cnn/run_don_t_walk/info.md) | [详解](modules/cnn/run_don_t_walk/detailed.md) | [代码](modules/cnn/run_don_t_walk/module.py) |
| 18 | SCConv | [论文](https://openaccess.thecvf.com//content/CVPR2023/papers/Li_SCConv_Spatial_and_Channel_Reconstruction_Convolution_for_Feature_Redundancy_CVPR_2023_paper.pdf) | [图片](modules/cnn/scconv/overview.png) | [简介](modules/cnn/scconv/info.md) | [详解](modules/cnn/scconv/detailed.md) | [代码](modules/cnn/scconv/module.py) |
| 19 | SCNet | [论文](https://openaccess.thecvf.com/content_CVPR_2020/papers/Liu_Improving_Convolutional_Networks_With_Self-Calibrated_Convolutions_CVPR_2020_paper.pdf) | [图片](modules/cnn/scnet_cnn/overview.png) | [简介](modules/cnn/scnet_cnn/info.md) | - | - |
| 20 | Temporal_conv卷积 | Connecting the Dots: Multivariate Time Series Forecasting with Graph Neural Networks | - | - | [详解](modules/cnn/temporal_conv/detailed.md) | [代码](modules/cnn/temporal_conv/module.py) |
| 21 | UniRepLKNet | [论文](https://arxiv.org/pdf/2311.15599v2) | [图片](modules/cnn/unireplknet/overview.png) | [简介](modules/cnn/unireplknet/info.md) | - | - |
| 22 | 可变性卷积 | InternImage: Exploring Large-Scale Vision Foundation Models with DeformableConvolutions | - | - | [详解](modules/cnn/deformable_conv/detailed.md) | [代码](modules/cnn/deformable_conv/module.py) |
| 23 | 深度可分离卷积 | DeepLab V3 | - | - | [详解](modules/cnn/depthwise_separable_conv/detailed.md) | [代码](modules/cnn/depthwise_separable_conv/module.py) |
| 24 | 空洞卷积 | MULTI-SCALE CONTEXT AGGREGATION BY DILATED CONVOLUTIONS | - | - | [详解](modules/cnn/dilated_conv/detailed.md) | [代码](modules/cnn/dilated_conv/module.py) |
| 25 | 蛇形卷积 | Dynamic Snake Convolution based on Topological Geometric Constraints for TubularStructure Segmentation | - | - | [详解](modules/cnn/snake_conv/detailed.md) | [代码](modules/cnn/snake_conv/module.py) |

---

## 频域系列模块

| # | 模块 | 论文 | 图片 | 简介 | 详解 | 代码 |
|---|------|------|------|------|------|------|
| 1 | AFFNet | [论文](https://arxiv.org/pdf/2307.14008v1) | [图片](modules/frequency/affnet/overview.png) | [简介](modules/frequency/affnet/info.md) | - | - |
| 2 | AFNO模块 | [论文](https://arxiv.org/pdf/2111.13587v2) | [图片](modules/frequency/afno/overview.png) | [简介](modules/frequency/afno/info.md) | - | - |
| 3 | fcanet | FcaNet: Frequency Channel Attention Networks | - | - | [详解](modules/frequency/fcanet/detailed.md) | [代码](modules/frequency/fcanet/module.py) |
| 4 | FFT | [论文](https://arxiv.org/pdf/2303.03932v2) | [图片](modules/frequency/fft/overview.png) | [简介](modules/frequency/fft/info.md) | - | - |
| 5 | FlashFFTConv | [论文](https://arxiv.org/pdf/2311.05908v1) | [图片](modules/frequency/flashfftconv/overview.png) | [简介](modules/frequency/flashfftconv/info.md) | - | - |
| 6 | FourCastNet | [论文](https://arxiv.org/pdf/2202.11214v1) | [图片](modules/frequency/fourcastnet/overview.png) | [简介](modules/frequency/fourcastnet/info.md) | - | - |
| 7 | FourierGNN | [论文](https://arxiv.org/pdf/2311.06190v1) | [图片](modules/frequency/fouriergnn/overview.png) | [简介](modules/frequency/fouriergnn/info.md) | - | - |
| 8 | GFNet | [论文](https://arxiv.org/pdf/2107.00645v2) | [图片](modules/frequency/gfnet/overview.png) | [简介](modules/frequency/gfnet/info.md) | - | - |
| 9 | SpectFormer | [论文](https://arxiv.org/pdf/2304.06446v2) | [图片](modules/frequency/spectformer/overview.png) | [简介](modules/frequency/spectformer/info.md) | - | - |
| 10 | TimesNet | [论文](https://arxiv.org/pdf/2210.02186v3) | [图片](modules/frequency/timesnet/overview.png) | [简介](modules/frequency/timesnet/info.md) | - | - |

---

## 特征融合系列模块

| # | 模块 | 论文 | 图片 | 简介 | 详解 | 代码 |
|---|------|------|------|------|------|------|
| 1 | Adaptive Fusion Techniques for Multimoda | [论文](https://arxiv.org/pdf/1911.03821v2) | [图片](modules/fusion/adaptive_fusion_techniques_for_multimodal_data/overview.png) | [简介](modules/fusion/adaptive_fusion_techniques_for_multimodal_data/info.md) | - | - |
| 2 | AFFAR | [论文](https://arxiv.org/pdf/2207.11221v1) | [图片](modules/fusion/affar/overview.png) | [简介](modules/fusion/affar/info.md) | - | - |
| 3 | ASSF | [论文](https://arxiv.org/pdf/1911.09516v2) | [图片](modules/fusion/assf/overview.png) | [简介](modules/fusion/assf/info.md) | - | - |
| 4 | CentralNet | [论文](https://arxiv.org/pdf/1808.07275v1) | [图片](modules/fusion/centralnet/overview.png) | [简介](modules/fusion/centralnet/info.md) | - | - |
| 5 | CLAP | [论文](https://arxiv.org/pdf/2211.06687v4) | [图片](modules/fusion/clap/overview.png) | [简介](modules/fusion/clap/info.md) | - | - |
| 6 | CMFNet | [论文](https://arxiv.org/pdf/2206.02748v1) | [图片](modules/fusion/cmfnet/overview.png) | [简介](modules/fusion/cmfnet/info.md) | - | - |
| 7 | DSSD | [论文](https://arxiv.org/pdf/1701.06659v1) | [图片](modules/fusion/dssd/overview.png) | [简介](modules/fusion/dssd/info.md) | - | - |
| 8 | FPN | [论文](https://arxiv.org/pdf/1612.03144v2) | [图片](modules/fusion/fpn/overview.png) | [简介](modules/fusion/fpn/info.md) | - | - |
| 9 | FSSD | [论文](https://arxiv.org/pdf/1712.00960v4) | [图片](modules/fusion/fssd/overview.png) | [简介](modules/fusion/fssd/info.md) | - | - |
| 10 | Low-rank-Multimodal-Fusion | [论文](https://arxiv.org/pdf/1806.00064v1) | [图片](modules/fusion/low_rank_multimodal_fusion/overview.png) | [简介](modules/fusion/low_rank_multimodal_fusion/info.md) | - | - |
| 11 | Multimodal Topic Learning for Video Reco | [论文](https://arxiv.org/pdf/2010.13373v1) | [图片](modules/fusion/multimodal_topic_learning_for_video_recommendation/overview.png) | [简介](modules/fusion/multimodal_topic_learning_for_video_recommendation/info.md) | - | - |
| 12 | Rethinking Atrous Convolution for Semant | [论文](https://arxiv.org/pdf/1706.05587v3) | [图片](modules/fusion/rethinking_atrous_convolution_for_semantic_image_segmentation/overview.png) | [简介](modules/fusion/rethinking_atrous_convolution_for_semantic_image_segmentation/info.md) | [详解](modules/fusion/rethinking_atrous_convolution_for_semantic_image_segmentation/detailed.md) | [代码](modules/fusion/rethinking_atrous_convolution_for_semantic_image_segmentation/module.py) |
| 13 | TFN | [论文](https://arxiv.org/pdf/1707.07250v1) | [图片](modules/fusion/tfn/overview.png) | [简介](modules/fusion/tfn/info.md) | - | - |

---

## 下采样系列模块

| # | 模块 | 论文 | 图片 | 简介 | 详解 | 代码 |
|---|------|------|------|------|------|------|
| 1 | AutoFocusFormer | [论文](https://arxiv.org/pdf/2304.12406v2) | [图片](modules/downsampling/autofocusformer/overview.png) | [简介](modules/downsampling/autofocusformer/info.md) | - | - |
| 2 | CM-DM | [论文](https://arxiv.org/pdf/2309.00853v1) | [图片](modules/downsampling/cm_dm/overview.png) | [简介](modules/downsampling/cm_dm/info.md) | - | - |
| 3 | FastICENet | [论文](https://www.sciencedirect.com/science/article/abs/pii/S0165168423002244) | [图片](modules/downsampling/fasticenet/overview.png) | [简介](modules/downsampling/fasticenet/info.md) | - | - |
| 4 | FouriDown | [论文](https://openreview.net/pdf?id=nCwStXFDQu) | [图片](modules/downsampling/fouridown/overview.png) | [简介](modules/downsampling/fouridown/info.md) | - | - |
| 5 | GC ViT | [论文](https://arxiv.org/pdf/2206.09959v5) | [图片](modules/downsampling/gc_vit/overview.png) | [简介](modules/downsampling/gc_vit/info.md) | - | - |
| 6 | LUM-ViT | [论文](https://arxiv.org/pdf/2403.01412v1) | [图片](modules/downsampling/lum_vit/overview.png) | [简介](modules/downsampling/lum_vit/info.md) | - | - |
| 7 | PUERT | [论文](https://arxiv.org/pdf/2204.11189v1) | [图片](modules/downsampling/puert/overview.png) | [简介](modules/downsampling/puert/info.md) | - | - |
| 8 | SPD-Conv | [论文](https://arxiv.org/pdf/2208.03641v1) | [图片](modules/downsampling/spd_conv/overview.png) | [简介](modules/downsampling/spd_conv/info.md) | - | - |

---

## 注意力系列模块

| # | 模块 | 论文 | 图片 | 简介 | 详解 | 代码 |
|---|------|------|------|------|------|------|
| 1 | A2 -Nets | [论文](https://arxiv.org/pdf/1810.11579) | [图片](modules/attention/a2_nets/overview.png) | [简介](modules/attention/a2_nets/info.md) | [详解](modules/attention/a2_nets/detailed.md) | [代码](modules/attention/a2_nets/module.py) |
| 2 | ACmix | [论文](https://arxiv.org/pdf/2111.14556v2) | [图片](modules/attention/acmix/overview.png) | [简介](modules/attention/acmix/info.md) | [详解](modules/attention/acmix/detailed.md) | [代码](modules/attention/acmix/module.py) |
| 3 | AFT | An Attention Free Transformer | - | - | [详解](modules/attention/aft/detailed.md) | [代码](modules/attention/aft/module.py) |
| 4 | Agent Attention | [论文](https://arxiv.org/pdf/2312.08874v3) | [图片](modules/attention/agent_attention/overview.png) | [简介](modules/attention/agent_attention/info.md) | - | - |
| 5 | Axial_attention | AXIAL ATTENTION IN MULTIDIMENSIONAL TRANSFORMERS | - | - | [详解](modules/attention/axial_attention/detailed.md) | [代码](modules/attention/axial_attention/module.py) |
| 6 | BiFormer | [论文](https://arxiv.org/pdf/2303.08810v1) | [图片](modules/attention/biformer/overview.png) | [简介](modules/attention/biformer/info.md) | [详解](modules/attention/biformer/detailed.md) | [代码](modules/attention/biformer/module.py) |
| 7 | CBAM | [论文](https://arxiv.org/pdf/1807.06521v2) | [图片](modules/attention/cbam/overview.png) | [简介](modules/attention/cbam/info.md) | [详解](modules/attention/cbam/detailed.md) | [代码](modules/attention/cbam/module.py) |
| 8 | CenterMask | [论文](https://arxiv.org/pdf/1911.06667v6) | [图片](modules/attention/centermask/overview.png) | [简介](modules/attention/centermask/info.md) | - | - |
| 9 | Cloattention | Rethinking Local Perception in Lightweight Vision Transformer | - | - | [详解](modules/attention/cloattention/detailed.md) | [代码](modules/attention/cloattention/module.py) |
| 10 | CoordAttention | Coordinate Attention for Efficient Mobile Network Design | - | - | [详解](modules/attention/coordattention/detailed.md) | [代码](modules/attention/coordattention/module.py) |
| 11 | CoTAttention | Contextual Transformer Networks for Visual Recognition | - | - | [详解](modules/attention/cot_attention/detailed.md) | [代码](modules/attention/cot_attention/module.py) |
| 12 | CrissCrossAttention | CROSSFORMER: A VERSATILE VISION TRANSFORMER HINGING ON CROSS-SCALEATTENTION | - | - | [详解](modules/attention/crisscrossattention/detailed.md) | [代码](modules/attention/crisscrossattention/module.py) |
| 13 | DANet | Dual Attention Network for Scene Segmentation | - | - | [详解](modules/attention/danet/detailed.md) | [代码](modules/attention/danet/module.py) |
| 14 | DilateForme | DilateFormer: Multi-Scale Dilated Transformer for Visual Recognition | - | - | [详解](modules/attention/dilateforme/detailed.md) | [代码](modules/attention/dilateforme/module.py) |
| 15 | ECA-Net | [论文](https://arxiv.org/pdf/1910.03151v4) | [图片](modules/attention/eca/overview.png) | [简介](modules/attention/eca/info.md) | [详解](modules/attention/eca/detailed.md) | [代码](modules/attention/eca/module.py) |
| 16 | EfficientAdditiveAttnetion | SwiftFormer: Efficient Additive Attention for Transformer-based Real-time Mobile VisionApplications | - | - | [详解](modules/attention/efficientadditiveattnetion/detailed.md) | [代码](modules/attention/efficientadditiveattnetion/module.py) |
| 17 | EMA-attention-module | [论文](https://arxiv.org/pdf/2305.13563v2) | [图片](modules/attention/ema_attention_module/overview.png) | [简介](modules/attention/ema_attention_module/info.md) | [详解](modules/attention/ema_attention_module/detailed.md) | [代码](modules/attention/ema_attention_module/module.py) |
| 18 | EMO | Rethinking Mobile Block for Efficient Attention-based Models | - | - | [详解](modules/attention/emo/detailed.md) | [代码](modules/attention/emo/module.py) |
| 19 | EMSA | ResT: An Efficient Transformer for Visual Recognition | - | - | [详解](modules/attention/emsa/detailed.md) | [代码](modules/attention/emsa/module.py) |
| 20 | ExternalAttention | Beyond Self-attention: External Attention using Two Linear Layers for Visual Tasks | - | - | [详解](modules/attention/externalattention/detailed.md) | [代码](modules/attention/externalattention/module.py) |
| 21 | FECAM | [论文](https://arxiv.org/pdf/2212.01209v1) | [图片](modules/attention/fecam/overview.png) | [简介](modules/attention/fecam/info.md) | - | - |
| 22 | gam | Global Attention Mechanism: Retain Information to Enhance Channel-Spatial Interactions | - | - | [详解](modules/attention/gam/detailed.md) | [代码](modules/attention/gam/module.py) |
| 23 | Gather-Excite | [论文](https://arxiv.org/pdf/1810.12348v3) | [图片](modules/attention/gather_excite/overview.png) | [简介](modules/attention/gather_excite/info.md) | - | - |
| 24 | GCNet | [论文](https://arxiv.org/pdf/2012.13375v1) | [图片](modules/attention/gcnet/overview.png) | [简介](modules/attention/gcnet/info.md) | - | - |
| 25 | HaLoAttention | Scaling Local Self-Attention for Parameter Efficient Visual Backbones | - | - | [详解](modules/attention/haloattention/detailed.md) | [代码](modules/attention/haloattention/module.py) |
| 26 | HAT | [论文](https://arxiv.org/pdf/2205.04437v3) | [图片](modules/attention/hat/overview.png) | [简介](modules/attention/hat/info.md) | - | - |
| 27 | LSKNet | [论文](https://arxiv.org/pdf/2303.09030v2) | [图片](modules/attention/lsknet/overview.png) | [简介](modules/attention/lsknet/info.md) | - | - |
| 28 | Non-local Neural Networks | [论文](https://arxiv.org/pdf/1711.07971v3) | [图片](modules/attention/non_local_neural_networks/overview.png) | [简介](modules/attention/non_local_neural_networks/info.md) | - | - |
| 29 | Non-stationary Transformers | [论文](https://arxiv.org/pdf/2205.14415v4) | [图片](modules/attention/non_stationary_transformers/overview.png) | [简介](modules/attention/non_stationary_transformers/info.md) | - | - |
| 30 | PAM | Pyraformer: Low-Complexity Pyramidal Attention for Long-Range Time Series Modeling andForecasting | - | - | [详解](modules/attention/pam/detailed.md) | [代码](modules/attention/pam/module.py) |
| 31 | Partnet | NON-DEEP NETWORKS | - | - | [详解](modules/attention/partnet/detailed.md) | [代码](modules/attention/partnet/module.py) |
| 32 | PSA | [论文](https://arxiv.org/pdf/2107.00782v2) | [图片](modules/attention/psa/overview.png) | [简介](modules/attention/psa/info.md) | - | - |
| 33 | PSA | EPSANet: An Efficient Pyramid Squeeze Attention Block on Convolutional Neural Network | - | - | [详解](modules/attention/psa_epsanet/detailed.md) | [代码](modules/attention/psa_epsanet/module.py) |
| 34 | RevCol | [论文](https://arxiv.org/pdf/2212.11696v3) | [图片](modules/attention/revcol/overview.png) | [简介](modules/attention/revcol/info.md) | - | - |
| 35 | S2Attention | S2-MLPV2: IMPROVED SPATIAL-SHIFT MLP ARCHITECTURE FOR VISION | - | - | [详解](modules/attention/s2attention/detailed.md) | [代码](modules/attention/s2attention/module.py) |
| 36 | SAFM | Spatially-Adaptive Feature Modulation for Efficient Image Super-Resolution | - | - | [详解](modules/attention/safm/detailed.md) | [代码](modules/attention/safm/module.py) |
| 37 | SE Net | Squeeze-and-Excitation Networks | - | - | [详解](modules/attention/se_net/detailed.md) | [代码](modules/attention/se_net/module.py) |
| 38 | Sea | SeaFormer: Squeeze-Enhanced Axial Transformer for Mobile Semantic Segmentation | - | - | [详解](modules/attention/sea/detailed.md) | [代码](modules/attention/sea/module.py) |
| 39 | ShuffleAttention | SA-NET: SHUFFLE ATTENTION FOR DEEP CONVOLUTIONAL NEURAL NETWORKS | - | - | [详解](modules/attention/shuffleattention/detailed.md) | [代码](modules/attention/shuffleattention/module.py) |
| 40 | SimAM | SimAM: A Simple, Parameter-Free Attention Module for Convolutional Neural Networks | - | - | [详解](modules/attention/simam/detailed.md) | [代码](modules/attention/simam/module.py) |
| 41 | SKAttention | Selective Kernel Networks | - | - | [详解](modules/attention/skattention/detailed.md) | [代码](modules/attention/skattention/module.py) |
| 42 | STVit | Vision Transformer with Super Token Sampling | - | - | [详解](modules/attention/stvit/detailed.md) | [代码](modules/attention/stvit/module.py) |
| 43 | TCN | [论文](https://arxiv.org/pdf/1803.01271v2) | [图片](modules/attention/tcn/overview.png) | [简介](modules/attention/tcn/info.md) | - | - |
| 44 | TripletAttention | Rotate to Attend: Convolutional Triplet Attention Module | - | - | [详解](modules/attention/tripletattention/detailed.md) | [代码](modules/attention/tripletattention/module.py) |
| 45 | UFO | UFO-ViT: High Performance Linear Vision Transformer without Softmax | - | - | [详解](modules/attention/ufo/detailed.md) | [代码](modules/attention/ufo/module.py) |
| 46 | ViP | VISION PERMUTATOR: A PERMUTABLE MLP-LIKE ARCHITECTURE FOR VISUALRECOGNITION | - | - | [详解](modules/attention/vip/detailed.md) | [代码](modules/attention/vip/module.py) |

---

## 时间序列模块

| # | 模块 | 论文 | 图片 | 简介 | 详解 | 代码 |
|---|------|------|------|------|------|------|
| 1 | ANOMALY TRANSFORMER | [论文](https://arxiv.org/pdf/2110.02642) | [图片](modules/timeseries/anomaly_transformer/overview.png) | [简介](modules/timeseries/anomaly_transformer/info.md) | - | - |
| 2 | AnomalyBERT | [论文](https://arxiv.org/pdf/2305.04468v1) | [图片](modules/timeseries/anomalybert/overview.png) | [简介](modules/timeseries/anomalybert/info.md) | - | - |
| 3 | CityCAN | [论文](https://arxiv.org/pdf/2205.14415) | [图片](modules/timeseries/citycan/overview.png) | [简介](modules/timeseries/citycan/info.md) | - | - |
| 4 | COUTA模块 | [论文](https://arxiv.org/pdf/2207.12201) | [图片](modules/timeseries/couta/overview.png) | [简介](modules/timeseries/couta/info.md) | - | - |
| 5 | DCdetector | [论文](https://arxiv.org/pdf/2306.10347v2) | [图片](modules/timeseries/dcdetector/overview.png) | [简介](modules/timeseries/dcdetector/info.md) | - | - |
| 6 | FECAM | - | [图片](modules/timeseries/fecam/overview.png) | [简介](modules/timeseries/fecam/info.md) | - | - |
| 7 | GANF模块 | [论文](https://arxiv.org/pdf/2202.07857) | [图片](modules/timeseries/ganf/overview.png) | [简介](modules/timeseries/ganf/info.md) | - | - |
| 8 | GDN模块 | [论文](https://arxiv.org/pdf/2106.06947v1) | [图片](modules/timeseries/gdn/overview.png) | [简介](modules/timeseries/gdn/info.md) | - | - |
| 9 | InterFusion模块 | [论文](https://netman.aiops.org/wp-content/uploads/2021/08/KDD21_InterFusion_Li.pdf) | [图片](modules/timeseries/interfusion/overview.png) | [简介](modules/timeseries/interfusion/info.md) | - | - |
| 10 | PYRAFORMER | [论文](https://openreview.net/pdf?id=0EXmFzUn5I) | [图片](modules/timeseries/pyraformer/overview.png) | [简介](modules/timeseries/pyraformer/info.md) | - | - |
| 11 | Spectral Residual | [论文](https://arxiv.org/pdf/1906.03821v1) | [图片](modules/timeseries/spectral_residual/overview.png) | [简介](modules/timeseries/spectral_residual/info.md) | - | - |
| 12 | TCN模块 | An Empirical Evaluation of Generic Convolutional and Recurrent Networks for Sequence Modeling | [图片](modules/timeseries/tcn/overview.png) | [简介](modules/timeseries/tcn/info.md) | - | - |
| 13 | TODS | [论文](https://arxiv.org/pdf/2009.09822v3) | [图片](modules/timeseries/tods/overview.png) | [简介](modules/timeseries/tods/info.md) | - | - |
| 14 | TranAD | [论文](https://arxiv.org/pdf/2201.07284) | [图片](modules/timeseries/tranad/overview.png) | [简介](modules/timeseries/tranad/info.md) | - | - |
| 15 | UnetTSF | [论文](https://arxiv.org/pdf/2401.03001) | [图片](modules/timeseries/unettsf/overview.png) | [简介](modules/timeseries/unettsf/info.md) | - | - |
| 16 | 无监督模型选择 | [论文](https://arxiv.org/pdf/2210.01078) | [图片](modules/timeseries/unsupervised_model_selection/overview.png) | [简介](modules/timeseries/unsupervised_model_selection/info.md) | - | - |

---

## 文件结构说明

```
modules/<分类>/<模块名>/
├── overview.png    # 模块结构图（来自阿文整理）
├── info.md         # 论文信息与简介（来自阿文整理）
├── detailed.md     # 机制详解：作用、机制、独特优势（来自MinerU）
└── module.py       # Python实现代码（来自MinerU）
```

---

*生成工具: build.py*