
>[!warning] 提示
>点击右上角「书本」![[Pasted image 20231125105318.png]]图标, 进入阅读模式, 以获得更好的阅读体验！

# 矩阵A(t)的导数

1. 参数设定
	1. 自变量$t$
	2. $m\times n$阶矩阵$A(t)$ 
		1. 其中$t$表示矩阵中的每个元素都是以$t$为自变量的函数
		2. 如果矩阵中存在常数, 也应该将其看作$t$的函数
	3. 矩阵$A(t)$ 的每一个元素$a_{ij}(t)$
2. 条件
	1. 如果$a_{ij}(t)$都是$t$的可微函数
3. 结论
	1. 称$A(t)$是可微的
	2. 且$A(t)$的导数定义为其中每一个元素单独对$t$进行求导, 即$$A(t)'=\frac{\mathrm{d}A(t)}{\mathrm{d}t}=\left(\frac{\mathrm{d}}{\mathrm{d}t}a_{ij}(t)\right)_{m\times n}=\begin{bmatrix} \frac{\mathrm{d}a_{11}(t)}{\mathrm{d}t}&\frac{\mathrm{d}a_{12}(t)}{\mathrm{d}t}&\cdots&\frac{\mathrm{d}a_{1n}(t)}{\mathrm{d}t}\\  \frac{\mathrm{d}a_{21}(t)}{\mathrm{d}t}&\frac{\mathrm{d}a_{22}(t)}{\mathrm{d}t}&\cdots&\frac{\mathrm{d}a_{2n}(t)}{\mathrm{d}t}\\   \vdots&\vdots&\vdots&\vdots\\   \frac{\mathrm{d}a_{m1}(t)}{\mathrm{d}t}&\frac{\mathrm{d}a_{m2}(t)}{\mathrm{d}t}&\cdots&\frac{\mathrm{d}a_{mn}(t)}{\mathrm{d}t}\end{bmatrix}$$ 
