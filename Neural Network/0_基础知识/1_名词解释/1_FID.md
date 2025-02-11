
>[!warning] 提示
>点击右上角「书本」![[Pasted image 20231125105318.png]]图标, 进入阅读模式, 以获得更好的阅读体验！

# 什么是FID

一句话描述：一个评价**生成的图像的效果好坏**的指标

具体来说, FID(Fréchet Inception Distance)的计算过程如下：
1. 准备工作
	1. 需要一个训练好的CNN特征提取器
	2. 两张图像：一张是生成的图像、一张是真实的图像
2. 计算流程
	1. 将**生成的图像**与**真实的图像**丢入**CNN**中
	2. 计算上述两个图像的**特征图**
		1. 假设这两个图像的特征均满足高斯分布
	3. 判断生成图像与真实图像**高斯分布**之间的**差距**, 这个差距即为**FID**
		1. 如果差距较**小**, 说明生成的图像较为**接近真实图像**
		2. 如果差距较**大**, 说明生成的图像**与真实图像**之间相似度较低

上述过程说明, FID越小, 说明生成图像越接近真实图像, 效果也就越好
- 需要注意的是, 如果生成的是艺术图像, 那么输入的真实图像也应该是艺术图像, 如果输入的是照片图像, 那么FID的差距一定很大
- 也即, 真实图像可以是**艺术图像**, 也可以是**写实照片图像**

# FID-10K

FID后面跟着的数字表示：使用了多少张对应图像测试FID, 10K表示使用了10000对图像进行FID的计算