#  Hermite变换的定义

线性空间$V$上的线性变换$T$满足$$(Tx,y)=(x,Ty),(x,y\in V)$$
则称该变换$T$为对称变换

# Hermite矩阵的定义

如果一个矩阵$A$满足$$A^H=A$$则称该矩阵为Hermite阵


# Hermite阵的性质

Hermite矩阵可以视作对称矩阵的一种特殊形式. 类似的, Hermite矩阵具有两个性质
1. Hermite矩阵的特征值都是实数
	1. $$\begin{aligned}Ax=\lambda x &\implies x^HAx = x^H\lambda x \end{aligned},$$对上式取转置, 有$$\left(x^HAx\right)^H = \left(x^H\lambda x\right)^H\implies x^HA^Hx =x^H\lambda^H x$$将上面两个式子联立, 有$$x^HAx = x^H\lambda x =x^H\lambda^H x$$取后面两项, 并移项, 有$$\left(\lambda-\lambda_H\right)x^Hx=0,$$而由于向量$x$是特征向量, 所以$x$不为零向量, 所以$x^Hx > 0$, 所以$\lambda - \lambda^H=0$,所以$\lambda$为实数
2. 属于Hermite矩阵不同特征值的特征向量「相互正交」