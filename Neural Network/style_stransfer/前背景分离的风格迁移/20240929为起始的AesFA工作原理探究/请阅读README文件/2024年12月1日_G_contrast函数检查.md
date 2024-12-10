## 输入数据检查

### 输出总结

![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20241201211230.png)

### 基于检查结果的推理

#### 第一次循环

第 1 次循环中, 输入数据均不为 nan. 在输入数据均不为 nan 的情况下, 该损失函数计算结果为依旧为 nan, 说明该损失函数 `G_Contrast` 的计算过程出现错误

观察发现, 该损失函数的计算涉及了生成图像, 所以第一次循环问题的原因可能与下面问题的原因相同

#### 之后的循环

在之后的循环中, 输入数据为生成图像, 或经过 StyleEncoder 后的输出中间结果 o7 为 nan, 而经过 StyleEncoder 后的输出结果 o13 却不为 nan.

说明 StyleEncoder 的计算出现问题, 
### 根据以上推理, 可以得出结论

#### 猜想 1：网络深度问题

因为 o7 为 nan, 而 o13 不为 nan, 所以猜想 StyleEncoder 在编码过程中可能需要一段时间使数据不为 nan.

#### 猜想 2：Encoder 运行逻辑出现问题

在基线工作 AseFA 中, o7 是一个不为 nan 的数, 而在 ParitalAes 中, o7 却是一个 nan, 所以可能是编码器的逻辑出现了问题

### 解决方案

根据以上推理, 可以得到解决方案

#### 针对猜想 1

原始网络中仅仅有两层 OctConv, 也即 o7 为中间输出, o13 为最终输出.

考虑将 StyleEncoder 与ContentEncoder 深度加深, 从 2 层 OctConv 增加为 3 层 OctConv, 从而使 o13 为中间输出, o19 为最终输出.

最终在返回时, 按下表修改三个返回值

|       | 1: 下采样前的结果 | 2_out_sty  | 3_enc_feat     |
| ----- | ---------- | ---------- | -------------- |
| 原始返回值 | out 13     | out 13 下采样 | out 7, out 13  |
| 新返回值  | out 19     | out 19 下采样 | Out 13, out 19 |


#### 针对猜想 2

在猜想 1 被验证为错误的情况下验证猜想 2, 具体到时候再说.

### 详细输出结果

