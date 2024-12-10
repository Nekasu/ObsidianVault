
>[!warning] 提示
>点击右上角「书本」![[Pasted image 20231125105318.png]]图标, 进入阅读模式, 以
>获得更好的阅读体验！

https://yinglinzheng.netlify.app/diffusion-model-tutorial/

## 扩散模型的前提

1. 扩散模型遵循这样一个前提：所有图像都满足某种特定的概率分布
	1. 高斯噪声服从高斯分布, 且高斯噪声是从高斯分布中采样得到的图像
	2. 复杂图像服从复杂分布, 且复杂图像是从某个复杂分布中采样得到的图像
3. 如何将复杂分布变成高斯分布, 就是扩散过程需要完成的任务.
	1. 实际上, 这一步很简单
	2. 在实际中i, 我们往往是有一张特定的图像, 只需要往里面加高斯噪声就可以达成这个目标
	3. 这是因为这个特定的图像可以看作是一个定值, 所以可以看作是高斯噪声的均值
4. 如何将高斯分布变换成其他复杂分布, 就是逆扩散过程需要完成的任务
	1. 

## 前向过程与扩散

### 前向过程的描述



### 前向过程的参数化表示

#### 参数设定

1. 原始图像：$x_0$
2. 第 $t$ 次的从标准高斯分布中采样噪声图像 $z_t$ 
3. 第 $t$ 次将噪声 $z_t$ 加入 $x_0$ 后的图像 $x_t$
4. 第 $t$ 次加噪声时, 噪声图像 $z_t$ 与图像 $x_{t-1}$ 的比例 $1-\beta_t$ 与 $\beta_t$ 

#### 加噪过程

##### 加噪过程公式

1. 从数据集中获取一张原始的真实图像 $x_0$
2. 从标准高斯分布 $\mathcal{N}(0,1)$ 中采样一张噪声图 $z_1$
3. 将噪声图 $z_1$ 与原始图像 $x_0$ 按 $\sqrt{1-\alpha_1}$ 与 $\sqrt{\alpha_1}$ 的比例混合, 可以得到第一步的加噪声结果, 如下所示

$$
x_1 = \sqrt{1-\alpha_1}z_0 + \sqrt{\alpha_1}x_0
$$
4. 将噪声图 $z_2$ 与上一步得到的结果 $z_1$ 按 $\sqrt{1-\alpha_2}$ 与 $\sqrt{\alpha_2}$ 的比例混合, 如下所示

$$
\begin{equation}
	\begin{aligned}
		x_2 =& \sqrt{1-\alpha_2}z_1 + \sqrt{\alpha_2}x_1\\
	\end{aligned}
\end{equation}
$$

5. 则第 $t$ 张加噪图像 $x_t$ 满足以下公式：

$$
x_t = \sqrt{\alpha_t}x_{t-1}+\sqrt{1-\alpha_t}z_t
$$
##### 加噪过程公式简化

###### 整体简化

我们对第 $t$ 张加噪图像 $x_t$ 满足的公式 $x_t = \sqrt{\alpha_t}x_{t-1}+\sqrt{1-\alpha_t}z_t$ 进行如下变换：

$$
\begin{equation}
\begin{aligned}

x_t &= \sqrt{\alpha_t}x_{t-1}+\sqrt{1-\alpha_t}z_t\\
\\
&= \sqrt{\alpha_t}\left(\sqrt{\alpha_{t-1}}x_{t-2}+\sqrt{1-\alpha_{t-1}}z_{t-1}\right)+\sqrt{1-\alpha_t}z_t\\
&= \sqrt{\alpha_t\alpha_{t-1}}x_{t-2}+\sqrt{\alpha_t(1-\alpha_{t-1})}z_{t-1}+\sqrt{1-\alpha_t}z_t\\
\\
&= \sqrt{\alpha_t\alpha_{t-1}}\left(\sqrt{\alpha_{t-2}}x_{t-3}+\sqrt{1-\alpha_{t-2}}z_{t-2}\right)+\sqrt{\alpha_t(1-\alpha_{t-1})}z_{t-1}+\sqrt{1-\alpha_t}z_t\\
&= \sqrt{\alpha_t\alpha_{t-1}\alpha_{t-2}}x_{t-3}+\sqrt{\alpha_t\alpha_{t-1}(1-\alpha_{t-2})}z_{t-2}+\sqrt{\alpha_t(1-\alpha_{t-1})}z_{t-1}+\sqrt{1-\alpha_t}z_t\\
\\
&=\cdots\\
&=\sqrt{\alpha_t\alpha_{t-1}\alpha_{t-2}\cdots\alpha_1}x_0+\sqrt{\alpha_t\alpha_{t-1}\cdots\alpha_2(1-\alpha_1)}z_1 \\
&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad+\sqrt{\alpha_t\alpha_{t-1}\cdots\alpha_3(1-\alpha_2)}z_2\\
&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad+ \sqrt{\alpha_t\alpha_{t-1}\cdots\alpha_4(1-\alpha_3)}z_3\\
&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad+ \sqrt{\alpha_t\alpha_{t-1}\cdots\alpha_5(1-\alpha_4)}z_4\\
&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad+ \sqrt{\alpha_t\alpha_{t-1}\cdots\alpha_6(1-\alpha_5)}z_5\\
&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad+ \sqrt{\alpha_t\alpha_{t-1}\cdots\alpha_7(1-\alpha_6)}z_6\\
&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\vdots\\
&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad+ \sqrt{\alpha_t(1-\alpha_{t-1})}z_{t-1}\\
&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad+ \sqrt{1-\alpha_t}z_{t}\\
\\
&= \sqrt{\alpha_t\alpha_{t-1}\alpha_{t-2}\cdots\alpha_1}x_0+ \sum_{i=1}^t\sqrt{\alpha_t\alpha_{t-1}\cdots\alpha_{i+1}(1-\alpha_i)}z_i
\end{aligned}
\end{equation}

$$

