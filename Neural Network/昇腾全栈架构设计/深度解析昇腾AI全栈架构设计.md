本文内容来自
[深度解析昇腾AI全栈架构设计](https://www.elecfans.com/rengongzhineng/2093350.html)

# 1 昇腾AI全栈架构

![[Neural Network/昇腾全栈架构设计/0_Attachments/Pasted image 20230803161204.png]]
## 1.1 昇腾AI全栈的四个大部分

- 应用使能层：`接口层`
	- 面此层面通常<mark style="background: #FFB8EBA6;">包含用于部署模型的软硬件</mark>，例如API、SDK、部署平台，模型库等等。
- AI框架层面：`框架层`
	- 此层面<mark style="background: #FFB8EBA6;">包含用于构建模型的训练框架</mark>，例如华为的MindSpore、TensorFlow、Pytorch等。
- 异构计算架构：`协调层`
	- <mark style="background: #FFB8EBA6;">偏底层、偏通用</mark>的计算框架，用于针对上层AI框架的调用进行加速，力求向上支持多种AI框架，并在硬件上进行加速。
	- 即CANN异构计算架构
- 计算硬件：`硬件层`
	- 本层是AI计算的底座，有了<mark style="background: #FFB8EBA6;">强力的芯片及硬件设备</mark>，上层的加速才有实施的基础。

# 2.异构计算架构CANN

## 2.1 CANN 抽象的五层架构

`【涉及领域与基础架构】`面向计算机视觉、自然语言处理、推荐系统、类机器人等领域量身打造了基于“达芬奇（DaVinci）架构”的昇腾（Ascend）AI处理器，开启了智能之旅。

`【CANN被提出的原因及其优势】`为提升用户开发效率和释放昇腾AI处理器澎湃算力，同步推出针对AI场景的异构计算架构CANN（Compute Architecture for Neural Networks），CANN通过提供多层次的编程接口，以全场景、低门槛、高性能的优势，支持用户快速构建基于[[Neural Network/昇腾全栈架构设计/0专有名词#Ascend平台|Ascend平台]]的AI应用和业务。

`〔昇腾AI异构计算架构的结构〕`昇腾AI异构计算架构（Compute Architecture for Neural Networks，CANN）被抽象成五层架构，如下图所示 \[下图中间部分\]。

[![ab1bc83e-fe80-11ed-90ce-dac502259ad0.png](http://images.elecfans.top/uploads/20230530/ab1bc83e-fe80-11ed-90ce-dac502259ad0.png)](http://images.elecfans.top/uploads/20230530/ab1bc83e-fe80-11ed-90ce-dac502259ad0.png)

### **1.  昇腾计算语言接口** 〔编程语言接口〕

昇腾计算语言（Ascend Computing Language，AscendCL）接口是昇腾计算开放编程框架，是对低层昇腾计算服务接口的封装。它提供Device（设备）管理、Context（上下文）管理、Stream（流）管理、内存管理、模型加载与执行、算子加载与执行、媒体数据处理、Graph（图）管理等API库，供用户开发人工智能应用调用。

### **2.  昇腾计算服务层**  〔计算库〕

本层主要提供昇腾计算库，例如神经网络（Neural Network，NN）库、线性代数计算库（Basic Linear Algebra Subprograms，BLAS）等；昇腾计算调优引擎库，例如算子调优、子图调优、梯度调优、模型压缩以及AI框架适配器。

### **3.  昇腾计算编译引擎** 〔编译〕

本层主要提供图编译器（Graph Compiler）和TBE（Tensor Boost Engine）算子开发支持。前者将用户输入中间表达（Intermediate Representation，IR）的计算图编译成NPU运行的模型。后者提供用户开发自定义算子所需的工具。

### **4.  昇腾计算执行引擎** 〔程序执行〕

本层负责模型和算子的执行，提供如[[Neural Network/昇腾全栈架构设计/0专有名词#运行时|运行时]]（Runtime）库（执行内存分配、模型管理、数据收发等）、图执行器（Graph Executor）、数字视觉预处理（Digital Vision Pre-Processing，DVPP）、人工智能预处理（Artificial Intelligence Pre-Processing，AIPP）、华为集合通信库（Huawei Collective Communication Library，HCCL）等功能单元。

### **5.  昇腾计算基础层**

本层主要为其上各层提供基础服务，如共享虚拟内存（Shared Virtual Memory，SVM）、设备虚拟化（Virtual Machine，VM）、主机-设备通信（Host Device Communication，HDC）等。

## 2.2 CANN 的三层逻辑架构

[![ab59620c-fe80-11ed-90ce-dac502259ad0.png](http://images.elecfans.top/uploads/20230530/ab59620c-fe80-11ed-90ce-dac502259ad0.png)](http://images.elecfans.top/uploads/20230530/ab59620c-fe80-11ed-90ce-dac502259ad0.png)

### 2.2.1 应用层

包括基于 Ascend 平台开发的各种应用，以及 Ascend 提供给用户进行算法开发、调优的应用类工具。

#### **1. 推理应用**

基于 AscendCL 提供的 API 构建推理应用

#### **2. AI 框架**

包括 TensorFlow、Caffe、MindSpore 以及第三方框架

#### **3. 模型小型化工具**

实现对模型进行量化，加速模型

#### **4. AutoML 工具**

基于 MindSpore 自动学习工具，根据昇腾芯片特点进行搜索生成亲和性网络，充分发挥昇腾性能

#### **5. 加速库**

基于 AscendCL 构建的加速库（当前支持 Blas 加速库）

#### **6. MindStudio**

提供给开发者的集成开发环境和调试工具，可以通过MindStudio进行离线模型转换、离线推理算法应用开发调试、算法调试、自定义算子开发和调试、日志查看、性能调优、系统故障查看等

### 2. 2.2 芯片使能层

实现解决方案对外能力开放，以及基于计算图的业务流的控制和运行。 

#### **1. AscendCL 昇腾计算语言库**

开放编程框架，提供 Device/Context/Stream/ 内存等的管理、模型及算子的加载与执行、媒体数据处理、Graph 管理等 API 库，供用户开发深度神经网络应用。

#### **2. 图优化和编译**

统一的 IR 接口对接不同前端，支持 TensorFlow/Caffe/MindSpore 表达的计算图的解析/优化/编译，提供对后端计算引擎最优化部署能力

Graph Engine：图编译和运行的控制中心

Fusion Engine：管理算子融合规则

AI[CPU](https://www.elecfans.com/v/tag/132/) Engine：AICPU 算子信息管理

HCCL：HCCL 算子信息管理

#### **3. 算子编译和算子库**

TBE：编译生成算子及算子开发工具

算子库：神经网络加速库

#### **4. 数字视觉预处理**

实现[视频](https://m.elecfans.com/v/)编解码（VENC/VDEC）、JPEG 编解码（JPEG/E）、PNG 解码（PNGD）、VPC（预处理）

#### **5. 执行引擎**

Runtime：为神经网络的任务分配提供资源管理通道

Task Scheduler：计算图 Task 序列的管理和调度、执行

### 2.2.3 计算资源层

主要实现系统对数据的处理和对数据的运算执行。 

#### **1. 计算设备**

AI Core：执行 NN 类算子

AI CPU：执行 CPU 算子

DVPP：视频/图像编解码、预处理

#### **2. 通信链路**

PCIe：芯片间或芯片与 CPU 间高速互联

HCCS：实现芯片间缓存一致性功能

RoCE：实现芯片内存 R[DMA](https://www.elecfans.com/tags/dma/) 功能

# 3.昇腾计算语言接口 AscendCL

## 3.1 AscendCL 简介

AscendCL（Ascend Computing Language，昇腾计算语言）是昇腾计算开放编程框架，是对底层昇腾计算服务接口的封装，它提供运行时资源（例如设备、内存等）管理、模型加载与执行、算子加载与执行、图片数据编解码/裁剪/缩放处理等API库，实现在昇腾CANN平台上进行深度学习推理计算、图形图像预处理、单算子加速计算等能力。简单来说，就是统一的API框架，实现对所有资源的调用。

[![ac1e1980-fe80-11ed-90ce-dac502259ad0.png](http://images.elecfans.top/uploads/20230530/ac1e1980-fe80-11ed-90ce-dac502259ad0.png)](http://images.elecfans.top/uploads/20230530/ac1e1980-fe80-11ed-90ce-dac502259ad0.png)

## 3.2 AscendCL 的优势

1.  高度抽象：算子编译、加载、执行的API归一，相比每个算子一个API，AscendCL大幅减少API数量，降低复杂度。 
2.  向后兼容：AscendCL具备向后兼容，确保软件升级后，基于旧版本编译的程序依然可以在新版本上运行。 
3.  零感知芯片：一套AscendCL接口可以实现应用代码统一，多款昇腾处理器无差异。

## 3.3 AscendCL 的主要应用场景

1.  开发应用：用户可以直接调用AscendCL提供的接口开发图片分类应用、目标识别应用等。 
2.  供第三方框架调用：用户可以通过第三方框架调用AscendCL接口，以便使用昇腾AI处理器的计算能力。 
3.  供第三方开发lib库：用户还可以使用AscendCL封装实现第三方lib库，以便提供昇腾AI处理器的运行管理、资源管理等能力。

## 3.4 AscendCL 的分层能力开放

AscendCL 提供的是分层开放能力的管控，通过不同的组件对不同的使能部件进行对接。包含 GE 能力开放、算子能力开放、Runtime 能力开放、Driver 能力开放等。

**模型加载能力开放**：处理om模型加载，但接口的开放是通过AscendCL。

**算子能力开放**：算子能力实现在CANN中，但算子能力开放是通过AscendCL。

**Runtime 能力开放**：处理基于stream的设备能力、内存、event等资源能力开发诉求，对app屏蔽底层实现。