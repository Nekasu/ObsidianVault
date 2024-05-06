
>[!warning] 提示
>点击右上角「书本」![[Pasted image 20231125105318.png]]图标, 进入阅读模式, 以获得更好的阅读体验！

# 计算Jordan块的n次方的思路

思路如下

将Jordan写成$\lambda_i I+M$的形式, 再利用二项式定理计算$J_i^k=(\lambda_i I+M)^k$ 
- 其中$\lambda_i$为当前Jordan块的特征值
- $I$为单位阵
- $M$为一个特征值为$0$的Jordan块
- 将$\lambda_i I+M$展开写, 就是如下的形式$$\begin{aligned} J_i(\lambda_i)&=\begin{bmatrix}\lambda_i&1& & & \\ & \lambda_i&1& & \\& & \lambda_i&\ddots& \\& & & \ddots&1\\& & & & \lambda_i\end{bmatrix}\\&=\lambda_i\begin{bmatrix}\lambda_i&1& & & \\ & \lambda_i&1& & \\& & \lambda_i&\ddots& \\& & & \ddots&1\\& & & & \lambda_i\end{bmatrix}+ \begin{bmatrix}0&1& & & \\ & 0&1& & \\& & 0&\ddots& \\& & & \ddots&1\\& & & & 0\end{bmatrix}\\&=\lambda_i I+M \end{aligned}$$

# Jordan块的n次方的结果

1. 当$k<$Jordan块的维度$m_i$时,$$\boldsymbol{J}_{t}^{k}=(\lambda_i I+M)^k=\left[\begin{array}{cccc}
\lambda_{i}^{k} & \mathrm{C}_{k}^{1} \lambda_{i}^{k-1} & \cdots & \mathrm{C}_{k^{2}}^{m_{1}-1} \lambda_{i}^{k-m_{\mathrm{i}}+1} \\
& \lambda_{i}^{k} & \ddots & \vdots \\
& & \ddots & \mathrm{C}_{k}^{1} \lambda_{i}^{k-1} \\
& & & \lambda_{i}^{k}
\end{array}\right]$$
2. 当$k>$Jordan块的维度$m_i$时,$\boldsymbol{J}_{t}^{k}=O$
	1. 即零矩阵

