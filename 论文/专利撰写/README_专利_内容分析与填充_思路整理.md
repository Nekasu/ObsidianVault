本文件用于思考如何撰写专利, 以现有的三份专利作为参考, 力求弄清如何撰写专利. 主要任务有以下几个：

1. [x] 弄清专利的撰写思路
2. 确定自己专利的撰写思路
3. 找到撰写专利时, 需要确定使用的技术, 并根据技术需求确定当前所缺少的内容、参考文献等资料.

## 专利内容总结

[[郑钰辉专利分析]]

## 专利撰写套路

[[专利撰写套路]]

## 个人专利撰写

### 第一部分：总体步骤

基于中国传统艺术作品中背景与主体内容差别较大的特点, 将风格图像输入显著目标检测模块, 以区分风格图像的主体部分与背景部分, 从而实现分离风格图像中不同风格部分的目的.

基于内容图像中场景与主体多而杂、相同主体基本处于相同深度的特点, 构建深度估计机制, 将内容图像输入深度估计模块, 再根据摄影图像拍摄自不同相机模型的模糊性, 构建标准相机空间变换, 利用标准相机变换与去标准化操作估计内容图像中的深度信息, 以实现内容图像中不同场景分离的目的.

对于上述两个步骤得到的数据, 鉴于中国传统风格画具有背景与主体相互独立的艺术特点, 尝试分别以风格图像主体部分与背景部分作为指导, 构建对象独立的风格迁移流程. 

对于风格主体对象, 基于其纹理特征明显的特点, 以傅里叶变换与深度卷积特征通道的风格分离属性为基础, 提取风格主体对象的风格特征, 并设计损失函数, 对主体对象的迁移结果进行训练, 以得到风格化主体对象迁移结果.

对与风格背景对象, 基于其颜色单一的特点, 结合内容背景对象包含较多复杂对象的特点, 以背景散焦与自适应实例归一化为基础, 调整内容背景对象的清晰度与风格信息, 以得到风格化背景对象迁移结果.

获取风格化主体对象与风格化主体对象后, 以原始内容图像作为参考, 对风格化主体对象迁移结果与风格化背景对象迁移结果进行归一化操作, 缩小二者之间的风格差异, 并进行最终合并操作.

最终得到对象独立的中国传统风格迁移网络.

### 第二部分：详细步骤

#### 步骤 1

步骤 1, 基于中国传统艺术作品中背景与主体内容差别较大的特点, 将风格图像输入显著目标检测模块, 以区分风格图像的主体部分与背景部分, 从而实现分离风格图像中不同风格部分的目的.

步骤 101 , 使用显著性检测网络 $D_{\text{sal}}$ 对风格图像 $S$ 进行处理, 获得显著性图 $M_{\text{sal}}$, 用于表示每个像素值属于主体的概率. 公式如下：
$$
M_{\text{sal}}=D_{\text{sal}}(S)
$$

步骤 102, 根据步骤 101 得到的显著性图 $M_{\text{sal}}$, 将风格图像 $S$ 分离为主体部分 $S_m$ 与背景部分 $S_b$, 公式如下：

$$
S_m = S \odot M_{\text{sal}}, S_b = S\odot (1-M_{\text{sal}})
$$
其中, $\odot$ 表示逐元素相乘.

#### 步骤 2

步骤 2, 基于内容图像中场景与主体多而杂、相同主体基本处于相同深度的特点, 构建深度估计机制, 将内容图像输入深度估计模块, 再根据摄影图像拍摄自不同相机模型的模糊性, 构建标准相机空间变换, 利用标准相机变换与去标准化操作估计内容图像中的深度信息, 以实现分离内容图像为兴趣区域图像与非兴趣区域图像的目的.

步骤 201, 对输入的内容图像 $C$ 进小波分解, 得到低频分量 $L$ 与高频分量 $H$, 公式如下：
$$
C = \mathcal{W}^{-1}(L,H)
$$
其中 $\mathcal{W}$ 表示小波变换，$\mathcal{W}^{-1}$ 表示小波逆变换。对高频分量 $H$ 应用非局部均值方法进行降噪, 得到降噪后的高频分量 $H_{denoised}$, 公式如下：
$$
H_{denoised}(i,j) = \frac{\sum_{k,l}w(i,j,k,l)H(k,l)}{\sum_{k,l}w(i,j,k,l)}
$$
其中，权重 $w(i,j,k,l)$ 根据像素块的相似度计算.
将低频分量 $L$ 与降噪后的高频分量 $H_{denoised}$ 进行小波逆变换, 得到增强后的图像 $C_{enhanced}$
$$C_{enhanced}=\mathcal{W}^{-1}(L,H_{denoised})$$

