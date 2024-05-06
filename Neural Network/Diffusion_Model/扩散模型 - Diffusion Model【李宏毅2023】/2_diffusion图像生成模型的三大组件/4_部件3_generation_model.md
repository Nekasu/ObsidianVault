
>[!warning] 提示
>点击右上角「书本」![[Pasted image 20231125105318.png]]图标, 进入阅读模式, 以获得更好的阅读体验！


# Generation Model功能

1. Generation Model, 图像生成器, denoise过程
	1. 输入：文字的**向量**、噪声图像
	2. 输出：**中间图像**
		1. 一般是压缩的图像或特征图
	3. 主要功能：理解文字的向量, 并根据**向量**生成对应的**中间图像**
		1. 此模块担任的功能, 就是diffusion图像生成过程中的[[2_denoise过程介绍|denoise过程]] 

图中蓝色方框圈起来的模块为generation_model
- ![[Pasted image 20231221203950.png|474]]


# Generation Model的训练

## denoise过程与generation model

由于Generation Model代表的是[[2_denoise过程介绍|denoise过程]], 所以其训练过程也与denoise过程类似, 区别仅在于输入输出不同

denoise过程的训练就是noise predicter的训练, generation model的训练也是noise predicter的训练

我们将二者进行类比, 先给出[[2_denoise过程介绍|denoise过程]]的训练步骤, 再仿照此完成Generation Model中noise predicter的训练

## denoise过程的训练

![[2_denoise过程介绍#denoise过程的训练数据获取]]

1. denoise过程
	1. 输入：denoise模块接受3个参数作为输入
		1. 带有噪声的图像
		2. 当前的Step数
		3. 对于图像的文本描述 
	2. 输出：denoise模块将输出一张「去除了一点噪声」的图像
2. generation model
	1. 输入：generation model接收3个参数作为输入
		1. 带有噪声的图像
		2. 当前的Step数
		3. Text Encoder产生的文字向量
	2. 输出
		1. 中间图像

## generation model的训练数据的获取

generation model的训练其实就是noise predicter的训练, generation model中最核心的内容就是noise predicter

我们知道, noise predicter是以3个数据作为输入, 并输出一张噪声, 我们需要成对配套的输入输出, 也即成对的
1. 带有噪声的**中间图像**
2. 当前的Step数
3. Text Encoder产生的文字向量
4. 带有噪声的中间图像中的噪声

所以我们可以考虑向一张干净的**中间图像**中加入噪声, 这样就可以得到配套的上述四个数据, 如下图所示：

![[Pasted image 20231222170631.png|292]]

重复这个过程, 就可以得到noise predicter的训练数据, 如下图所示

![[Pasted image 20231222170651.png]]

用获取的数据对noise predicter进行训练即可, 如下所示：
- ![[Pasted image 20231222170714.png|448]]