通过上述公式, 我们便可以计算经过 $t$ 次加噪后获得的图像 $x_t$. 整个公式可以看作是两个部分, 其一为包含原图的「原图项」 $\sqrt{\alpha_t\alpha_{t-1}\alpha_{t-2}\cdots\alpha_1}x_0$, 其二为包含 $t$ 个噪声的「叠加噪声项」 $\sum_{i=1}^t\sqrt{\alpha_t\alpha_{t-1}\cdots\alpha_{i+1}(1-\alpha_i)}z_i$

###### 原图项的简化

实际上, 「原图项」是一个计算较为简单的项, 而后面的「叠加噪声项」是一个计算复杂的项. 现在我们探索如何简化「叠加噪声项」.

为了化简方便, 我们定义「原图项」 $\sqrt{\alpha_t\alpha_{t-1}\alpha_{t-2}\cdots\alpha_1}x_0$ 的系数 $\sqrt{\alpha_t\alpha_{t-1}\alpha_{t-2}\cdots\alpha_1}$为 $\overline{\alpha_t}$,  有

$$
\overline{\alpha_t} = \prod\limits_{i=1}^t\alpha_i=\sqrt{\alpha_t\alpha_{t-1}\alpha_{t-2}\cdots\alpha_1}
$$

如 $\overline{\alpha_2}=\alpha_2\cdot\alpha_1$, $\overline{\alpha_4}=\alpha_4\cdot\alpha_3\cdot\alpha_2\cdot\alpha_1$

在此定义下, 将 $\overline{\alpha_t} = \prod\limits_{i=1}^t\alpha_i$ 代入 $x_t$ 中的「原图项」, 有

$$
\begin{equation}
\begin{aligned}

x_t &= \sqrt{\alpha_t\alpha_{t-1}\alpha_{t-2}\cdots\alpha_1}x_0+ \sum_{i=1}^t\sqrt{\alpha_t\alpha_{t-1}\cdots\alpha_{i+1}(1-\alpha_i)}z_i\\
&= \sqrt{\overline{\alpha_t}}x_0 + \sum_{i=1}^t\sqrt{\alpha_t\alpha_{t-1}\cdots\alpha_{i+1}(1-\alpha_i)}z_i\\

\end{aligned}
\end{equation}
$$

###### 叠加噪声项的简化

 因为我们希望整个「叠加噪声项」是一个简单的噪声, 所以我们希望最终 $x_t$ 满足的表达式也具有 $x_t=\sqrt{\overline{\alpha_t}}a+\sqrt{1-\overline{\alpha_t}}b$ 的形式, 即系数的平方和为 $1$.
 
  注意到「原图项」的系数现在为 $\sqrt{\overline{\alpha_t}}$, 我们期望后面的「叠加噪声项」的系数为 $\sqrt{1-\overline{\alpha_i}}$, 所以对「叠加噪声项」提取系数 $\sqrt{1-\overline{\alpha_t}}$, 从而有以下变化

$$\begin{equation}
\begin{aligned}

x_t &= \sqrt{\overline{\alpha_t}}x_0 + \sum_{i=1}^t\sqrt{\alpha_t\alpha_{t-1}\cdots\alpha_{i+1}(1-\alpha_i)}z_i\\
&= \sqrt{\overline{\alpha_t}}x_0 +　\sqrt{1-\overline{\alpha_t}}\sum_{i=1}^t\frac{\sqrt{\alpha_t\alpha_{t-1}\cdots\alpha_{i+1}(1-\alpha_i)}}{\sqrt{1-\overline{\alpha_t}}}z_i

\end{aligned}
\end{equation}$$
- - -

现在考察「叠加噪声项」中的 $\sum_{i=1}^t\frac{\sqrt{\alpha_t\alpha_{t-1}\cdots\alpha_{i+1}(1-\alpha_i)}}{\sqrt{1-\overline{\alpha_t}}}z_i$ 部分 (即上面公式中最后一个分式)分以期望他是一个简单的分布.

这个分式部分中的单个噪声项 $z_i$ 均是从标准高斯分布中采样得到的, 即 $z_i∼\mathcal{N}(0,1)$ (即均值为0，方差为1), 且上一次采样的噪声不会影响下一次噪声的采样, 所以 $z_i$ 的获取是相互独立的.

同时, 我们知道, 如果 $X\sim \mathcal{N}(\mu_x,\sigma_x^2)$, $Y\sim \mathcal{N}(\mu_y,\sigma_y^2)$, 且 $X$ 与 $Y$ 相互独立, 则有 $aX+bY\sim\mathcal{N}(a\mu_x+b\mu_y,a^2\sigma_x^2+b^2\sigma_y^2)$ 

在这样的情况下, 则有「叠加噪声项」中的 $\sum_{i=1}^t\frac{\sqrt{\alpha_t\alpha_{t-1}\cdots\alpha_{i+1}(1-\alpha_i)}}{\sqrt{1-\overline{\alpha_t}}}z_i$ 部分服从以下高斯分布：

$$\sum_{i=1}^t\frac{\sqrt{\alpha_t\alpha_{t-1}\cdots\alpha_{i+1}(1-\alpha_i)}}{\sqrt{1-\overline{\alpha_t}}}z_i\sim \mathcal{N}\left[\sum_{i=1}^t\left(\frac{\sqrt{\alpha_t\alpha_{t-1}\cdots\alpha_{i+1}(1-\alpha_i)}}{\sqrt{1-\overline{\alpha_t}}}\cdot0\right), \sum_{i=1}^t\left(\frac{\alpha_t\alpha_{t-1}\cdots\alpha_{i+1}(1-\alpha_i)}{1-\overline{\alpha_t}}\cdot 1\right)\right]$$

可以发现, 这个高斯分布的均值部分为 $0$, 因为均值部分中累加的每一项都与 $0$ 相乘了. 从而上述高斯分布可以化简为：