/mnt/sda/zxt/3_code_area/code_develop/PartialConv_AesFA/log/dunhuanglog. Txt
Cuda: cuda:1
Version: dunhuang
Content dir: /mnt/sda/Dataset/Detection/COCO/train 2017
Style dir: /mnt/sda/Dataset/style_image/dunhuang_style/crop_256/origin
Train:  60000 images:  7500 x 8 (batch size) = 60000
\# Of parameter: 6726511
Parameters of networks: {'netE': 825728, 'netS': 825664, 'netG': 1569379, 'vgg_loss': 3505740}
---------------------------在第 0 个 epoch 中的第 0 个循环中---------------------------
输入数据 1 中第 0 个元组的第 1 个 Tensor self. Content_B_feat[0,0] 是否为 nan : False
输入数据 1 中第 0 个元组的第 2 个 Tensor self. Content_B_feat[0,1] 是否为 nan : False
输入数据 1 中第 1 个元组的第 1 个 Tensor self. Content_B_feat[1,0] 是否为 nan : False
输入数据 1 中第 1 个元组的第 2 个 Tensor self. Content_B_feat[1,1] 是否为 nan : False
输入数据 2 中第 0 个元组的第 1 个 Tensor self. Style_B_feat[0,0] 是否为 nan : False
输入数据 2 中第 0 个元组的第 2 个 Tensor self. Style_B_feat[0,1] 是否为 nan : False
输入数据 2 中第 1 个元组的第 1 个 Tensor self. Style_B_feat[1,0] 是否为 nan : False
输入数据 2 中第 1 个元组的第 2 个 Tensor self. Style_B_feat[1,1] 是否为 nan : False
输入数据 2 中第 2 个元组的第 1 个 Tensor self. Style_B_feat[2,0] 是否为 nan : False
输入数据 2 中第 2 个元组的第 2 个 Tensor self. Style_B_feat[2,1] 是否为 nan : False
输入数据 3 中第 0 个元组的第 1 个 Tensor self. Content_trs_AtoB_feat[0,0] 是否为 nan : False
输入数据 3 中第 0 个元组的第 2 个 Tensor self. Content_trs_AtoB_feat[0,1] 是否为 nan : False
输入数据 3 中第 1 个元组的第 1 个 Tensor self. Content_trs_AtoB_feat[1,0] 是否为 nan : False
输入数据 3 中第 1 个元组的第 2 个 Tensor self. Content_trs_AtoB_feat[1,1] 是否为 nan : False
输入数据 4 中第 0 个元组的第 1 个 Tensor self. Style_trs_AtoB_feat[0,0] 是否为 nan : False
输入数据 4 中第 0 个元组的第 2 个 Tensor self. Style_trs_AtoB_feat[0,1] 是否为 nan : False
输入数据 4 中第 1 个元组的第 1 个 Tensor self. Style_trs_AtoB_feat[1,0] 是否为 nan : False
输入数据 4 中第 1 个元组的第 2 个 Tensor self. Style_trs_AtoB_feat[1,1] 是否为 nan : False
输入数据 4 中第 2 个元组的第 1 个 Tensor self. Style_trs_AtoB_feat[2,0] 是否为 nan : False
输入数据 4 中第 2 个元组的第 2 个 Tensor self. Style_trs_AtoB_feat[2,1] 是否为 nan : False
损失函数 G_contrast 是否为 nan: True
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
Tot_itrs: 1/160000 | Epoch: 1 | itr: 1/7500 | Loss_G: nan
------------------------------------------------------------------------------
---------------------------在第 0 个 epoch 中的第 1 个循环中---------------------------
输入数据 1 中第 0 个元组的第 1 个 Tensor self. Content_B_feat[0,0] 是否为 nan : True
输入数据 1 中第 0 个元组的第 2 个 Tensor self. Content_B_feat[0,1] 是否为 nan : True
输入数据 1 中第 1 个元组的第 1 个 Tensor self. Content_B_feat[1,0] 是否为 nan : False
输入数据 1 中第 1 个元组的第 2 个 Tensor self. Content_B_feat[1,1] 是否为 nan : False
输入数据 2 中第 0 个元组的第 1 个 Tensor self. Style_B_feat[0,0] 是否为 nan : True
输入数据 2 中第 0 个元组的第 2 个 Tensor self. Style_B_feat[0,1] 是否为 nan : True
输入数据 2 中第 1 个元组的第 1 个 Tensor self. Style_B_feat[1,0] 是否为 nan : False
输入数据 2 中第 1 个元组的第 2 个 Tensor self. Style_B_feat[1,1] 是否为 nan : False
输入数据 2 中第 2 个元组的第 1 个 Tensor self. Style_B_feat[2,0] 是否为 nan : False
输入数据 2 中第 2 个元组的第 2 个 Tensor self. Style_B_feat[2,1] 是否为 nan : False
输入数据 3 中第 0 个元组的第 1 个 Tensor self. Content_trs_AtoB_feat[0,0] 是否为 nan : True
输入数据 3 中第 0 个元组的第 2 个 Tensor self. Content_trs_AtoB_feat[0,1] 是否为 nan : True
输入数据 3 中第 1 个元组的第 1 个 Tensor self. Content_trs_AtoB_feat[1,0] 是否为 nan : False
输入数据 3 中第 1 个元组的第 2 个 Tensor self. Content_trs_AtoB_feat[1,1] 是否为 nan : False
输入数据 4 中第 0 个元组的第 1 个 Tensor self. Style_trs_AtoB_feat[0,0] 是否为 nan : True
输入数据 4 中第 0 个元组的第 2 个 Tensor self. Style_trs_AtoB_feat[0,1] 是否为 nan : True
输入数据 4 中第 1 个元组的第 1 个 Tensor self. Style_trs_AtoB_feat[1,0] 是否为 nan : False
输入数据 4 中第 1 个元组的第 2 个 Tensor self. Style_trs_AtoB_feat[1,1] 是否为 nan : False
输入数据 4 中第 2 个元组的第 1 个 Tensor self. Style_trs_AtoB_feat[2,0] 是否为 nan : False
输入数据 4 中第 2 个元组的第 2 个 Tensor self. Style_trs_AtoB_feat[2,1] 是否为 nan : False
损失函数 G_contrast 是否为 nan: True
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
Tot_itrs: 2/160000 | Epoch: 1 | itr: 2/7500 | Loss_G: nan
------------------------------------------------------------------------------
---------------------------在第 0 个 epoch 中的第 2 个循环中---------------------------
输入数据 1 中第 0 个元组的第 1 个 Tensor self. Content_B_feat[0,0] 是否为 nan : True
输入数据 1 中第 0 个元组的第 2 个 Tensor self. Content_B_feat[0,1] 是否为 nan : True
输入数据 1 中第 1 个元组的第 1 个 Tensor self. Content_B_feat[1,0] 是否为 nan : False
输入数据 1 中第 1 个元组的第 2 个 Tensor self. Content_B_feat[1,1] 是否为 nan : False
输入数据 2 中第 0 个元组的第 1 个 Tensor self. Style_B_feat[0,0] 是否为 nan : True
输入数据 2 中第 0 个元组的第 2 个 Tensor self. Style_B_feat[0,1] 是否为 nan : True
输入数据 2 中第 1 个元组的第 1 个 Tensor self. Style_B_feat[1,0] 是否为 nan : False
输入数据 2 中第 1 个元组的第 2 个 Tensor self. Style_B_feat[1,1] 是否为 nan : False
输入数据 2 中第 2 个元组的第 1 个 Tensor self. Style_B_feat[2,0] 是否为 nan : False
输入数据 2 中第 2 个元组的第 2 个 Tensor self. Style_B_feat[2,1] 是否为 nan : False
输入数据 3 中第 0 个元组的第 1 个 Tensor self. Content_trs_AtoB_feat[0,0] 是否为 nan : True
输入数据 3 中第 0 个元组的第 2 个 Tensor self. Content_trs_AtoB_feat[0,1] 是否为 nan : True
输入数据 3 中第 1 个元组的第 1 个 Tensor self. Content_trs_AtoB_feat[1,0] 是否为 nan : False
输入数据 3 中第 1 个元组的第 2 个 Tensor self. Content_trs_AtoB_feat[1,1] 是否为 nan : False
输入数据 4 中第 0 个元组的第 1 个 Tensor self. Style_trs_AtoB_feat[0,0] 是否为 nan : True
输入数据 4 中第 0 个元组的第 2 个 Tensor self. Style_trs_AtoB_feat[0,1] 是否为 nan : True
输入数据 4 中第 1 个元组的第 1 个 Tensor self. Style_trs_AtoB_feat[1,0] 是否为 nan : False
输入数据 4 中第 1 个元组的第 2 个 Tensor self. Style_trs_AtoB_feat[1,1] 是否为 nan : False
输入数据 4 中第 2 个元组的第 1 个 Tensor self. Style_trs_AtoB_feat[2,0] 是否为 nan : False
输入数据 4 中第 2 个元组的第 2 个 Tensor self. Style_trs_AtoB_feat[2,1] 是否为 nan : False
损失函数 G_contrast 是否为 nan: True
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
Tot_itrs: 3/160000 | Epoch: 1 | itr: 3/7500 | Loss_G: nan
------------------------------------------------------------------------------
---------------------------在第 0 个 epoch 中的第 3 个循环中---------------------------
输入数据 1 中第 0 个元组的第 1 个 Tensor self. Content_B_feat[0,0] 是否为 nan : True
输入数据 1 中第 0 个元组的第 2 个 Tensor self. Content_B_feat[0,1] 是否为 nan : True
输入数据 1 中第 1 个元组的第 1 个 Tensor self. Content_B_feat[1,0] 是否为 nan : False
输入数据 1 中第 1 个元组的第 2 个 Tensor self. Content_B_feat[1,1] 是否为 nan : False
输入数据 2 中第 0 个元组的第 1 个 Tensor self. Style_B_feat[0,0] 是否为 nan : True
输入数据 2 中第 0 个元组的第 2 个 Tensor self. Style_B_feat[0,1] 是否为 nan : True
输入数据 2 中第 1 个元组的第 1 个 Tensor self. Style_B_feat[1,0] 是否为 nan : False
输入数据 2 中第 1 个元组的第 2 个 Tensor self. Style_B_feat[1,1] 是否为 nan : False
输入数据 2 中第 2 个元组的第 1 个 Tensor self. Style_B_feat[2,0] 是否为 nan : False
输入数据 2 中第 2 个元组的第 2 个 Tensor self. Style_B_feat[2,1] 是否为 nan : False
输入数据 3 中第 0 个元组的第 1 个 Tensor self. Content_trs_AtoB_feat[0,0] 是否为 nan : True
输入数据 3 中第 0 个元组的第 2 个 Tensor self. Content_trs_AtoB_feat[0,1] 是否为 nan : True
输入数据 3 中第 1 个元组的第 1 个 Tensor self. Content_trs_AtoB_feat[1,0] 是否为 nan : False
输入数据 3 中第 1 个元组的第 2 个 Tensor self. Content_trs_AtoB_feat[1,1] 是否为 nan : False
输入数据 4 中第 0 个元组的第 1 个 Tensor self. Style_trs_AtoB_feat[0,0] 是否为 nan : True
输入数据 4 中第 0 个元组的第 2 个 Tensor self. Style_trs_AtoB_feat[0,1] 是否为 nan : True
输入数据 4 中第 1 个元组的第 1 个 Tensor self. Style_trs_AtoB_feat[1,0] 是否为 nan : False
输入数据 4 中第 1 个元组的第 2 个 Tensor self. Style_trs_AtoB_feat[1,1] 是否为 nan : False
输入数据 4 中第 2 个元组的第 1 个 Tensor self. Style_trs_AtoB_feat[2,0] 是否为 nan : False
输入数据 4 中第 2 个元组的第 2 个 Tensor self. Style_trs_AtoB_feat[2,1] 是否为 nan : False
损失函数 G_contrast 是否为 nan: True
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
Tot_itrs: 4/160000 | Epoch: 1 | itr: 4/7500 | Loss_G: nan
------------------------------------------------------------------------------
---------------------------在第 0 个 epoch 中的第 4 个循环中---------------------------
输入数据 1 中第 0 个元组的第 1 个 Tensor self. Content_B_feat[0,0] 是否为 nan : True
输入数据 1 中第 0 个元组的第 2 个 Tensor self. Content_B_feat[0,1] 是否为 nan : True
输入数据 1 中第 1 个元组的第 1 个 Tensor self. Content_B_feat[1,0] 是否为 nan : False
输入数据 1 中第 1 个元组的第 2 个 Tensor self. Content_B_feat[1,1] 是否为 nan : False
输入数据 2 中第 0 个元组的第 1 个 Tensor self. Style_B_feat[0,0] 是否为 nan : True
输入数据 2 中第 0 个元组的第 2 个 Tensor self. Style_B_feat[0,1] 是否为 nan : True
输入数据 2 中第 1 个元组的第 1 个 Tensor self. Style_B_feat[1,0] 是否为 nan : False
输入数据 2 中第 1 个元组的第 2 个 Tensor self. Style_B_feat[1,1] 是否为 nan : False
输入数据 2 中第 2 个元组的第 1 个 Tensor self. Style_B_feat[2,0] 是否为 nan : False
输入数据 2 中第 2 个元组的第 2 个 Tensor self. Style_B_feat[2,1] 是否为 nan : False
输入数据 3 中第 0 个元组的第 1 个 Tensor self. Content_trs_AtoB_feat[0,0] 是否为 nan : True
输入数据 3 中第 0 个元组的第 2 个 Tensor self. Content_trs_AtoB_feat[0,1] 是否为 nan : True
输入数据 3 中第 1 个元组的第 1 个 Tensor self. Content_trs_AtoB_feat[1,0] 是否为 nan : False
输入数据 3 中第 1 个元组的第 2 个 Tensor self. Content_trs_AtoB_feat[1,1] 是否为 nan : False
输入数据 4 中第 0 个元组的第 1 个 Tensor self. Style_trs_AtoB_feat[0,0] 是否为 nan : True
输入数据 4 中第 0 个元组的第 2 个 Tensor self. Style_trs_AtoB_feat[0,1] 是否为 nan : True
输入数据 4 中第 1 个元组的第 1 个 Tensor self. Style_trs_AtoB_feat[1,0] 是否为 nan : False
输入数据 4 中第 1 个元组的第 2 个 Tensor self. Style_trs_AtoB_feat[1,1] 是否为 nan : False
输入数据 4 中第 2 个元组的第 1 个 Tensor self. Style_trs_AtoB_feat[2,0] 是否为 nan : False
输入数据 4 中第 2 个元组的第 2 个 Tensor self. Style_trs_AtoB_feat[2,1] 是否为 nan : False
损失函数 G_contrast 是否为 nan: True
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
Tot_itrs: 5/160000 | Epoch: 1 | itr: 5/7500 | Loss_G: nan
------------------------------------------------------------------------------
---------------------------在第 0 个 epoch 中的第 5 个循环中---------------------------
输入数据 1 中第 0 个元组的第 1 个 Tensor self. Content_B_feat[0,0] 是否为 nan : True
输入数据 1 中第 0 个元组的第 2 个 Tensor self. Content_B_feat[0,1] 是否为 nan : True
输入数据 1 中第 1 个元组的第 1 个 Tensor self. Content_B_feat[1,0] 是否为 nan : False
输入数据 1 中第 1 个元组的第 2 个 Tensor self. Content_B_feat[1,1] 是否为 nan : False
输入数据 2 中第 0 个元组的第 1 个 Tensor self. Style_B_feat[0,0] 是否为 nan : True
输入数据 2 中第 0 个元组的第 2 个 Tensor self. Style_B_feat[0,1] 是否为 nan : True
输入数据 2 中第 1 个元组的第 1 个 Tensor self. Style_B_feat[1,0] 是否为 nan : False
输入数据 2 中第 1 个元组的第 2 个 Tensor self. Style_B_feat[1,1] 是否为 nan : False
输入数据 2 中第 2 个元组的第 1 个 Tensor self. Style_B_feat[2,0] 是否为 nan : False
输入数据 2 中第 2 个元组的第 2 个 Tensor self. Style_B_feat[2,1] 是否为 nan : False
输入数据 3 中第 0 个元组的第 1 个 Tensor self. Content_trs_AtoB_feat[0,0] 是否为 nan : True
输入数据 3 中第 0 个元组的第 2 个 Tensor self. Content_trs_AtoB_feat[0,1] 是否为 nan : True
输入数据 3 中第 1 个元组的第 1 个 Tensor self. Content_trs_AtoB_feat[1,0] 是否为 nan : False
输入数据 3 中第 1 个元组的第 2 个 Tensor self. Content_trs_AtoB_feat[1,1] 是否为 nan : False
输入数据 4 中第 0 个元组的第 1 个 Tensor self. Style_trs_AtoB_feat[0,0] 是否为 nan : True
输入数据 4 中第 0 个元组的第 2 个 Tensor self. Style_trs_AtoB_feat[0,1] 是否为 nan : True
输入数据 4 中第 1 个元组的第 1 个 Tensor self. Style_trs_AtoB_feat[1,0] 是否为 nan : False
输入数据 4 中第 1 个元组的第 2 个 Tensor self. Style_trs_AtoB_feat[1,1] 是否为 nan : False
输入数据 4 中第 2 个元组的第 1 个 Tensor self. Style_trs_AtoB_feat[2,0] 是否为 nan : False
输入数据 4 中第 2 个元组的第 2 个 Tensor self. Style_trs_AtoB_feat[2,1] 是否为 nan : False
损失函数 G_contrast 是否为 nan: True
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
Tot_itrs: 6/160000 | Epoch: 1 | itr: 6/7500 | Loss_G: nan
------------------------------------------------------------------------------
---------------------------在第 0 个 epoch 中的第 6 个循环中---------------------------
输入数据 1 中第 0 个元组的第 1 个 Tensor self. Content_B_feat[0,0] 是否为 nan : True
输入数据 1 中第 0 个元组的第 2 个 Tensor self. Content_B_feat[0,1] 是否为 nan : True
输入数据 1 中第 1 个元组的第 1 个 Tensor self. Content_B_feat[1,0] 是否为 nan : False
输入数据 1 中第 1 个元组的第 2 个 Tensor self. Content_B_feat[1,1] 是否为 nan : False
输入数据 2 中第 0 个元组的第 1 个 Tensor self. Style_B_feat[0,0] 是否为 nan : True
输入数据 2 中第 0 个元组的第 2 个 Tensor self. Style_B_feat[0,1] 是否为 nan : True
输入数据 2 中第 1 个元组的第 1 个 Tensor self. Style_B_feat[1,0] 是否为 nan : False
输入数据 2 中第 1 个元组的第 2 个 Tensor self. Style_B_feat[1,1] 是否为 nan : False
输入数据 2 中第 2 个元组的第 1 个 Tensor self. Style_B_feat[2,0] 是否为 nan : False
输入数据 2 中第 2 个元组的第 2 个 Tensor self. Style_B_feat[2,1] 是否为 nan : False
输入数据 3 中第 0 个元组的第 1 个 Tensor self. Content_trs_AtoB_feat[0,0] 是否为 nan : True
输入数据 3 中第 0 个元组的第 2 个 Tensor self. Content_trs_AtoB_feat[0,1] 是否为 nan : True
输入数据 3 中第 1 个元组的第 1 个 Tensor self. Content_trs_AtoB_feat[1,0] 是否为 nan : False
输入数据 3 中第 1 个元组的第 2 个 Tensor self. Content_trs_AtoB_feat[1,1] 是否为 nan : False
输入数据 4 中第 0 个元组的第 1 个 Tensor self. Style_trs_AtoB_feat[0,0] 是否为 nan : True
输入数据 4 中第 0 个元组的第 2 个 Tensor self. Style_trs_AtoB_feat[0,1] 是否为 nan : True
输入数据 4 中第 1 个元组的第 1 个 Tensor self. Style_trs_AtoB_feat[1,0] 是否为 nan : False
输入数据 4 中第 1 个元组的第 2 个 Tensor self. Style_trs_AtoB_feat[1,1] 是否为 nan : False
输入数据 4 中第 2 个元组的第 1 个 Tensor self. Style_trs_AtoB_feat[2,0] 是否为 nan : False
输入数据 4 中第 2 个元组的第 2 个 Tensor self. Style_trs_AtoB_feat[2,1] 是否为 nan : False
损失函数 G_contrast 是否为 nan: True
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
Tot_itrs: 7/160000 | Epoch: 1 | itr: 7/7500 | Loss_G: nan
------------------------------------------------------------------------------
---------------------------在第 0 个 epoch 中的第 7 个循环中---------------------------
输入数据 1 中第 0 个元组的第 1 个 Tensor self. Content_B_feat[0,0] 是否为 nan : True
输入数据 1 中第 0 个元组的第 2 个 Tensor self. Content_B_feat[0,1] 是否为 nan : True
输入数据 1 中第 1 个元组的第 1 个 Tensor self. Content_B_feat[1,0] 是否为 nan : False
输入数据 1 中第 1 个元组的第 2 个 Tensor self. Content_B_feat[1,1] 是否为 nan : False
输入数据 2 中第 0 个元组的第 1 个 Tensor self. Style_B_feat[0,0] 是否为 nan : True
输入数据 2 中第 0 个元组的第 2 个 Tensor self. Style_B_feat[0,1] 是否为 nan : True
输入数据 2 中第 1 个元组的第 1 个 Tensor self. Style_B_feat[1,0] 是否为 nan : False
输入数据 2 中第 1 个元组的第 2 个 Tensor self. Style_B_feat[1,1] 是否为 nan : False
输入数据 2 中第 2 个元组的第 1 个 Tensor self. Style_B_feat[2,0] 是否为 nan : False
输入数据 2 中第 2 个元组的第 2 个 Tensor self. Style_B_feat[2,1] 是否为 nan : False
输入数据 3 中第 0 个元组的第 1 个 Tensor self. Content_trs_AtoB_feat[0,0] 是否为 nan : True
输入数据 3 中第 0 个元组的第 2 个 Tensor self. Content_trs_AtoB_feat[0,1] 是否为 nan : True
输入数据 3 中第 1 个元组的第 1 个 Tensor self. Content_trs_AtoB_feat[1,0] 是否为 nan : False
输入数据 3 中第 1 个元组的第 2 个 Tensor self. Content_trs_AtoB_feat[1,1] 是否为 nan : False
输入数据 4 中第 0 个元组的第 1 个 Tensor self. Style_trs_AtoB_feat[0,0] 是否为 nan : True
输入数据 4 中第 0 个元组的第 2 个 Tensor self. Style_trs_AtoB_feat[0,1] 是否为 nan : True
输入数据 4 中第 1 个元组的第 1 个 Tensor self. Style_trs_AtoB_feat[1,0] 是否为 nan : False
输入数据 4 中第 1 个元组的第 2 个 Tensor self. Style_trs_AtoB_feat[1,1] 是否为 nan : False
输入数据 4 中第 2 个元组的第 1 个 Tensor self. Style_trs_AtoB_feat[2,0] 是否为 nan : False
输入数据 4 中第 2 个元组的第 2 个 Tensor self. Style_trs_AtoB_feat[2,1] 是否为 nan : False
损失函数 G_contrast 是否为 nan: True
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.
NaN or Inf found in input tensor.