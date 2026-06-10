# EMO - 详细讲解

> 论文: Rethinking Mobile Block for Efficient Attention-based Models

## 1、作用

本文提出了一种有效的轻量级模型设计方法，旨在开发现代高效的轻量级模型，用于密集预测任务，同时平衡参数、FLOPs和性能。作者通过重新思考高效的Inverted Residual Block（IRB）和Transformer的有效组件，从统一的视角出发，扩展了基于CNN的IRB到基于Meta attention的模型，并抽象出了一种一次残差的Meta Mobile Block（MMB），用于轻量级模型设计。

## 2、机制

本研究通过简单但有效的设计准则，提出了一种现代的Inverted Residual Mobile Block（iRMB），并使用iRMB构建了一个类似于ResNet的高效模型（EMO），仅用于下游任务。EMO通过将CNN的效率和Transformer的动态建模能力结合在iRMB中，有效地提高了模型性能。同时，EMO在不引入复杂结构的情况下，实现了与当前最先进的轻量级注意力模型的竞争性能。

## 3、独特优势

EMO在ImageNet-1K、COCO2017和ADE20K基准上的广泛实验展示了其优越性，例如，EMO-1M/2M/5M分别达到了71.5%、75.1%和78.4%的Top-1准确率，超过了同等级别的CNN-/Attention-based模型。同时，在参数效率和准确性之间取得了良好的平衡：在iPhone14上运行速度比EdgeNeXt快2.8-4.0倍。此外，EMO不使用复杂的操作，但仍然在多个视觉任务中获得了非常竞争性的结果，这证明了其作为轻量级注意力模型的有效性和实用性。

---

> 代码文件: [module.py](module.py)
