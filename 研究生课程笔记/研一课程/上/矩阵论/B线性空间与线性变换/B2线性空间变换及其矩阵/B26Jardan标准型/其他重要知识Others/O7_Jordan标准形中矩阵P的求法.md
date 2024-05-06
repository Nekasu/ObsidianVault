由于证明较为复杂, 此处仅以例子给出求法

# 参数假设

设Jordan标准形为$$J=\begin{bmatrix}\lambda_1&0&0\\0&\lambda_2&1\\0&0&\lambda_2\end{bmatrix}$$


# 求法介绍


以三阶矩阵为例, 根据[[T1_28Jardan引理]], 可知, 有$$J= P^{-1}AP$$移项, 有 $$AP=JP$$ 
不妨设$P=\begin{bmatrix}x_1&x_2&x_3\end{bmatrix},$代入$AP=PJ$有  $$A\begin{bmatrix}x_1&x_2&x_3\end{bmatrix}=\begin{bmatrix}x_1&x_2&x_3\end{bmatrix}\begin{bmatrix}\lambda_1&0&0\\0&\lambda_2&1\\0&0&\lambda_2\end{bmatrix}$$展开, 有$$\begin{bmatrix}Ax_2&Ax_2&Ax_3\end{bmatrix}=\begin{bmatrix}\lambda_1x_1&\lambda_2x_2&x_2+\lambda_3x_3\end{bmatrix}$$写成方程, 有$$\begin{cases}Ax_1&=\lambda_1x_1\\Ax_2&=\lambda_2x_2\\Ax_3&=x_2+\lambda_3x_3\end{cases}$$移项, 有$$\begin{cases}(A-\lambda_1I)x_1&=0\\(A-\lambda_2I)x_2&=0\\(A-\lambda_3I)x_3&=x_2\end{cases}$$
解方程即可
 