步骤 202, 将步骤 101 得到的增强后图像 $C_{enhanced}$ ​ 转换到标准相机空间，以消除由于不同相机模型带来的度量模糊性。标准相机变换可以表示为：
$$
C_{canonical} = \tau_{c}(C_{enhanced})
$$
其中, $\tau_{c}$ 表示标准相机空间变换操作, $C_{canonical}$ 表示标准相机模型图像.

步骤 203, 在标准相机空间中, 对步骤 202 得到的标准相机模型图像 $C_{canonical}$ 进行深度估计, 得到标准化深度图 $D_c$. 公式如下：
$$
D_c = \text{DepthEstimation}(C_{canonical})
$$
其中, $\text{DepthEstimation}$ 表示深度估计模型, $D_C$ 表示内容图像 $F_c$ 的深度信息.

进一步进行归一化操作, 以减小误差. 公式如下：
$$
D_N = \text{Normalize}(D_c) = \frac{D_{i,j}-D_{\min}}{D_{\max}-D_{\min}}
$$
其中, $\text{Normalize}$ 表示归一化操作, $D_\min$ 与 $D_\max$ 分别表示深度信息 $D_c$ 中的最大值与最小值.

步骤 205, 基于步骤 204 中归一化后的深度信息 $D_N$, 结合用户输入, 将原内容图像 $C_{enhanced}$ 划分成兴趣区域与非兴趣区域 , 创建掩膜 $M$ 与对应的 $\alpha$ 通道掩膜 $M^\alpha$, 公式如下：

以 $n$ 表示内容图像划分区域的个数, $M_{i}$ 表示兴趣区域掩膜：
$$
\begin{equation}
\begin{aligned}
M_i(x,y) = \begin{cases}1, &\text{if}\quad\frac{i-1}{n}\le D_{N}(x,y)<\frac{i}{n}\\
0, &\text{otherwise}\end{cases}
\end{aligned}
\end{equation}
$$

$M_i^\alpha$ 表示对应兴趣区域掩膜的 $\alpha$ 通道掩膜：
$$
\begin{equation}
\begin{aligned}
M_i^\alpha(x,y) = \begin{cases}1, &\text{if}\quad\frac{i-1}{n}\le D_{N}(x,y)<\frac{i}{n}\\
0, &\text{otherwise}\end{cases}
\end{aligned}
\end{equation}
$$
 
 $M_{o}$ 表示非兴趣区域掩膜：
$$
\begin{equation}
\begin{aligned}
M_o(x,y) = \begin{cases}0, &\text{if}\quad\frac{i-1}{n}\le D_{N}(x,y)<\frac{i}{n}\\
1, &\text{otherwise}\end{cases}
\end{aligned}
\end{equation}
$$
$M_o^\alpha$ 表示对应非兴趣区域掩膜的 $\alpha$ 通道掩膜：
$$
\begin{equation}
\begin{aligned}
M_o^\alpha(x,y) = \begin{cases}0, &\text{if}\quad\frac{i-1}{n}\le D_{N}(x,y)<\frac{i}{n}\\
1, &\text{otherwise}\end{cases}
\end{aligned}
\end{equation}
$$

步骤 206, 将基于步骤 205 中得到的四种掩膜应用于增强后的内容图像上, 得到内容兴趣图像 $R_{ce\_i}$ 与内容非兴趣图像 $R_{ce\_o}$, 公式如下.
$$
\begin{equation}
\begin{aligned}
R_{ce\_i}&=[C_{enhanced} \odot M_i, M_i^\alpha],\quad i\in\{1,2,3,\cdots,n\}\\
R_{ce\_o}&=[C_{enhanced} \odot M_o, M_o^\alpha],\quad o \in\{1,2,3,\cdots,n\} ,o\neq i
\end{aligned}
\end{equation}
$$
其中, $\odot$ 表示逐元素相乘, $[,]$ 表示拼接操作.

#### 步骤 3

步骤 3 对于风格主体对象, 基于其纹理特征明显的特点, 以傅里叶变换与深度卷积特征通道的风格分离属性为基础, 提取风格主体对象的风格特征, 并设计不透明度敏感的损失函数, 对主体对象的迁移结果进行训练, 以得到风格化主体对象迁移结果.

