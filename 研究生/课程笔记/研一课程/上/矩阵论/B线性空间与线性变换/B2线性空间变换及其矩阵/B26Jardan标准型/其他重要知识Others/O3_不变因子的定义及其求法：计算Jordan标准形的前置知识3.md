# 不变因子的定义

在[[O2_多项式矩阵的标准形：计算Jordan标准形的前置知识2|多项式矩阵的标准形]]中, 对角线上的元素被称作这个矩阵的“不变因子”
- 是因为这些因子不会因“将多项式矩阵化为标准形时步骤的改变”而改变, 正是因为其“不变性”, 故而将其称作“不变因子”

如在![[O2_多项式矩阵的标准形：计算Jordan标准形的前置知识2]]中, $d_1(\lambda),d_2(\lambda),\cdots,d_s(\lambda)$被称作不变因子

# 不变因子的求法

# 可以用定义求

即将[[O1_多项式矩阵：计算Jordan标准形的前置知识1|多项式矩阵]]化成[[O2_多项式矩阵的标准形：计算Jordan标准形的前置知识2|标准形]], 取对角线上的元素

## 可以用公式求

### 符号定义

1. 设$D_i(\lambda)$是多项式矩阵$A(\lambda)$的[[一些线性代数的基本名词#n-1阶子式|i阶子式]]的最大公因子 ($i=1,2,3,\cdots, n$)

### 一个前提

求出$D_1(\lambda), D_2(\lambda),\cdots, D_n(\lambda)$, 并令$D_0(\lambda)=1$

### 一个结论/公式

那么不变因子$$d_i(\lambda)=\frac{D_i(\lambda)}{D_{i-1}(\lambda)}$$举例来说, 有$$\begin{aligned}d_1(\lambda)&=\frac{D_1(\lambda)}{D_{0}(\lambda)},\\d_2(\lambda)&=\frac{D_2(\lambda)}{D_{1}(\lambda)},\\d_3(\lambda)&=\frac{D_3(\lambda)}{D_{2}(\lambda)},\\\vdots\end{aligned}$$
