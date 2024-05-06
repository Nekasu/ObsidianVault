# denoise过程在diffusion过程中的位置与作用

- denoise过程在diffusion过程中处于核心的地位, 其作用在于给噪声图像降噪, 如下图
	- ![[Pasted image 20231221105732.png]]
- 如果用“雕刻石像”作为例子的话, denoise过程的作用就是一点一点去除多余的石料的过程, 这个==一点一点==的过程, 可以用下图表示：
	- ![[Pasted image 20231221105817.png]]

# denoise过程的处理过程

## denoise过程的输入与输出


1. 输入：denoise过程接受3个参数作为输入
	1. 带有噪声的图像
	2. 当前的Step数
	3. 对于图像的文本描述 
2. 输出：denoise过程将输出一张「去除了一点噪声」的图像
3. 输入输出如下图所示
	1. ![[Pasted image 20231221144910.png|422]]
## denoise过程的内部

denoise过程内部按功能分可以分为两个部分
1. Noise Predicter模块
	1. 主要用于预测输入图像中「噪声」可能的样子, 并生成这个噪声
2. 降噪模块
	1. 用原图减去Noise Predicter模块产生的噪声, 从而达到降噪的目的
3. denoise过程的两个部分如下所示：
	1. ![[Pasted image 20231221152807.png]]

### Noise Predicter模块

1. 功能：主要用于预测输入图像中「噪声」可能的样子, 并生成这个噪声
2. 输入与输出
	1. 输入：Noise Predicter模块的输入就是denoise过程的输入, 也即有3个输入
		1. 带有噪声的图像
		2. 当前的Step数
		3. 对图像的文本描述
	2. 输出：「预测」输入图像中的「噪声」是什么样的
	3. 输入输出如下图所示：
		1. ![[Pasted image 20231221152712.png]]

### 降噪模块

降噪模块的功能如下：用原图减去Noise Predicter模块产生的噪声, 从而达到降噪的目的

1. 输入：降噪模块接受两个图像作为输入
	1. 原始的噪声图像
	2. noise predicter「预测」的输入图像中的「噪声」
2. 输出：将「原始的噪声图像」减去Noise Predicter产生的「预测噪声」, 将该结果作为降噪结果, 并输出
3. 如下图所示：
	1. ![[Pasted image 20231221153020.png]]

## denoise过程的工作流程

1. Step1：
	1. 接收下面三个, 作为输入
		1. 输入1：带有有噪声的图像
		2. 输入2：当前的Step数
		3. 输入3：对图像的文本描述
2. Step2：
	1. noise predicter模块：三个输入传入noise predicter中, 预测噪声
3. Step3：
	1. 降噪模块：用输入1减去第二步中得到的噪声结果, 并把该结果当作降噪结果, 完成降噪


# denoise过程的训练数据获取

denoise过程的训练其实就是noise predicter的训练, denoise过程中最核心的内容就是noise predicter

我们知道, noise predicter是以3个数据作为输入, 并输出一张噪声, 我们需要成对配套的输入输出, 也即成对的
1. 噪声图像
2. 文字描述
3. 当前的Step数
4. 噪声图像中的噪声

所以我们可以考虑向一张干净的图像中加入噪声, 这样就可以得到配套的上述四个数据, 如下图所示：

![[Pasted image 20231221201756.png]]

重复这个过程, 就可以得到noise predicter的训练数据, 如下图所示

![[Pasted image 20231221201828.png]]

用获取的数据对noise predicter进行训练即可, 如下所示：
- ![[Pasted image 20231221144910.png|422]]