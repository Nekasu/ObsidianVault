
>[!warning] 提示
>推荐使用 [obsidian 软件](https://obsidian.md/), 以获得最好的阅读体验
>点击右上角「书本」![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240910163022.png)图标, 进入阅读模式, 以获得更好的阅读体验！
>
>作者：Nekasu/周肖桐

爱钻牛角尖的宝贝们有时可能希望能分清这三者的区别, 这里有一些简单的解释, 快来看看吧

# 一图说明问题

![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/Drawing%202024-05-11%2017.46.08.excalidraw.svg)


# CUDA 既是架构, 又是框架

CUDA 也是一款 `异构计算架构、异构计算框架`

## 基础知识

首先请明白什么是[[Neural Network/昇腾全栈架构设计/昇腾AI处理器_架构与编程/A0_基础概念#架构|架构]], 什么是[[Neural Network/昇腾全栈架构设计/昇腾AI处理器_架构与编程/A0_基础概念#框架|框架]].

通俗来说
- 架构就是微软公司设计 powerpoint 时的蓝图, 类似于设计标准之类的东西.
- Powerpoint 就是框架, 做 ppt 的过程就是使用框架的过程.

## CUDA 是架构

**CUDA 作为架构：** 在计算机领域，"CUDA" 通常指的是 NVIDIA 的 Compute Unified Device Architecture ，这是一种并行计算架构，用于利用 GPU 进行通用目的的并行计算。这个架构指的是一种硬件架构，它定义了 GPU 如何执行并行计算任务，包括了处理器、内存等硬件组件的设计和交互方式。

有时, Compute Unified Device Architecture 中的“Architecture”会被翻译成“平台”, 但实际上还是指“架构”.

## CUDA 是框架

**CUDA 作为框架：** 有时人们可能也会将 "CUDA" 用来描述 NVIDIA 提供的一套编程模型、工具和库，用于在 GPU 上进行并行编程。这个编程框架允许开发者在 GPU 上编写并行代码，并利用 GPU 的并行计算能力。这个框架提供了一组 API 和工具，用于管理内存、调度任务、并行编程等。

## CUDA 既是架构, 也是框架

CUDA 是一种设计思想, 将之实现后的框架也被人们称作 CUDA.

CUDA 起初是 NVIDIA 设计的一种并行计算架构和思想，用于利用 GPU 进行通用目的的高性能计算。随着时间的推移，CUDA 这个设计思想被实现为一套编程框架，开发者可以使用这个框架在 GPU 上进行并行编程。

总结起来，CUDA 首先是一种并行计算架构的设计思想，描述了如何在 GPU 上执行并行计算。然后，NVIDIA 将这个设计思想实现为一套编程框架，使开发者能够利用 GPU 的并行计算能力。因此，人们可以将实现后的编程框架也称作 CUDA，因为它是基于 CUDA 架构思想而创建的。

## 争议

关于 CUDA 是否足够被称为一个框架，存在一些不同的观点。这个问题的背景如下：

**CUDA 的特点：**
CUDA（Compute Unified Device Architecture）是 NVIDIA 提供的一种并行计算框架，旨在利用 GPU 进行通用目的的高性能计算。CUDA 包括编程模型、API 和工具，允许开发者在 GPU 上编写并行代码，从而加速各种计算密集型任务，包括深度学习、科学计算等。CUDA 提供了一些库和函数，用于管理内存、调度任务、并行编程等。

**关于 "框架" 的定义：**
在软件开发领域，术语 "框架" 通常指的是提供了一定的结构、模式、工具和功能的软件环境，用于支持和简化特定类型应用程序的开发。框架通常为开发者提供了一些通用的功能，可以让他们更轻松地构建特定类型的应用程序。

**关于是否称为 "框架" 的争议：**
有些人可能会认为 CUDA 并不是典型意义上的 "框架"，因为它更侧重于提供了一种编程模型和工具，而不像一些传统的框架那样提供了丰富的抽象、组件和预定义功能。另一方面，有些人可能认为 CUDA 可以被视为一种框架，因为它提供了一系列工具和接口，用于支持 GPU 上的并行编程，使开发者能够更好地利用 GPU 的计算能力。

因此，关于是否将 CUDA 称为 "框架" 可能会因为不同人的观点而有所不同。这种争议通常是语义上的，取决于对 "框架" 这个术语的理解和定义。无论如何，CUDA 在并行计算领域发挥了重要作用，提供了强大的工具来加速各种计算任务，包括深度学习和科学计算。

# cudatoolkit 是架构的实现

cudatoolkit 的意思是“cuda 工具箱”

我们可以认为, cudatoolkit 是对 cuda 作为“架构”的实现. 

也即, cudatoolkit 实际上是 cuda 这种设计思路的一个具体的实现. 我们可以使用 cudatoolkit 这一工具箱实现许多对 gpu 的操作.

## nvcc 是 cudatoolkit 的编译器

nvcc 是 cudatoolkit 的一部分.

cudatoolkit 为了能够将用户编写的命令能够同时传递给 gpu 与 cpu, 使二者协同工作, 需要将用户的代码进行编译, 以确保 gpu 与 cpu 能按照特定的工作流程进行协同工作.

而 nvcc 就是这样的一个编译器, 能够将用户写的高级语言编译成二进制语言, 供机器使用.

# cudnn 是 cudatoolkit 的组成

实际上，cuDNN（CUDA Deep Neural Network library）与 CUDA Toolkit 之间存在着密切的关系。CuDNN 是 NVIDIA 开发的深度学习加速库，它是 CUDA Toolkit 的一部分，提供了深度学习框架（如 TensorFlow、PyTorch 等）所需的 GPU 加速的基本操作和算法的实现。

CuDNN 与 CUDA Toolkit 的关系如下：

1. **cuDNN 是 CUDA Toolkit 的组件**：cuDNN 被包含在 CUDA Toolkit 中，作为其中的一个重要组件。用户安装 CUDA Toolkit 后，cuDNN 也会随之安装。

2. **CUDA Toolkit 提供了深度学习开发所需的基础设施**：除了 cuDNN 外，CUDA Toolkit 还提供了用于 CUDA 编程的编译器、库、调试器等工具，以及与 GPU 相关的其他加速库和工具。

3. **cuDNN 提供了深度学习任务的 GPU 加速实现**：cuDNN 实现了深度学习中常见的基本操作，如卷积、池化、归一化等，以高效地在 NVIDIA GPU 上执行。这使得深度学习框架可以利用 GPU 的并行计算能力进行高效的模型训练和推理。

因此，cuDNN 是 CUDA Toolkit 中的一个重要组件，它为深度学习框架提供了 GPU 加速的实现，使得深度学习任务能够在 NVIDIA GPU 上获得高性能的执行。

# 一些问题

## 从 NVIDIA 上下载的 CUDA 是什么？

- 我们从 NIVIDIA 上下载的 CUDA, 实际上下载的是 cudatoolkit (完整版)

## PyTorch 中的 CUDA 是什么？

- PyTorch 中的 CUDA 指的是 cuda toolkit (for pytorch), 
-  cuda toolkit (for pytorch) 中一般不含有 cudatoolkit (完整版) 的编译器 nvcc
	- 因为 PyTorch 有自己的方法将 cudatoolkit 的代码编译成二进制语言, 所以无须 nvcc 的辅助, 也因此 cudatoolkit (for PyTorch) 中没有 nvcc