“雕像本来就在石头里, 我只是把不需要的东西去掉罢了”--米开朗基罗

Diffusion也是如此, 噪声图像中本来就有图像, 只是把噪声“去除”罢了

# Denoise模块

## 什么是Denoise模块

一个将噪声图像转变为有意义的、言之有物的图像

## Denoise模块的输入

有三个, 一个是噪声图像, 另一个是需要迭代的次数, 最后一个是对于图像的文字描述

## Denoise模块的组成

### Noise Predicter

用于预测噪声图像中有什么图像. 

从实现角度来说
1. Denoise模块接收「迭代轮次」与「噪声图像」作为输入
2. Denoise模块产生「输入图像」的「噪声杂讯」
3. 将「噪声杂讯」扣掉「输入图像」以达成Denoise的效果

### 训练Noise Predicter

1. 创造训练数据：加噪声
	1. Forward Process(Diffusion Process)对一张图像加噪声, 并重复这步骤, 直到地道一张噪声图像 
		1. ![[Pasted image 20231103104634.png]]
	2. 以此为数据集, 即可告诉Noise Predicter有关「迭代轮次」、「当前轮次的结果」、「描述性文字」之间的对应关系,
		1. 以训练1000次为例, 第1次加噪声的结果, 应该是网络第999次Denoise时的输出图像
		2. ![[Pasted image 20231103110816.png]]
		3. 


接下来我们继续推导 DDPM 中的最大化下界：

根据前面的推导，我们得到了如下的不等式：

$$
\log P_\theta(x_0) \ge \mathbb{E}_{q(x_{1:T}|x_0)}\left[\log\frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)}\right]
$$

这个不等式的右边部分即为证据下界（Evidence Lower Bound, ELBO），记作 $\mathcal{L}(\theta)$，我们需要最大化这个下界：

$$
\mathcal{L}(\theta) = \mathbb{E}_{q(x_{1:T}|x_0)}\left[\log\frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)}\right]
$$

进一步，我们可以将 $\mathcal{L}(\theta)$ 分解为以下几项：

$$
\mathcal{L}(\theta) = \mathbb{E}_{q(x_{1:T}|x_0)}\left[\log p_\theta(x_{0:T}) - \log q(x_{1:T}|x_0)\right]
$$

我们分别对这两项进行处理。

### 1. 处理 $\log p_\theta(x_{0:T})$

根据马尔可夫性质，我们可以将 $p_\theta(x_{0:T})$ 分解为：

$$
p_\theta(x_{0:T}) = p(x_T) \prod_{t=1}^T p_\theta(x_{t-1}|x_t)
$$

因此有：

$$
\log p_\theta(x_{0:T}) = \log p(x_T) + \sum_{t=1}^T \log p_\theta(x_{t-1}|x_t)
$$

### 2. 处理 $\log q(x_{1:T}|x_0)$

根据定义，$q(x_{1:T}|x_0)$ 可以表示为：

$$
q(x_{1:T}|x_0) = q(x_T|x_0) \prod_{t=1}^{T-1} q(x_t|x_{t+1}, x_0)
$$

因此有：

$$
\log q(x_{1:T}|x_0) = \log q(x_T|x_0) + \sum_{t=1}^{T-1} \log q(x_t|x_{t+1}, x_0)
$$

将这些结果代入 $\mathcal{L}(\theta)$，我们得到：

$$
\begin{aligned}
\mathcal{L}(\theta) &= \mathbb{E}_{q(x_{1:T}|x_0)}\left[\log p(x_T) + \sum_{t=1}^T \log p_\theta(x_{t-1}|x_t) - \log q(x_T|x_0) - \sum_{t=1}^{T-1} \log q(x_t|x_{t+1}, x_0)\right] \\
&= \mathbb{E}_{q(x_{1:T}|x_0)}\left[\log p(x_T) - \log q(x_T|x_0) + \sum_{t=1}^T \log p_\theta(x_{t-1}|x_t) - \sum_{t=1}^{T-1} \log q(x_t|x_{t+1}, x_0)\right]
\end{aligned}
$$

### 3. 化简得到最终的 ELBO

为了简化分析，我们引入 KL 散度：

$$
\text{KL}(q(x_T|x_0) \| p(x_T)) = \mathbb{E}_{q(x_T|x_0)}\left[\log q(x_T|x_0) - \log p(x_T)\right]
$$

同样地，对于每个 $t$，我们有：

$$
\text{KL}(q(x_t|x_{t+1}, x_0) \| p_\theta(x_{t-1}|x_t)) = \mathbb{E}_{q(x_t|x_{t+1}, x_0)}\left[\log q(x_t|x_{t+1}, x_0) - \log p_\theta(x_{t-1}|x_t)\right]
$$

将上述 KL 散度表达式代入 $\mathcal{L}(\theta)$，我们得到：

$$
\begin{aligned}
\mathcal{L}(\theta) &= -\text{KL}(q(x_T|x_0) \| p(x_T)) - \sum_{t=1}^T \mathbb{E}_{q(x_{t+1:T}|x_0)}\left[\text{KL}(q(x_t|x_{t+1}, x_0) \| p_\theta(x_{t-1}|x_t))\right] \\
&= -\text{KL}(q(x_T|x_0) \| p(x_T)) - \sum_{t=1}^{T-1} \mathbb{E}_{q(x_{t+1:T}|x_0)}\left[\text{KL}(q(x_t|x_{t+1}, x_0) \| p_\theta(x_{t-1}|x_t))\right]
\end{aligned}
$$

这就是 DDPM 中 ELBO 的形式，我们通过最大化该下界来训练模型参数 $\theta$。