步骤 301, 对步骤 1 中获得的风格主体对象 $S_m$ 与步骤 2 中获得的内容兴趣图像 $R_{ce\_i}$ 进行八度卷积, 将其分解为高频与低频分量, 公式如下：
$$
   \begin{equation}
   \begin{aligned}
   &R_{ce\_i}^{H}, R_{ce\_i}^{L} = \text{OctConv}(R_{ce\_i}), \quad S_m^{H}, S_m^{L} = \text{OctConv}(S_m)
   \end{aligned}
   \end{equation}
$$
   其中，$R_{ce\_i}^{H}$ 和 $R_{ce\_i}^{L}$ 分别表示内容兴趣图像的高频和低频分量，$S_m^{H}$ 和 $S_m^{L}$ 分别表示风格主体对象的高频和低频分量。

步骤 302, 使用风格特征提取器 $E_{s}$ 提取步骤 301 中得到的风格主体对象的风格特征, 并通过核预测网络预测相应的卷积核与偏置, 公式如下：

$$
\begin{equation}
\begin{aligned}
k_{n,H}, b_{n,H} &= K_{n,H}(E_{s}(S_m^h,S_m^L))\\
k_{n,l}, b_{n,L} &= K_{n,L}(E_{s}(S_m^h,S_m^L))
\end{aligned}
\end{equation}
$$
其中, $K_{n,H}$ 与 $K_{n,L}$ 为卷积与偏置预测网络, $k_{n,H}, b_{n,H}$ 表示从高频风格主体对象中预测获得的卷积核与偏置, $k_{n,L}, b_{n,L}$ 表示从低频风格主体对象中预测获得的卷积核与偏置.

步骤 303, 内容兴趣图像的高频和低频分量与步骤 302 中预测的卷积核和偏置结合，在生成器$G$中进行风格迁移得到风格化主体对象 $O_m$, 公式如下：
$$
O_m = G\left(R_{ce\_i}^{H}, R_{ce\_i}^{L},\left\{k_{n,H}, b_{n,H}\right\},\left\{k_{n,L}, b_{n,L}\right\}\right)
$$

步骤 304, 基于步骤 303 得到的风格化主体对象, 计算损失函数 $\mathcal{L}$ 并进行反向传播更新卷积与偏置预测网络 $K_{n,H},K_{n,L}$ 和风格迁移生成器 $G$, 公式如下：

$$
\begin{equation}
\begin{aligned}
\mathcal{L}=\lambda_{\text{content}}\mathcal{L}_{\text{content}}+\lambda_{\text{style}}\mathcal{L}_{\text{style}}+\lambda_{\text{alpha}}\mathcal{L}_{\text{alpha}}
\end{aligned}
\end{equation}
$$
其中, $\mathcal{L}_{\text{content}},\mathcal{L}_{\text{style}},\mathcal{L}_{\text{alpha}}$ 分别表示内容损失函数, 风格损失函数, 不透明度损失函数.  $\lambda_{\text{content}},\lambda_{\text{style}},\lambda_{\text{alpha}}$ 是超参数, 用于分别表示三个损失函数在总损失函数中的含量. 
  
  内容损失 $\mathcal{L}_{\text{content}}$ 用于确保风格化后的图像保持与原始内容图像相似的结构和细节, 其公式如下：
   $$
\begin{equation}
\mathcal{L}_{\text{content}} = \| \phi(O_m) - \phi(C) \|_2^2
\end{equation}
   $$

   其中，$\phi$ 表示预训练的 VGG 特征提取网络。
   
   风格损失 $\mathcal{L}_{\text{style}}$ 用于确保风格化后的图像能够捕捉并重现风格图像的纹理和风格特征, 其公式如下： 

   $$
   \begin{equation}
   \mathcal{L}_{\text{style}} = \sum_{l} \| \mathcal{G}(\phi_l(O_m)) - \mathcal{G}(\phi_l(S_m)) \|_2^2
   \end{equation}
   $$

   其中，$\mathcal{G}$ 表示Gram矩阵，$\phi_l$ 表示第 $l$ 层特征图。

不透明度损失 $\mathcal{L}_{\text{alpha}}$ 用于确保风格迁移网络对图像中不透明度信息的敏感性, 同时使用正负样本提升风格迁移的美学效果, 其公式如下：

