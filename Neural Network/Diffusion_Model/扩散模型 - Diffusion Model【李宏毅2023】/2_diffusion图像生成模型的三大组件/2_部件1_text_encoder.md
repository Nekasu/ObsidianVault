
>[!warning] 提示
>点击右上角「书本」![[Pasted image 20231125105318.png]]图标, 进入阅读模式, 以获得更好的阅读体验！

# Text-encoder的功能

1. Text Encoder, 文字编码器, 预处理过程
	1. 输入：对图像的**描述性文字**
	2. 输出：向量
	3. 主要功能：将描述性**文字**改写成**向量**
		4. 可以看作是[[2_denoise过程介绍|denoise过程]]的预处理, 将「人类的自然语言」处理成[[2_denoise过程介绍|denoise过程]]看得懂的样子

图中红色方框圈起来的模块为Text Encoder
- ![[Pasted image 20231221203950.png|474]]

我们可以选择GPT当作Text-encoder


# 文字编码器Text Encoder对图像生成的效果的影响较大

给出一张实验数据图

![[Pasted image 20231221204656.png]]

上面这张实验数据图中可以直接看出：
1. 左图：Text Encoder性能的优劣、模块的大小能直接影响图像生成的效果
	1. 横坐标：[[2_CLIP_Score|CLIP SCORE]]
	2. 纵坐标：[[1_FID|FID]]-10k
		1. 表示用10k张图像测试出的FID值
2. 右图：图像生成模块的大小对图像生成效果的影响较小
	1. 横坐标：[[2_CLIP_Score|CLIP SCORE]]
	2. 纵坐标：[[1_FID|FID]]
		1. 表示用10k张图像测试出的FID值