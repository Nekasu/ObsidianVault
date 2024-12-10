
>[!warning] 提示
>点击右上角「书本」![[Pasted image 20231125105318.png]]图标, 进入阅读模式, 以获得更好的阅读体验！

- 本人首次下述渠道了解到该名词
	- 论文：Park T, Efros A A, Zhang R, et al. Contrastive learning for unpaired image-to-image translation \[C\] /a/Computer Vision–ECCV 2020: 16 th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part IX 16. Springer International Publishing, 2020: 319-345.
- 原文如下
	- Emergent perceptual similarity in deep <mark style="background: #ADCCFFA6;">network embeddings</mark>.
- 记录日期：
	- 2024-09-02

本文内容主要来自：[# 网络表示学习综述：一文理解Network Embedding](https://www.jiqizhixin.com/articles/2018-08-14-10)

### 简单理解

- Network Embedding 中的 Network 指的是“关系网络”, 即点与边组成的图结构, 而非我们熟悉的神经网络.
- 向量嵌入 (vector embedding)是一个将<mark style="background: #ADCCFFA6;">高维向量映射到低维向量</mark>的方式.
- 网络嵌入 (network embedding)是一个将<mark style="background: #ADCCFFA6;">复杂信息网络映射到简单信息网络</mark>的方式.
	- 信息网络：可以用 obsidian 中的节点图理解, 如下图
	- 以 DeepWalk 为例, DeepWalk 可以将网络中的拓扑信息转换为一个二维的潜在表示 (latent representation)
		- DeepWalk 是第一个被提出来使用或深度学习社区的技术的网络嵌入方法
		- 其学习 Zachary’s Karate network 网络中的拓扑结构信息并转换成一个二维的潜在表示（latent representation）
		- ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240902222412.png)

### Network Embedding 介绍

由于 (图结构的) 信息网络可能包含数十亿个节点和边缘，因此在整个网络上执行复杂的推理过程可能会非常棘手。

因此有人提出了用于解决该问题的一种方法是网络嵌入（Network Embedding）。

NE 的中心思想就是找到一种==映射==函数，该函数将网络中的每个节点转换为低维度的潜在表示。

#### Network Embedding 简史

传统意义上的 Graph Embedding 被看成是一个==降维==的过程，而主要的方法包括==主成分分析==（PCA）和多维缩放（MDS）。所有的方法都可以理解成运用一个 n × k 的矩阵来表示原始的 n × m 矩阵，其中 k << n。

在 2000 年代早期，又提出了其他方法，如 IsoMap 和 LLE，以保持非线性流形的整体结构。总的来说，这些方法都在小型网络上提供了良好的性能。 然而这些方法的时间复杂性至少是二次的，这使得它们无法在大规模网络上运行。

另一类流行的==降维==技术使用可从图中导出的矩阵的光谱特性（例如，特征向量）来嵌入图的节点。拉普拉斯特征==映射==（Laplacian eigenmaps）通过与其k个最小非平凡特征值相关联的特征向量表示图中的每个节点。