$$
\begin{equation}
\begin{aligned}
\mathcal{L}_{\text{alpha}}&=\sum\limits_{l=1}\mathcal{L}_{\text{alpha},l,\text{High}}+\sum\limits_{l=1}\mathcal{L}_{\text{alpha},l,\text{Low}}\\
\mathcal{L}_{\text{alpha},l}&=\sum\limits_{j=1}^N \frac{\Vert F_l(O_j*O_{j\alpha})-\text{EFDM}(F_l(O_j*O_{j\alpha}),F_l(S_{\text{pos},j}*S_{\text{pos},j,\alpha})) \Vert}{\Vert F_l(O_j*O_{j\alpha})-\text{EFDM}(F_l(O_j*O_{j\alpha}),F_l(S_{\text{neg},j}*S_{\text{neg},j,\alpha}))  \Vert}
\end{aligned}
\end{equation}
$$ 
其中, $\mathcal{L}_{\text{alpha},l,\text{High}}$ 表示利用生成器 $G$ 的第 $l$ 层输出特征图的高频部分, $\mathcal{L}_{\text{alpha},l,\text{Low}}$ 表示利用生成器 $G$ 的第 $l$ 层输出特征图的低频部分, $O_j$ 表示生成器生成的第 $j$ 张风格化主体对象, $O_{j\alpha}$ 表示 $O_j$ 的 $\alpha$ 通道, $S_{\text{pos},j}$ 表示第 $j$ 个正样本, $S_{\text{neg},j}$ 表示第 $j$ 个负样本.

#### 步骤 4

步骤 4对与风格背景对象, 基于其颜色单一的特点, 结合内容背景对象包含较多复杂对象的特点, 以背景散焦与自适应实例归一化为基础, 调整内容背景对象的清晰度与风格信息, 以得到风格化背景对象迁移结果.

步骤 401, 使用高斯模糊对内容背景对象应用散焦处理，使其与风格背景对象的单一颜色特点更加匹配, 公式如下：
$$
\begin{equation}
R_{b} = \text{GaussianBlur}(R_{ce\_o}, \sigma)
\end{equation}
$$

其中，$R_b$ 是模糊后的内容背景对象，$R_{ce\_o}$ 是原始内容背景对象，$\sigma$ 是高斯模糊的标准差，控制模糊程度。

步骤 402, 预训练的神经网络 VGG 19 对步骤 401 中模糊后的内容背景对象进行提取风格背景对象特征提取，这些特征用于指导内容背景对象的风格迁移, 公式如下：

$$
\begin{equation}
S_{bg} = \phi(S_b)
\end{equation}
$$
  其中，$S_{bg}$ 是从风格背景对象 $S_b$ 中提取的特征，$\phi$ 表示预训练的特征提取网络 VGG19。

步骤 403, 结合内容背景对象与风格背景对象的特征，使用自适应实例归一化 (AdaIN)调整步骤 402 中获得的内容背景对象的风格。

$$
\begin{equation}
O_o=\text{AdaIN}(R_b, S_{bg}) = \sigma(S_{bg}) \left( \frac{R_b - \mu(R_b)}{\sigma(R_b)} \right) + \mu(S_{bg})
\end{equation}
$$
  
   其中，$\mu$ 和 $\sigma$ 分别表示均值和标准差计算， $S_{bg}$ 表示风格背景对象的特征, $O_o$ 表示风格化背景对象。

#### 步骤 5

步骤 5, 获取风格化主体对象与风格化背景对象后, 进行最终合并操作.

步骤 501, 将风格化主体对象与风格化背景对象进行最终的合并操作, 公式如下：
$$
\begin{equation}
\begin{aligned}
O_{\text{final}}=M\cdot O_m + (I-M)O_o
\end{aligned}
\end{equation}
$$
其中, $M$ 表示主体对象的掩膜, $I$ 表示单位矩阵, $O_{\text{final}}$ 表示最终的风格迁移结果.

### 第三部分：专利优势

1. 本发明在面对内容主体纷乱的内容图像时, 通过深度估计机制, 引导风格迁移模块对特定区域实现风格迁移, 有效解决了复杂场景风格迁移结果杂乱的问题.
2. 在风格主体对象迁移网络的训练中, 重新设计了将图像 alpha 通道信息纳入考量的风格训练损失函数, 这样既可以引导模型迅速收敛, 又可使模型考虑图像中的不透明度信息, 有效解决了风格迁移领域难以迁移 png 格式图像的问题. 在网络的训练中, 也会利用正负样本的差别对网络进行训练, 实现了更有效果的风格迁移.
3. 在内容图像分解方面, 利用了相同主体基本处于相同深度的特点, 对内容图像相关矩阵进行分解, 进而提取出主体对象区域与背景对象区域，这样做可以更好的区分主体与背景的边界. 

### 第四部分：配图

