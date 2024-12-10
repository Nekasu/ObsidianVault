
>[!warning] 提示
>点击右上角「书本」![[Pasted image 20231125105318.png]]图标, 进入阅读模式, 以获得更好的阅读体验！

>[!tips] 声明
>本笔记转载自[# Github配置ssh key的步骤（大白话+包含原理解释）](https://blog.csdn.net/weixin_42310154/article/details/118340458)

## 前言

在 github 上配置 ssh key 很容易，网上一大堆教程，但基本没有详细解释其原理的，为什么要配？每使用一台主机都要配？配了为啥就不用密码了？下面将简单通俗地解释一下。

我们在往 github 上 push 项目的时候，如果走 https 的方式，每次都需要输入账号密码，非常麻烦。而采用 ssh 的方式，就不再需要输入，只需要在 github 自己账号下配置一个 ssh key 即可。

### 配置 SSH

Git 使用 SSH 配置，初始需要以下三个步骤
1. 使用秘钥生成工具生成 rsa 秘钥和公钥 
2. 将 rsa 公钥添加到代码托管平台
3. 将 rsa 秘钥添加到 ssh-agent 中，为 ssh client 指定使用的秘钥文件

具体操作如下：

#### 第一步 ：检查本地主机是否已经存在 ssh key

```bash
cd ~/.ssh
ls
//看是否存在 id_rsa 和 id_rsa.pub文件，如果存在，说明已经有SSH Key
```

如下图所示，则表明已经存在

![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240419114410.png)

如果存在，直接跳到第三步

#### 第二步 ：生成 ssh key

如果不存在 ssh key，使用如下命令生成

```bash
ssh-keygen -t rsa -C " xxx@xxx.com "
//执行后一直回车即可
```

生成完以后再用第一步命令，查看 ssh key

#### 第三步 ：获取 ssh key 公钥内容（id_rsa. Pub）

```bash
cd ~/. Ssh
cat id_rsa. Pub
```

如下图所示，复制该内容

![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240419114517.png)

##### 第四步：Github 账号上添加公钥

进入 Settings 设置

![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240419114533.png)

添加 ssh key，把刚才复制的内容粘贴上去保存即可

![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240419114548.png)

#### 第五步：验证是否设置成功

```bash
ssh -T git@github.com
```

显示如下信息表明设置成功

![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240419114618.png)

设置成功后，即可不需要账号密码 clone 和 push 代码

注意之后在 clone 仓库的时候要使用 ssh 的 url，而不是 https！

### 验证原理

SSH 登录安全性由非对称加密保证，产生密钥时，一次产生两个密钥，一个公钥，一个私钥，在 git 中一般命名为 id_rsa. Pub, id_rsa。

那么如何使用生成的一个私钥一个公钥进行验证呢？

本地生成一个密钥对，其中公钥放到远程主机，私钥保存在本地
当本地主机需要登录远程主机时，本地主机向远程主机发送一个登录请求，远程收到消息后，随机生成一个字符串并用公钥加密，发回给本地。本地拿到该字符串，用存放在本地的私钥进行解密，再次发送到远程，远程比对该解密后的字符串与源字符串是否等同，如果等同则认证成功。
通俗解释！！
重点来了：一定要知道 ssh key 的配置是针对每台主机的！，比如我在某台主机上操作 git 和我的远程仓库，想要 push 时不输入账号密码，走 ssh 协议，就需要配置 ssh key，放上去的 key 是当前主机的 ssh 公钥。那么如果我换了一台其他主机，想要实现无密登录，也就需要重新配置。

下面解释开头提出的问题：
1. 为什么要配？
	1. 配了才能实现 push 代码的时候不需要反复输入自己的 github 账号密码，更方便
2. 每使用一台主机都要配？
	1. 是的，每使用一台新主机进行 git 远程操作，想要实现无密，都需要配置。并不是说每个账号配一次就够了，而是每一台主机都需要配。
3. 配了为啥就不用密码了？
	1. 因为配置的时候是把当前主机的公钥放到了你的 github 账号下，相当于当前主机和你的账号做了一个关联，你在这台主机上已经登录了你的账号，此时此刻 github 认为是该账号主人在操作这台主机，在配置 ssh 后就信任该主机了。所以下次在使用 git 的时候即使没有登录 github，也能直接从本地 push 代码到远程了。当然这里不要混淆了，你不能随意 push 你的代码到任何仓库，你只能 push 到你自己的仓库或者其他你有权限的仓库！