$$
\sum_{i=1}^t\frac{\sqrt{\alpha_t\alpha_{t-1}\cdots\alpha_{i+1}(1-\alpha_i)}}{\sqrt{1-\overline{\alpha_t}}}z_i\sim \mathcal{N}\left(0, \sum_{i=1}^t\frac{\alpha_t\alpha_{t-1}\cdots\alpha_{i+1}(1-\alpha_i)}{1-\overline{\alpha_t}} \right)
$$

为了搞清楚这个「叠加噪声项」到底满足什么样的高斯分布, 我们继续考察这个高斯分布的方差部分, 记为 $\sigma^2_s=\sum_{i=1}^t\frac{\alpha_t\alpha_{t-1}\cdots\alpha_{i+1}(1-\alpha_i)}{1-\overline{\alpha_t}}$ , 下标 $s$ 为 sum 的缩写, 表示累加

直接将 $\sigma^2_S$ 拆开, 有

$$
\begin{equation}
\begin{aligned}

\sigma^2_s &=\sum_{i=1}^t\frac{\alpha_t\alpha_{t-1}\cdots\alpha_{i+1}(1-\alpha_i)}{1-\overline{\alpha_t}}\\

&=\frac{1}{1-\overline{\alpha_t}}\left[\sum_{i=1}^t\alpha_t\alpha_{t-1}\cdots\alpha_{i+1}(1-\alpha_i)\right]\\

&\xlongequal{去除累加符号} \frac{1}{1-\overline{\alpha_t}}\left[(1-\alpha_t)+\alpha_t(1-\alpha_{t-1})+\alpha_t\alpha_{t-1}(1-\alpha_{t-2})+\cdots+\alpha_t\alpha_{t-1}\cdots\alpha_2(1-\alpha_1)\right]\\

&\xlongequal{拆除小括号}  \frac{1}{1-\overline{\alpha_t}}\left[1-\alpha_t+\alpha_t-\alpha_t\alpha_{t-1}+\alpha_t\alpha_{t-1}-\alpha_t\alpha_{t-1}\alpha_{t-2}+\cdots+\alpha_t\alpha_{t-1}\cdots\alpha_2-\alpha_t\alpha_{t-1}\cdots\alpha_2\alpha_1\right]\\

&\xlongequal{发现中括号中除了第一项和最后一项都可以消去} \frac{1}{1-\overline{\alpha_t}}\left[1-\alpha_t\alpha_{t-1}\cdots\alpha_2\alpha_1\right]\\

&=\frac{1}{1-\overline{\alpha_t}}(1-\overline{a_t})\\

&\xlongequal{分子分母相同}1

\end{aligned}
\end{equation}

$$

也即 $\sigma^2_s=1$, 从而有 $\sum_{i=1}^t\frac{\sqrt{\alpha_t\alpha_{t-1}\cdots\alpha_{i+1}(1-\alpha_i)}}{\sqrt{1-\overline{\alpha_t}}}z_i\sim\mathcal{N}(0,1)$, 我们记 $\sum_{i=1}^t\frac{\sqrt{\alpha_t\alpha_{t-1}\cdots\alpha_{i+1}(1-\alpha_i)}}{\sqrt{1-\overline{\alpha_t}}}z_i=\widetilde{z}$  , 从而有 $\widetilde{z}\sim\mathcal{N}(0,1)$ 

至此, 我们可以发现, 「叠加噪声项」也是一个服从标准高斯分布的噪声, 从而我们可以得到第 $t$ 步图像 $x_t$ 与原图 $x_0$ 之间的关系：

$$
\begin{equation}
\begin{aligned}

x_t &= \sqrt{\overline{\alpha_t}}x_0 + \sum_{i=1}^t\sqrt{\alpha_t\alpha_{t-1}\cdots\alpha_{i+1}(1-\alpha_i)}z_i\\
&= \sqrt{\overline{\alpha_t}}x_0 + \sqrt{1-\overline{a_t}}\widetilde{z},\quad \text{其中}\widetilde{z}\sim\mathcal{N}(0,1)

\end{aligned}
\end{equation}
$$

##### 加噪过程总结

在公式 $x_t= \sqrt{\overline{\alpha_t}}x_0 + \sqrt{1-\overline{a_t}}\widetilde{z},\quad \text{其中}\widetilde{z}\sim\mathcal{N}(0,1)$ 的指导下, 可以立刻得到某个特定步骤 $t$ 的加噪图像 $x_t$, 且加噪图像仅与原始图像 $x_0$ 与当前步骤数 $t$ 有关.

经过这样的简化, 就可以简单的获取加噪后的图像, 也即训练数据了.

#### 概率采样视角看加噪过程

