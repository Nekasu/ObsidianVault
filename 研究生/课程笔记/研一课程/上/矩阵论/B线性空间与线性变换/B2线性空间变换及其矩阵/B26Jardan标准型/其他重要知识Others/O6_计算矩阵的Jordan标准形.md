在复数域$C$上, 求矩阵$A$的Jordan标准形的步骤如下

# 计算机方法

在用计算机计算Jordan标准形时, 需要一个“死板”的而非“灵活”的方法, 具体计算过程如下

## Step1 求不变因子与初等因子组

1. [[O3_不变因子的定义及其求法：计算Jordan标准形的前置知识3|求不变因子]]  
2. [[O4_初等因子组及其求法：计算Jordan标准形的前置知识4|求初等因子组]]
	1. 不妨设求出初等因子组为$$(\lambda-\lambda_1)^{m_1},(\lambda-\lambda_2)^{m_2},\cdots,(\lambda-\lambda_s)^{m_s}$$
## Step2 写出每个初等因子对应的Jordan块

对于初等因子$(\lambda-\lambda_i)^{m_i}$, 有对应的Jordan块$$J_i(\lambda_i)=\begin{bmatrix}\lambda_i
&1& & & \\ & \lambda_i&1& & \\& & \lambda_i&\ddots& \\& & & \ddots&1\\& & & & \lambda_i\end{bmatrix}_{m_i\times m_i}$$也即初等因子的代数重数为Jordan块的维度(希望每个几何重数为$m_i$的特征值都能张成一个$m_i$维空间) 

## Step3 将Jordan块写成Jordan标准形

很简单, 不赘述

$$A\sim J, J=\begin{bmatrix}J_1(\lambda_1)& & & \\ & J_2(\lambda_2)& &  \\ & & \ddots& \\ & & & J_s(\lambda_s)\end{bmatrix}$$

## 求P

不妨设$P^{-1}AP =  J=\begin{bmatrix}1& 1& \\ & 1&  \\ & & 1\end{bmatrix}$

则有$AP=PJ$

设$P = \begin{bmatrix}\vec{x_1}&\vec{x_2}&\vec{x_3}\end{bmatrix}$ 

则有$$AP =  \begin{bmatrix}A\vec{x_1}&A\vec{x_2}&A\vec{x_3}\end{bmatrix}, $$$$PJ = \begin{bmatrix}\vec{x_1}&\vec{x_2}&\vec{x_3}\end{bmatrix}\cdot\begin{bmatrix}1& 1& \\ & 1&  \\ & & 1\end{bmatrix}=\begin{bmatrix}\vec{x_1}&\vec{x_1}+\vec{x_2}&\vec{x_3}\end{bmatrix}$$
将上面两式带入$AP=PJ$, 有$$\begin{bmatrix}A\vec{x_1}&A\vec{x_2}&A\vec{x_3}\end{bmatrix}=\begin{bmatrix}\vec{x_1}&\vec{x_1}+\vec{x_2}&\vec{x_3}\end{bmatrix}$$

则有一一对应关系如下：$$\begin{aligned}A\vec{x_1}&=x_1\\A\vec{x_2}&=\vec{x_1}+\vec{x_2}\\A\vec{x_3}&=\vec{x_3}\end{aligned}$$
移项, 有$$\begin{aligned}(A-I)\vec{x_1}&=\vec{0}\\(A-I)\vec{x_2}&=\vec{x_1}\\(A-I)\vec{x_3}&=\vec{0}\end{aligned}$$

第一和第三个式子为特征值$1$对应的特征向量

由第二个式子$(A-I)\vec{x_2}=\vec{x_1}$可知, $\vec{x_1}=(A-I)\vec{x_2}$, 代入到第一个式子$(A-I)\vec{x_1}=\vec{0}$ 中, 有$$(A-I)^2\vec{x_2}=\vec{0}$$

称这个向量$x_2$为广义特征向量


# 手算Jordan标准形的方法--利用初等行列变换

如果需要用手计算Jordan标准形, 那么在计算四阶矩阵的三阶子式时过于复杂, 因此可以考虑使用其他方法「手算」Jordan标准形, 具体方法如下：

## Step1：求矩阵的不变因子与初等因子组

可以使用初等**行列**变换的方式求解矩阵的初等因子组
- 注意, 可以使用**行变换**与**列变换**, 二者可以同时使用

以矩阵$A=\begin{bmatrix}3&0&1&0\\0&2&0&0\\1&1&3&0\\0&1&0&2\end{bmatrix}$为例, 用初等「行列」变换求解Jordan标准形的过程如下：

1. 计算$A-\lambda I$并做初等行列变换
	1. $$\begin{aligned}A-\lambda I&=\begin{bmatrix}3-\lambda&0&1&0\\0&2-\lambda&0&0\\1&1&3-\lambda&0\\0&1&0&2-\lambda\end{bmatrix}\\  &\xrightarrow[]{l_1\leftrightarrow l_3}\begin{bmatrix}1&1&3-\lambda&0\\0&2-\lambda&0&0\\3-\lambda&0&1&0\\0&1&0&2-\lambda\end{bmatrix}\\  &\xrightarrow[]{l_3-(3-\lambda) l_1}\begin{bmatrix}1&1&3-\lambda&0\\0&2-\lambda&0&0\\0&\lambda-3&(\lambda-2)(4-\lambda)&0\\0&1&0&2-\lambda\end{bmatrix}\\  &\xrightarrow[]{l_2\leftrightarrow l_4} \begin{bmatrix}1&1&3-\lambda&0\\0&1&0&2-\lambda\\0&\lambda-3&(\lambda-2)(4-\lambda)&0\\0&2-\lambda&0&0\end{bmatrix}\\ &\xrightarrow[l_3-(\lambda-3)l_2, \quad l_4-(2-\lambda)l_2]{l_1-l_2}\begin{bmatrix}1&0&3-\lambda&\lambda-2\\   0&1&0&2-\lambda\\0&0&(\lambda-2)(4-\lambda)&0\\9&0&0&-(2-\lambda)^2\end{bmatrix}\\ &\xrightarrow[c_4-(\lambda-2)c_1-(2-\lambda)c_2]{c_3-(3-\lambda)c_1}\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&(\lambda-2)(4-\lambda)&(\lambda-2)(\lambda-3)\\0&0&0&-(2-\lambda)^2\end{bmatrix}\\  &\rightarrow\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&(\lambda-2)(4-\lambda)&0\\0&0&0&-(2-\lambda)^2\end{bmatrix}\end{aligned}$$ 
2. 对角线上的元素即为[[O3_不变因子的定义及其求法：计算Jordan标准形的前置知识3|不变因子]]
3. 在求得不变因子后, 即可写出Jordan标准形