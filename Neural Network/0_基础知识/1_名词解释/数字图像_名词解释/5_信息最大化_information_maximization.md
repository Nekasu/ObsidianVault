
>[!warning] 提示
>点击右上角「书本」![[Pasted image 20231125105318.png]]图标, 进入阅读模式, 以获得更好的阅读体验！

- 本人首次下述渠道了解到该名词
	- 论文：Park T, Efros A A, Zhang R, et al. Contrastive learning for unpaired image-to-image translation \[C\] /a/Computer Vision–ECCV 2020: 16 th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part IX 16. Springer International Publishing, 2020: 319-345.
- 原文如下
	- Here we seek to replace cycle-consistency by instead learning a cross-domain similarity function between input and output patches through <mark style="background: #6495EDED;">information maximization</mark>, without relying on a pre-specified distance
- 记录日期：
	- 2024-09-02

“信息最大化”（Information Maximization）是指在模型训练过程中，试图通过最大化输出数据与输入数据之间的[[4_互信息|互信息（mutual information）]]，来增强模型对输入数据的理解和区分能力。在这个过程中，模型会倾向于学习最能区分不同输入模式的信息特征，从而提高模型的性能。

在这句话中，作者提出了一种方法，试图通过信息最大化来替代循环一致性（cycle-consistency）。具体来说，这个方法通过最大化输入和输出之间的互信息，来学习跨域（cross-domain）的相似性函数。这种方法不依赖于预先指定的距离度量，而是通过让模型自主学习能够最大化输入和输出块（patch）之间相关性的特征，从而捕捉到跨域的相似性。

总的来说，这句话中的“信息最大化”指的是通过最大化输入和输出之间的信息传递，使得模型能够更好地学习和表达输入和输出之间的跨域相似性。说明, 最大化互信息可以协助完成跨域转换.