在上面的[[扩散模型过程整理#加噪过程]]中, 我们推导出了直接从原图 $x_0$ 获取第 $t$ 次后的加噪图像 $x_t$ 的公式如下：

$$x_t= \sqrt{\overline{\alpha_t}}x_0 + \sqrt{1-\overline{a_t}}\widetilde{z},\quad \text{其中}\widetilde{z}\sim\mathcal{N}(0,1)$$

实际上, 我们也可以将 $x_t$ 看作是某种概率的采样结果, 推导如下：

已知 $\widetilde{z}\sim\mathcal{N}(0,1)$, 则有 $\sqrt{1-\overline{a_t}}\widetilde{z}\sim\mathcal{N}(0,1-\overline{\alpha_t})$

从而有 $\sqrt{\overline{\alpha_t}}x_0 + \sqrt{1-\overline{a_t}}\widetilde{z}\sim\mathcal{N}(\sqrt{\overline{\alpha_t}}x_0,1-\overline{\alpha_t})$  , 

从而有 $q(x_t\vert x_0)\sim \mathcal{N}(\sqrt{\overline{\alpha_t}}x_0,1-\overline{\alpha_t})$

这个结果表明，第 $t$ 步的加噪图像 $x_t$ ​ 可以看作是从一个正态分布中采样的结果，其均值和方差分别由初始图像 $x_0$ ​ 和累积噪声参数 $\overline{\alpha_t}$ ​决定

同理, 由于有 $x_t = \sqrt{\alpha_t}x_{t-1}+\sqrt{1-\alpha_t}z_t$ , 所以有 

$$q(x_t|x_{t-1},x_0)\sim \mathcal{N}(\sqrt{\alpha_t}x_{t-1}, 1-\alpha_t)$$


## 逆向过程与降噪

### 逆向过程的描述

从后一个推前一个

### 逆向过程的符号表示

很显然, 我们想要通过 $x_t$ 来预测 $x_{t-1}$. 

如果我们能够逆转上述扩散扩散过程, 并从 $𝑞(x_{𝑡−1}|𝑥_𝑡)$ 采样，就可以从高斯噪声 $𝑥_t∼𝑁(0,1)$ 还原出原图服从的分布 $𝑥_0∼𝑞(𝑥)$。

如何获得 $q(x_{t-1}\vert x_t)$ 这个概率密度就是一个需要探讨的问题. 直接计算比较困难, 所以我们可以考虑对公式进行变形. 对公式使用贝叶斯公式, 有如下结果

$$

\begin{equation}
\begin{aligned}
q(x_{t-1}|x_t) &\xlongequal{贝叶斯公式} \frac{q(x_{t-1},x_t)}{q(x_t)}\\
&\xlongequal{分母用全概率公式展开} \frac{q(x_t|x_{t-1})\cdot q(x_{t-1})}{q(x_t)}\\
&=q(x_t|x_{t-1}) \cdot \frac{q(x_{t-1})}{q(x_t)}\\
\end{aligned}
\end{equation}

$$

通过这样的变换, 我们将一个无法计算的式子 $q (x_{t-1}|x_t)$, 改写成了一个可计算的部分 $q(x_t|x_{t-1})$ 和一个不可计算的分式 $\frac{q(x_{t-1})}{q(x_t)}$ 的乘积

自己观察这个不可计算的分式, 可以发现, 这个分式的分子与分母都是不可计算的. 因为如果我们能直接得到 $q(x_{t})$ 或 $q(x_{x-1})$, 那我们就能直接得出 $q(x_0)$. 但是我们计算 $q (x_{t-1}|x_t)$ 的目的就是为了计算 $q(x_0)$, 如果可以直接得出 $q(x_0)$, 那么我们就没有计算 $q (x_{t-1}|x_t)$ , 所以我们不可能直接得到 $q(x_t)$.

可以想到, 虽然直接计算 $q(x_t)$ 是不可行的, 但是计算 $q(x_t|x_0)$ 是十分简单的, 在[[扩散模型过程整理#概率采样视角看加噪过程]] 中我们介绍过这个计算：

$$
q(x_t\vert x_0)\sim \mathcal{N}(\sqrt{\overline{\alpha_t}}x_0,1-\overline{\alpha_t})
$$

所以我们可以考虑将 $q(x_t)$ 的计算转换成 $q(x_t|x_0)$ 用于计算, 由此可以计算 $q(x_{t-1}|x_t,x_0)$, 有


$$

\begin{equation}
\begin{aligned}
q(x_{t-1}|x_t,x_0) &\xlongequal{贝叶斯公式} \frac{q(x_{t-1},x_t,x_0)}{q(x_t,x_0}\\
&\xlongequal{分母用全概率公式展开} \frac{q(x_t|x_{t-1},x_0)\cdot q(x_{t-1},x_0)}{q(x_t,x_0)}\\
&=q(x_t|x_{t-1}) \cdot \frac{q(x_{t-1},x_0)}{q(x_t,x_0)}\\
&=q(x_t|x_{t-1}) \cdot \frac{q(x_{t-1},x_0)}{q(x_t,x_0)}\\
=& q(x_t|x_{t-1}) \cdot \frac{q(x_{t-1}|x_0)\cdot q(x_0)}{q(x_t|x_0)\cdot q(x_0)}\\
=& q(x_t|x_{t-1}) \cdot \frac{q(x_{t-1}|x_0)}{q(x_t|x_0)}\\
\end{aligned}
\end{equation}

$$

对上述推导取等式左侧与右侧第一项, 有 $q(x_{t-1}|x_t,x_0)=q(x_t|x_{t-1}) \cdot \frac{q(x_{t-1}|x_0)}{q(x_t|x_0)}$

这三项就都是很好计算的项了, 从[[扩散模型过程整理#概率采样视角看加噪过程]] 中, 我们有推导结果

$$
\begin{equation}
\begin{aligned}
	q(x_t|x_{t-1},x_0)&\sim \mathcal{N}(\sqrt{\alpha_t}x_{t-1}, 1-\alpha_t)\\
	&=\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{1}{2}\cdot(\frac{x_t-\mu}{\sigma})^2}\\
	&= \frac{1}{\sqrt{2\pi}\cdot\sqrt{1-\alpha_t}}\exp\left[{-\frac{1}{2}\cdot\left(\frac{x_t-\sqrt{\alpha_t}x_{t-1}}{\sqrt{1-\alpha_t}}\right)^2}\right]\\
	x_t为随机变量
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
q(x_{t-1}\vert x_0)&\sim \mathcal{N}(\sqrt{\overline{\alpha_t}}x_0,1-\overline{\alpha_{t-1}})\\
&=\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{1}{2}\cdot(\frac{x_{t-1}-\mu}{\sigma})^2}\\
&= \frac{1}{\sqrt{2\pi}\cdot\sqrt{1-\overline{\alpha_{t-1}}}}\exp\left[{-\frac{1}{2}\cdot\left(\frac{x_{t-1}-\sqrt{\overline{\alpha_{t-1}}}x_0}{\sqrt{1-\overline{\alpha_{t-1}}}}\right)^2}\right]\\
x_{t-1}为随机变量
\end{aligned}
\end{equation}
$$
$$
\begin{equation}
\begin{aligned}
q(x_t\vert x_0)&\sim \mathcal{N}(\sqrt{\overline{\alpha_t}}x_0,1-\overline{\alpha_t})\\
&=\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{1}{2}\cdot(\frac{x_t-\mu}{\sigma})^2}\\
&= \frac{1}{\sqrt{2\pi}\cdot\sqrt{1-\overline{\alpha_t}}}\exp\left[{-\frac{1}{2}\cdot\left(\frac{x_t-\sqrt{\overline{\alpha_t}}x_0}{\sqrt{1-\overline{\alpha_t}}}\right)^2}\right]\\
x_t为随机变量
\end{aligned}
\end{equation}
$$

将这三个式子带入上述公式 $q(x_{t-1}|x_t,x_0)=q(x_t|x_{t-1}) \cdot \frac{q(x_{t-1}|x_0)}{q(x_t|x_0)}$, 有如下化简：

$$
\begin{equation}
\begin{aligned}
q(x_{t-1}|x_t,x_0) &= q(x_t|x_{t-1}) \cdot \frac{q(x_{t-1}|x_0)}{q(x_t|x_0)}\\
&= \frac{1}{\sqrt{2\pi}\cdot\sqrt{1-\alpha_t}}\exp\left[{-\frac{1}{2}\cdot\left(\frac{x_t-\sqrt{\alpha_t}x_{t-1}}{\sqrt{1-\alpha_t}}\right)^2}\right]\cdot\frac{\frac{1}{\sqrt{2\pi}\cdot\sqrt{1-\overline{\alpha_{t-1}}}}\exp\left[{-\frac{1}{2}\cdot\left(\frac{x_{t-1}-\sqrt{\overline{\alpha_{t-1}}}x_0}{\sqrt{1-\overline{\alpha_{t-1}}}}\right)^2}\right]}{\frac{1}{\sqrt{2\pi}\cdot\sqrt{1-\overline{\alpha_t}}}\exp\left[{-\frac{1}{2}\cdot\left(\frac{x_t-\sqrt{\overline{\alpha_t}}x_0}{\sqrt{1-\overline{\alpha_t}}}\right)^2}\right]}\\
&\xlongequal[忽略前面的系数]{指数相乘(除)等于幂相加(减)}k\cdot\exp\left\{-\frac12\cdot\left[ \left(\frac{x_t-\sqrt{\alpha_t}x_{t-1}}{\sqrt{1-\alpha_t}}\right)^2 +\left(\frac{x_{t-1}-\sqrt{\overline{\alpha_{t-1}}}x_0}{\sqrt{1-\overline{\alpha_{t-1}}}}\right)^2- \left(\frac{x_t-\sqrt{\overline{\alpha_t}}x_0}{\sqrt{1-\overline{\alpha_t}}}\right)^2 \right]\right\}\\
\end{aligned}
\end{equation}
$$

这个公式看起来很复杂, 但是我们可以这样考虑：整个公式为一个常数与一个「以 $e$ 为底的指数」的乘积, 与高斯分布的形式很像, 而我们知道, 高斯分布中的指数部分是一个完全平方：$\exp\left(-\frac12\cdot\left[\frac{(x-\mu)}{\sigma}\right]^2\right)=\exp\left\{-\frac12\left(\frac{1}{\sigma^2}x^2-\frac{2\mu}{\sigma^2}x+\frac{\mu^2}{\sigma^2}\right)\right\}$, 所以我们可以也将上面公式中的指数部分变成一个完全平方. 

经过简化, 有：

$$
\begin{equation}
\begin{aligned}
q(x_{t-1}|x_t,x_0) &= k\cdot \exp{\left\{-\frac{1}{2}\cdot\left[\left(\frac{x-\sqrt{\alpha_t}x_{t-1}}{\sqrt{1-\alpha_t}}\right)^2+\left(\frac{x-\sqrt{\overline{\alpha_{t-1}}}x_0}{\sqrt{1-\overline{\alpha_{t-1}}}}\right)^2-\left(\frac{x-\sqrt{\overline{\alpha_t}}x_0}{\sqrt{1-\overline{\alpha_t}}}\right)^2   \right]\right\}}\\
&\xlongequal{将平方拆开}k\cdot\exp \left\{ -\frac{1}{2}\left(\frac{{x}_{t}^{2}-2 \sqrt{\alpha_{t}} {x}_{t} {x}_{t-1}+\alpha_{t} {x}_{t-1}^{2}}{1-\alpha_{t}}+\frac{{x}_{t-1}^{2}-2 \sqrt{\overline{\alpha_{t-1}}} {x}_{0} {x}_{t-1}+\overline{\alpha_{t-1}} {x}_{0}^{2}}{1-\overline{\alpha_{t-1}}}-\frac{\left({x}_{t}-\sqrt{\overline{\alpha_{t}}} {x}_{0}\right)^{2}}{1-\overline{\alpha_{t}}}\right)\right\} \\
&\xlongequal{合并x_{t-1}的同类项}k\cdot\exp \left\{\underbrace{-\frac{1}{2}\left[\left(\frac{\alpha_{t}}{1-\alpha_{t}}+\frac{1}{1-\overline{\alpha_{t-1}}}\right) {x}_{t-1}^{2}-2\left(\frac{ \sqrt{\alpha_{t}}}{1-\alpha_{t}} {x}_{t}+\frac{\sqrt{\overline{\alpha_{t-1}}}}{1-\overline{\alpha_{t-1}}} {x}_{0}\right) {x}_{t-1}+C\left({x}_{t}, {x}_{0}\right)\right]}_{这部分就是高斯分布中的-\frac12\left(\frac{1}{\sigma^2}x^2-\frac{2\mu}{\sigma^2}x+\frac{\mu^2}{\sigma^2}\right)} \right\}\\
&\xlongequal{完全平方公式}k\cdot\exp\left\{-\frac{1}{2}\cdot\left[  \frac{x_{t-1}-\left(\frac{\sqrt{\alpha_t}(1-\overline{\alpha_{t-1}})}{1-\overline{\alpha_t}}x_t+\frac{\sqrt{\overline{\alpha_{t-1}}}\left(1-\alpha_t\right)}{1-\overline{\alpha_t}}x_0\right)}{\sqrt{\frac{\alpha_t}{1-\alpha_t}+\frac{1}{1-\overline{\alpha_{t-1}}}}}  \right]^2\right\}\\
&=\exp\left(-\frac12\cdot\left[\frac{(x-\mu)}{\sigma}\right]^2\right)\\
\end{aligned}
\end{equation}
$$

其中, $\mu=\frac{\sqrt{\alpha_t}(1-\overline{\alpha_{t-1}})}{1-\overline{\alpha_t}}x_t+\frac{\sqrt{\overline{\alpha_{t-1}}}\left(1-\alpha_t\right)}{1-\overline{\alpha_t}}x_0$, $\sigma=\sqrt{\frac{\alpha_t}{1-\alpha_t}+\frac{1}{1-\overline{\alpha_{t-1}}}}$

通过以上化简, 我们轻易的得到的 $q(x_{t-1}|x_t,x_0)$ 所服从的分布实际上也是一个高斯分布, 即

$$q(x_{t-1}|x_t,x_0)\sim\mathcal{N}(\mu,\sigma^2)\sim\mathcal{N}\left(\frac{\sqrt{\alpha_t}(1-\overline{\alpha_{t-1}})}{1-\overline{\alpha_t}}x_t+\frac{\sqrt{\overline{\alpha_{t-1}}}\left(1-\alpha_t\right)}{1-\overline{\alpha_t}}x_0, \frac{\alpha_t}{1-\alpha_t}+\frac{1}{1-\overline{\alpha_{t-1}}}\right)$$

观察方差 $\sigma^2=\frac{\alpha_t}{1-\alpha_t}+\frac{1}{1-\overline{\alpha_{t-1}}}$ 可以发现, 其中所有的值均为常数, 是一个可以直接计算的值

观察均值 $\mu=\frac{\sqrt{\alpha_t}(1-\overline{\alpha_{t-1}})}{1-\overline{\alpha_t}}x_t+\frac{\sqrt{\overline{\alpha_{t-1}}}\left(1-\alpha_t\right)}{1-\overline{\alpha_t}}x_0$, 可以发现所有的 $\alpha$ 均是已知值, $x_t$ 也是已知值, 而整个均值的式子中, 唯一一个不知道的值为 $x_0$. 如果能得知 $x_0$ 就能很快的进行计算了.

实际上, 我们在[[扩散模型过程整理#加噪过程总结]] 中有公式 

$$x_t=\sqrt{\overline{\alpha_t}}x_0 + \sqrt{1-\overline{a_t}}\widetilde{z},\quad \text{其中}\widetilde{z}\sim\mathcal{N}(0,1)$$

从这个式子中, 我们可以反推出 $x_0$, 即 $x_0 = \frac{1}{\sqrt{\overline{\alpha_t}}}\left(x_{t-1}-\sqrt{1-\overline{\alpha_t}}\widetilde{z}\right)$  , 用这个值替换 $\mu$ 中的 $x_0$, 有如下结果：

$$
\begin{equation}
\begin{aligned}
\mu&=\frac{\sqrt{\alpha_t}(1-\overline{\alpha_{t-1}})}{1-\overline{\alpha_t}}x_t+\frac{\sqrt{\overline{\alpha_{t-1}}}\left(1-\alpha_t\right)}{1-\overline{\alpha_t}}x_0\\
&=\frac{\sqrt{\alpha_t}(1-\overline{\alpha_{t-1}})}{1-\overline{\alpha_t}}x_t+\frac{\sqrt{\overline{\alpha_{t-1}}}\left(1-\alpha_t\right)}{1-\overline{\alpha_t}}\cdot\frac{1}{\sqrt{\overline{\alpha_t}}}\left(x_{t-1}-\sqrt{1-\overline{\alpha_t}}\widetilde{z}\right)\\
&=\frac{1}{\sqrt{\alpha_t}}\left( x_t-\frac{1-\alpha_t}{\sqrt{1-\overline{\alpha_t}}}\widetilde{z} \right)
\end{aligned}
\end{equation}
$$

即

$$
\mu=\frac{1}{\sqrt{\alpha_t}}\left( x_t-\frac{1-\alpha_t}{\sqrt{1-\overline{\alpha_t}}}\widetilde{z} \right)
$$

整个式子中仅有 $\widetilde{z}$ 是一个不可直接获得的值了. 为何会出现一个不能直接获得的 $\widetilde{z}$ 呢？回顾上述过程发现, 这个 $\widetilde{z}$ 是在为了消去 $x_0$ 时引入的一个值. 这个 $\widetilde{z}$ 表示的是在获得 $x_t$ 的过程中,  向 $x_0$ 中加入的噪声. 

为了能够获得这个噪声, 原文使用了一个神经网络进行预测.

在使用神经网络获得 $\widetilde{z}$ 后, $\mu$ 与 $\sigma^2$ 都变的可以计算, 从而 $q(x_{t-1}|x_t,x_0)\sim \mathcal{N}(\mu, \sigma^2)$ 就变成了可以直接获得的高斯分布. 从而 $x_{t-1}$ 就可以轻松的从这个分布中采样获取了.

# 噪声预测器训练过程

在 DDPM 中, 使用 UNet 网络进行噪声图像的预测, 并采样极大似然函数作为损失函数进行预测.

首先我们介绍一下极大似然 hj

## 极大似然估计



1. 输入一个自高斯分布中获取的噪声图像
2. 经过神经网络的操作, 使噪声图像变成一个其他复杂分布的一个实例
3. 这个实例满足的分布与真实分布越接近越好

## 如何衡量生成图像满足的分布与真实分布的差距？

1. 衡量二者之间的差距之前, 我们先做出这样一个假设
	1. 假设我们知道生成模型生成图像满足的分布 $P_{\theta}(X)$
		1. 其中 $X$ 为随机变量
		2. $\theta$ 表示生成模型的参数
2. 其次, 我们定义一些符号
	1.  我们定义真实图像的数据集为 $data$
		1. 从真实数据集 $data$ 中可以获取真实图像 $x_1,x_2,x_3\cdots$
3. 在上述符号定义的前提下, 我们可以知道这样一个事实：
	1. 生成图像满足的分布 $P_\theta(X)$ 中, 随机变量 $X$ 的取值为 $x_i, (i=1,2,3,\cdots)$ 的概率可以表示为 $P_\theta(X=x_i)$ 
	2. 而上述概率 $P_\theta(X=x_i)$ 的含义为：生成模型生成的图像与真实图像一模一样的概率
	3. 这个概率越大, 就说明这个模型生成的图像与真实图像越像
4. 所以如果想让模型生成的图像与真实图像越像, 所以应该概率 $P_\theta(X=x_i), i=1,2,3,\cdots$ 都取最大值
5. 也即 $\prod\limits_{i}P_\theta(X=x_i)$ 达到最大值, 也即 $\max \prod\limits_{i}P_\theta(X=x_i)$
6. 实际上, 这个过程就是极大似然估计的过程
7. 从另一层面来说, 上述累乘求最大值的过程化为 KL 散度, KL 散度表示两个分布之间的相似程度, 如果无法理解极大似然估计的过程, 可以利用 KL 散度进行理解
8. 但实际上, 我们无法直接计算 $P_\theta(X=x_i)$, 因为我们无法获取 $P_\theta$ 这个概率分布, 那么我们应如何计算这个概率分布呢？

## 如何计算 $P_\theta(X=x_i)$ 

有如下定义：

$$
P_\theta(X=x_i)=\int\limits_{z_i\sim\mathcal{N}(0,1)} P(Z=z_i)P_\theta(X=x_i | Z=z_i)dz,
$$
其中, 
1.  $z_i$ 为从高斯分布中采样的噪声图像, $x_i$ 为真实图像
2. 等式左侧为 $P_\theta(X=x_i)$, 其含义为模型生成的图像为 $x_i$ 的概率
3. 等式右侧中, 
	1. $q(Z=z_i)$ 表示从标准正态分布中获取噪声图像为 $z_i$ 的概率, 是一个较为容易计算的概率
	2. $P_\theta(X=x_i | Z=z_i)$ 表示将噪声图像 $z_i$ 输入进生成模型中, 模型生成的图像为 $x_i$ 的概率.

我们需要解释一下这个定义

1. 全概率公式
	1. 上述定义实际上全概率公式的一个积分形式
	2. 值得注意的是, 全概率公式中的条件概率 $P_\theta(X=x_i | Z=z_i)$ 与边缘概率 $P(Z=z_i)$ 并不要求满足同一分布。
	3. 相反，全概率公式的一个关键特性就是它允许我们将条件概率与不同的边缘概率结合起来，从而计算总体的边缘概率。这是全概率公式的核心思想所在。
2. 公式的含义
	1. 由于公式左侧无法计算, 所以考虑使用全概率公式计算.
	2. 模型能够生成图像 $x_i$ 的概率, 等于, 从正态分布中获取噪声图像 $z_i$ 的概率 $P(Z=z_i)$ 与模型在输入噪声图像 $z_i$ 的前提下, 生成图像 $x_i$ 的概率 $P_\theta(X=x_i | Z=z_i)$.


由于噪声图像 $z_i$ 是从正态分布中获取的, 所以 $P(Z=z_i)$ 是一个容易计算的值

在这样的化简下, 问题变成了如何计算 $P_\theta(X=x_i | Z=z_i)$ 

## 如何计算 $P_\theta(X=x_i | Z=z_i)$ 

### 一个符合直觉的定义

实际上, 有一个符合直觉的定义如下：

$$
P_\theta(X=x_i|Z=z_i)=\begin{cases}1, \quad G(z_i)=x_i\\
0, \quad G(z_i)\ne x_i\end{cases}
$$

这个式子中, 
-  $G$ 表示神经网络, 
- $z_i$ 表示输入的噪声图像, 
- $G(z_i)$ 表示输入噪声  $z_i$ 的情况下, 网络生成的图像
- $G(z_i)=x_i$ 表示网络生成的图像与真实图像 $x_i$ 完全相同
- $X$ 是表示真实图像的随机变量, $x_i$ 是 $X$ 的取值
	- 每个 $x_i$ 都是真实世界的一张图像

整个式子表示, 如果网络生成的图像与真实图像完全相同, 则概率 $P_\theta(X=x_i | Z=z_i)$ 为 1, 否则为 0

但实际上, 这个定义是很不合理的. 网络生成的图像与真实图像完全相同的可能性很低, 所以如果用这个「符合直觉的定义」进行计算, 得到的 [[扩散模型过程整理#如何计算 $P_ theta(x)$|$P_\theta(X=x_i)$]] 的结果很显然为 0, 所以需要换一种定义.

### 用 VAE (变分自编码器)类比

#### VAE 中的假设

这是一个 VAE 生成图像的过程.

![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240530105437.png)

在 VAE 中, 有如下假设.

1. 参数设定
	1. 噪声 $z_i$, 
	2. 模型 $G$ 
	3. 模型生成出的图像为 $G(z_i)$.
2. 假设的描述
	1. 给定噪声 $z_i$, 模型 $G$ 生成的图像 $G(z_i)$ 是某个高斯分布的均值
	2. $P_\theta(X| Z)$ 服从于某个高斯分布, 即假设模型生成图像的这个行为是服从高斯分布的
		1. 而非生成的图像是服从某个高斯分布的
3. 假设的解释：为何可以假设为高斯分布？
	1. 在解释假设之前, 我们应该明确的是, 
		1. $P_\theta(X| Z)$ 服从于某个高斯分布, 指的是模型生成图像的「这个行为」是服从高斯分布的
		2. 而非「生成的图像」是服从某个高斯分布的
			1. 图像服从的分布十分复杂, 不是能用高斯分布解释的
			2. 我们只能用高斯分布解释「生成模型 $G$ 的行为」, 即「 $G$ 生成图像的规律」

根据这个假设, 我们可以写出 $P_\theta(X|Z)$ 满足的概率密度, 如下

$$
P_\theta(X|Z) \sim N\left(G(z),\sigma^2\right)
$$
即
$$
P_\theta(X|Z) = \frac{1}{\sqrt{2\pi}\sigma^2}\exp\left[-\frac{1}{2}\cdot\left(\frac{X-G(Z)}{\sigma}\right)^2\right]
$$

从而有
$$
P_\theta(X|Z)\propto \exp(-\Vert X-G(Z)\Vert_2^2)
$$

进一步来说, 如果模型生成的图像 $G(Z)$ 与 $X$ 越接近, 那么概率 $P_\theta(X|Z)$ 越大. 

这个结论有些符合直觉, 但又有些不符合一般认知
- 符合直觉：如果生成图像与真实图像越接近, 那么生成模型能生成的图像与真实图像的概率越大, 这一点是显而易见的
- 有些匪夷所思：与一般的概率密度不一样. 一般的概率密度中, 变化的是随机变量 $X$；而在 VAE 中, 变化的是均值 $G(Z)$ 
	1. 一般的概率密度中, 随机变量 $X$ 是一个变化的量, 而均值是一个不变的量. 当随机变量与 $X$ 越接近时, 概率密度越大. 在概率密度附近的积分, 即概率越大
	2. 而在 VAE 中, 随机变量 $X$ 是一个定值, 而均值 $G(Z)$ 是一个变化的量. 当均值 $G(Z)$ 变化时, 即模型生成的图像变化时, 整个概率概率密度 $P_\theta(X|Z)$ 的对称轴会发生变化.
		1. 当这个均值与真实图像 $X$ 越接近, 则 $P_\theta(X|Z)$ 的概率越大.
		- 当 $G(Z)$ 不断变化时, 高斯分布的图像也随着移动.
		- 当 $G(Z)$ 移动到与真实图像 $X$ 越接近时, 概率 $P_\theta (X|Z)$ 越大
		- 如下图中：![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240531092358.png)
			- 红色的高斯分布的均值 $G(Z)$ 恰好为 $x_i$, 此时的概率密度达到最大, 概率也达到最大
			- 而对于蓝色与绿色的高斯分布来说, 在 $X=x_i$ 处, 概率密度并未达到最大值, 从而影响到概率并未达到最大值

在上面这个假设下, $P_\theta(X|Z)$ 被认为是服从 $\mathcal{N}\left(G(Z),\sigma^2\right)$ 的概率分布, 所以当真实图像 $X=x_i$ 与概率密度的均值 $G(Z)$ 已知的前提下, 概率密度 $P_\theta(X|Z)$ 也变得可以计算了.

在 $P_\theta(X|Z)$ 可计算后, $P_\theta(X)$ 也可以直接计算了

#### VAE 中的操作：最大化 $\log P_\theta(X)$ 的下界

在 $P_\theta(X)$ 变得可以计算后, 我们就有了这样的想法：让模型能够生成「与真实图像十分相近」的图像的概率越大越好,  也即最大化 $P_\theta(X)$ 

但实际上, VAE 中并不是直接最大化 $P_\theta(X)$. 

在 VAE 中, 为了计算 $P_\theta(X)$, 使其达到最大值, 采用的方法往往是最大值 $\log P_\theta(X=x_i)$ 的下界

由于 $P_\theta(X|Z)$ 有如下定义：

$$
P_\theta(X=x_i)=\int\limits_{z_i\sim\mathcal{N}(0,1)} q(Z=z_i)P_\theta(X=x_i | Z=z_i)dz
$$

这是一个基于全概率公式的定义. 

更改全概率公式中的边缘概率一项, 定义可以写成如下形式：

$$
P_\theta(X=x_i)=\int\limits_{z_i\sim\mathcal{N}(0,1)} q(X=x_i)P_\theta(Z=z_i | X=x_i)dz
$$

这个新的定义与原来定义的区别在于, 原来定义中的边缘概率一项为 $P(Z=z_i)$, 而在新的定义中, 边缘概率一项变为了 $q(X=x_i)$, 这样的变化使整个全概率公式发生了变化.

在新的定义下, 在最大化 $\log P_\theta(X)$ 的下界时, 有如下演化：

1. 由于定义中的 $q(X=x_i)$ 一项与积分变量 $dz$ 无关, 所以可以放到积分号前面, 如下：

$$
\begin{equation}
\begin{aligned}
	\log P_\theta(X) &= \log\left[\int\limits_{z_i\sim\mathcal{N}(0,1)}q(X=x_i)P_\theta(Z=z_i|X=x_i)dz\right]\\
		& =\log\left[q(X=x_i)\int\limits_{z_i\sim\mathcal{N}(0,1)}P_\theta(Z=z_i|X=x_i)dz\right]
\end{aligned}
\end{equation}
$$

2. 由于[条件概率密度的积分为 1](https://www.zhihu.com/question/478152820), 所以在上一步式子的基础上进一步演化, 有

$$
\begin{equation}
\begin{aligned}
	上式 &= \log\left[q(X=x_i)\cdot1\right]\\
	&= \log q(X=x_i)\\
	&= \left[\log q(X=x_i)\right]\cdot 1
\end{aligned}
\end{equation}
$$

3. 此时, 再将后面的数字 $1$ 变成概率密度积分的形式, 有

$$
\begin{equation}
\begin{aligned}
	上式 &= \left[\log q(X=x_i)\right]\cdot \int\limits_{z_i\sim\mathcal{N}(0,1)}P_\theta(Z=z_i|X=x_i)dz
\end{aligned}
\end{equation}
$$

4. 由于 $\left[\log q(X=x_i)\right]$ 与积分变量 $dz$ 无关, 所以可以放到积分号内, 有

$$
\begin{equation}
\begin{aligned}
	上式 &= \int\limits_{z_i\sim\mathcal{N}(0,1)}\left[\log P_\theta(X=x_i)\right]\cdot q(Z=z_i|X=x_i)dz
\end{aligned}
\end{equation}
$$

