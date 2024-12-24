
>[!warning] 提示
>点击右上角「书本」![[Pasted image 20231125105318.png]]图标, 进入阅读模式, 以获得更好的阅读体验！

# 利用「Jordan标准形」求矩阵函数的值

## 思想由来


在[[T3_7矩阵函数的定义#利用定义计算矩阵函数的值]]中, 我们提到了, 如果想要求矩阵函数的值, 关键的问题就是如何求一个高次的矩阵多项式的值

这个关键的问题其实我们在线性代数中遇到过.

在线性代数中, 我们学过, 高次幂的矩阵的值可以通过相似对角化来求, 其过程如下：
1. $$A=P^{-1}\Lambda P\implies A^{100} = \left( P^{-1}\Lambda P\right)^{100} = P^{-1}\Lambda^{100} P = P^{-1}\begin{bmatrix}\lambda_1^{100}& & & \\&\lambda_2^{100}& &\\&&\ddots&\\&&&\lambda_n^{100}\end{bmatrix}P$$
2. 在这个过程的基础上, 可以轻松的计算矩阵级数, 从而能够简单的计算矩阵函数的值, 如下所示：$$\begin{aligned}f(A)=&\sum_{k=0}^\infty c_kA^k\\ &= \sum_{k=0}^\infty c_k(P^{-1}\Lambda P)^k\\ &=\sum_{k=0}^\infty c_k P^{-1}\Lambda^{k} P\\ &=\sum_{k=0}^\infty c_kP^{-1}\begin{bmatrix}\lambda_1^{k}& & & \\&\lambda_2^{k}& &\\&&\ddots&\\&&&\lambda_n^{k}\end{bmatrix}P \\&=P^{-1} \begin{bmatrix}\sum\limits_{k=0}^\infty c_k\lambda_1^{k}& & & \\&\sum\limits_{k=0}^\infty c_k\lambda_2^{k}& &\\&&\ddots&\\&&&\sum\limits_{k=0}^\infty c_k\lambda_n^{k}\end{bmatrix}P\\ &= P^{-1}\begin{bmatrix} f(\lambda_1)& & & \\&f(\lambda_2)& &\\&&\ddots&\\&&&f(\lambda_n)\end{bmatrix}P \end{aligned}$$
3. 如此便可得到矩阵函数的值

## 一个问题

但是很显然, 并不是所有的矩阵都可以相似对角化

## 解决方案

###  初步演化

同时考虑到所有矩阵都有其[[1_Jordan标准形_索引文件|Jordan标准形]], 所以考虑是否能通过将矩阵化成Jordan标准形, 在Jordan标准形的基础上计算矩阵级数的值, 从而计算矩阵函数的值

- 在此这个思想的指导下, 我们仿照[[O4_利用「Jordan标准形」求矩阵函数的值#思想由来|上面介绍的流程]], 利用Jordan标准形进行类似的化简

设矩阵$A$相似于Jordan标准形$J$, 且有$A=P^{-1}JP$ , 则矩阵函数的计算过程如下$$\begin{aligned}f(A) &= \sum_{k=0}^\infty c_kA^k = \sum_{k=0}^\infty c_k(P^{-1}JP)^k\\ &= \sum_{k=0}^\infty c_kP^{-1}J^kP \\ &= P^{-1}\sum\limits_{k=0}^\infty c_kJ^k P \\ &= P^{-1} \begin{bmatrix}\sum\limits_{k=0}^\infty c_kJ_1^k & & & &\\&\sum\limits_{k=0}^\infty c_kJ_2^k&&\\&&\ddots&\\&&&\sum\limits_{k=0}^\infty c_kJ_s^k\end{bmatrix} P \\ &= P^{-1} \begin{bmatrix}f(J_1) & & & &\\&f(J_2)&&\\&&\ddots&\\&&&f(J_s)\end{bmatrix} P \end{aligned}\quad (1)$$

计算到这里, 如何计算$f(J_i)$成为了一个关键

### 深入考察：$f(J_i)$的计算

$f(J_i)$是一个矩阵函数, 而在[[T3_7矩阵函数的定义#利用定义计算矩阵函数的值]]中, 我们提到了, 如果想要求矩阵函数的值, 就需要将这个矩阵函数展开成级数的形式.$$f(J_i)=\sum\limits_{k=0}^\infty c_kJ_i^{k}$$
- 计算Jordan块的$n$次方的结果如下
	- 由于证明过程太长且不复杂, 所以此处仅给出思路与结论
		- 思路：[[A1_7_计算Jordan块的n次方#计算Jordan块的n次方的思路]]
		- 结论：[[A1_7_计算Jordan块的n次方#Jordan块的n次方的结果]]

因此, 上式可继续演化$$\begin{aligned} f\left(\boldsymbol{J}_{\imath}\right)&=\sum_{k=0}^{\infty} c_{k} \boldsymbol{J}_{i}^{k}\\&=\sum_{k=0}^{\infty} c_{k}\left[\begin{array}{cccc}\lambda_{i}^{k} & \mathrm{C}_{k}^{1} \lambda_{i}^{k-1} & \cdots & \mathrm{C}_{k^{2}}^{m_{1}-1} \lambda_{i}^{k-m_{\mathrm{t}}+1} \\& \lambda_{i}^{k} & \ddots & \vdots \\& & \ddots & \mathrm{C}_{k}^{1} \lambda_{i}^{k-1} \\& & & \lambda_{i}^{k}\end{array}\right]\\&=\left[\begin{array}{cccc}f\left(\lambda_{i}\right) & \frac{1}{1 !} f^{\prime}\left(\lambda_{i}\right) & \cdots & \frac{1}{\left(m_{i}-1\right) !} f^{\left(m_{i}- 1\right)}\left(\lambda_{i}\right) \\& f\left(\lambda_{i}\right) & \ddots & \vdots \\& & \ddots & \frac{1}{1 !} f^{\prime}\left(\lambda_{i}\right) \\& & & f\left(\lambda_{t}\right)\end{array}\right]\end{aligned}$$
其中$f^{(m_i-1)}$是函数的$m_i-1$阶导数

在将$f(J_i)$计算完毕后, 利用Jordan标准形求矩阵函数的值也变的可行了

### 结论

使用Jordan标准形求矩阵函数的值的思想如下：

1. $$\begin{aligned}f(A)  = P^{-1} \begin{bmatrix}f(J_1) & & & &\\&f(J_2)&&\\&&\ddots&\\&&&f(J_s)\end{bmatrix} P \end{aligned}$$其中$$
f\left(\boldsymbol{J}_{\imath}\right)=\left[\begin{array}{cccc}
f\left(\lambda_{i}\right) & \frac{1}{1 !} f^{\prime}\left(\lambda_{i}\right) & \cdots & \frac{1}{\left(m_{i}-1\right) !} f^{\left(m_{i} -1\right)}\left(\lambda_{i}\right) \\
& f\left(\lambda_{i}\right) & \ddots & \vdots \\
& & \ddots & \frac{1}{1 !} f^{\prime}\left(\lambda_{i}\right) \\
& & & f\left(\lambda_{t}\right)
\end{array}\right]$$

直接代入上述公式即可利用Jordan标准形求解矩阵函数的值

# 记忆方法

这个式子$\begin{aligned}f(A)  = P^{-1} \begin{bmatrix}f(J_1) & & & &\\&f(J_2)&&\\&&\ddots&\\&&&f(J_s)\end{bmatrix} P \end{aligned}$ 记忆比较简单, 与$P^{-1}\begin{bmatrix} f(\lambda_1)& & & \\&f(\lambda_2)& &\\&&\ddots&\\&&&f(\lambda_n)\end{bmatrix}P$较为类似

难以记忆的是$$f\left(\boldsymbol{J}_{\imath}\right)=\left[\begin{array}{cccc}
f\left(\lambda_{i}\right) & \frac{1}{1 !} f^{\prime}\left(\lambda_{i}\right) & \cdots & \frac{1}{\left(m_{i}-1\right) !} f^{\left(m_{i} -1\right)}\left(\lambda_{i}\right) \\
& f\left(\lambda_{i}\right) & \ddots & \vdots \\
& & \ddots & \frac{1}{1 !} f^{\prime}\left(\lambda_{i}\right) \\
& & & f\left(\lambda_{t}\right)
\end{array}\right]$$

其实这个式子记忆起来也比较简单, 一句话概括,  就是
- Jordan块中的$k$级隆起上的值是一样的, 为$\frac{1}{k!}f^{(k)}(\lambda_i)$ 
	- 如果觉得这句话难以理解的话, 请看图片 
		- ![[01e0857f97b3991f4e3ac95c845bc48.jpg]]


# 实际操作

在操作过程中, 如何利用矩阵$A$的Jordan标准形求矩阵函数$f(A)$的值呢？

1. step1 求Jordan块
	1. 求矩阵$A$的[[1_Jordan标准形_索引文件|Jordan标准形]]与可逆矩阵$P$ 
2. step2 求$f(Jordan块)$ 
	1. 将$f(A)$写成$f(x)$, 计算函数$f(x)$的$1\sim n$阶导数
	2. 利用公式求$f(J_i)$ , 将特征值$\lambda$代入$f(x)$的$1\sim n$阶导数中, 获得隆起上的值
		1. $$f\left(\boldsymbol{J}_{\imath}\right)=\left[\begin{array}{cccc}
f\left(\lambda_{i}\right) & \frac{1}{1 !} f^{\prime}\left(\lambda_{i}\right) & \cdots & \frac{1}{\left(m_{i}-1\right) !} f^{\left(m_{i} -1\right)}\left(\lambda_{i}\right) \\
& f\left(\lambda_{i}\right) & \ddots & \vdots \\
& & \ddots & \frac{1}{1 !} f^{\prime}\left(\lambda_{i}\right) \\
& & & f\left(\lambda_{t}\right)
\end{array}\right]$$
		2. 注意！$f(Jordan块)$中的值与函数$f$, 隆起的阶数以及$\lambda_i$有关, 与Jordan块中原来位置上的值无关
		3. 
1. step3 将$f(Jordan块)$写在一起
	1. $$\begin{aligned}f(A)  = P^{-1} \begin{bmatrix}f(J_1) & & & &\\&f(J_2)&&\\&&\ddots&\\&&&f(J_s)\end{bmatrix} P \end{aligned}$$


如果现在要求$f(At)$的值, 应该如何计算？其主要变化的上述的第二步中. 在操作中, 我们一般将$t$看作一个与函数无关的常量, 这个常量对整个计算过程的影响在于其对$f(J_i)$的计算产生了影响, 第二步的具体操作变成如下形式：

1. 将$f(At)$写成$f(x)$, 计算函数$f(x)$的$1\sim n$阶导数
2. 将特征值$\lambda$代入$f(x)$的$1\sim n$阶导数中, 获得隆起上的值
3. 写出$f(Jordan块)$ 
		1. $$f\left(\boldsymbol{J}_{\imath}\right)=\left[\begin{array}{cccc}
f\left(\lambda_{i}\right) & \frac{1}{1 !} f^{\prime}\left(\lambda_{i}\right) & \cdots & \frac{1}{\left(m_{i}-1\right) !} f^{\left(m_{i} -1\right)}\left(\lambda_{i}\right) \\
& f\left(\lambda_{i}\right) & \ddots & \vdots \\
& & \ddots & \frac{1}{1 !} f^{\prime}\left(\lambda_{i}\right) \\
& & & f\left(\lambda_{t}\right)
\end{array}\right]$$

用一个例子来解释这个过程, 假设现在有一个矩阵$$A=\begin{bmatrix}0&1&1\\0&0&1\\0&0&0\end{bmatrix}$$试求$\cos (At)$ 

1. 求矩阵$A$的Jordan标准形
	1. $$P^{-1}AP= J = \begin{bmatrix}0&1&1\\0&0&1\\0&0&0\end{bmatrix}, P=I$$
2. 求$f(Jordan块)$ 
	1. 将$f(At)$写成$f(x)$, 计算函数$f(x)$的$1\sim n$阶导数
		1. $\cos (At)\implies f(x)=\cos(xt)$, $f'(x)=-t\sin xt, f''(x)=-t^2\cos xt$ 
	2. 将特征值$\lambda$代入$f(x)$的$0\sim n$阶导数中, 获得隆起上的值
		1. $f(0)=1, f'(0)=-t\sin 0t=0, f''(x)=-t^2\cos 0t=-t^2$  
	3.  写出$f(Jordan块)$ 
		1. $$f\left(\boldsymbol{J}_{\imath}\right)=\begin{bmatrix}1&0&-\frac{1}{2}t^2\\0&1&0\\0&0&1\end{bmatrix}$$
3. 将$f(Jordan块)$写在一起
	1. $$\begin{aligned}f(At)  = P^{-1} \begin{bmatrix}f(J_1) \end{bmatrix} P =f\left(\boldsymbol{J}_{\imath}\right)=\begin{bmatrix}1&0&-\frac{1}{2}t^2\\0&1&0\\0&0&1\end{bmatrix}\end{aligned}$$