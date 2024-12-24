Jordan引理这个名字是作者自己起的，实际上书上并没有写这个定理的名字

用一句话描述这个定理, 就是“所有线性变换对应的矩阵$A$张成的空间<mark style="background: #FFB8EBA6;">都可以拆分</mark>为多个线性空间的直和”, 结合[[D1_27线性变换的矩阵与“组合基”]]定理, 就能推出所有$A$都相似于一个上三角的分块对角阵

书上<mark style="background: #FF5582A6;">不加证明的</mark>给出了这个定理， 其表述如下

# 一些参数假设

1. $T$为线性空间$V^n$上的一个线性变换
2. 矩阵$A$为线性变换$T$在$V^n$任意一个基下的矩阵

# 一个条件

如果矩阵$A$的特征多项式可以因式分解为$$\begin{aligned}\varphi(\lambda)=(\lambda-\lambda_1)^{m_1}(\lambda-\lambda_2)^{m_2}\cdots(\lambda-\lambda_s)^{m_s}\\(\lambda_i\text{与}\lambda_j\text{之间可能相同}, m_1+m_2+\cdots+m_n=n)\end{aligned}$$

# 一个结论

那么$V_n$可以分解成$m$个子空间的直和, 即$$V_N = N_1\oplus N_2 \oplus \cdots \oplus N_m,$$其中$N_i$是矩阵$A$的特征值$\lambda_i$的特征空间, 即$$N_i=\left\{x_i\mid Tx=\lambda_i x, x\in V_n\right\}$$

# 结论的推论

根据[[D1_27线性变换的矩阵与“组合基”]]可知, 如果一个线性空间$V_n$可以分解成$m$个空间的直和, 那么这个空间与一个“准对角阵（分块对角阵）”相似, 所以可以知道$$A\sim \text{分块对角阵},$$同时, 任意矩阵相似与一个上三角阵, 所以该空间$V_n$可以相似与一个上三角的分块对角阵, 即$$A\sim J, J=\begin{bmatrix}J_1(\lambda_1)& & & \\ & J_2(\lambda_2)& &  \\ & & \ddots& \\ & & & J_s(\lambda_s)\end{bmatrix}$$其中$J$是一个$n\times n$的上三角的分块对角矩阵； $J_i(\lambda_i)$是一个$m_i \times m_i$的矩阵, 且$$J_i(\lambda_i)=\begin{bmatrix}\lambda_i
&1& & & \\ & \lambda_i&1& & \\& & \lambda_i&\ddots& \\& & & \ddots&1\\& & & & \lambda_i\end{bmatrix}_{m_i\times m_i}$$ 