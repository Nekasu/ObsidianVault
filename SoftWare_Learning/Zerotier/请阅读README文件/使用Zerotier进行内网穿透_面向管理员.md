
>[!warning] 提示
>推荐使用 [obsidian 软件](https://obsidian.md/), 以获得最好的阅读体验
>点击右上角「书本」![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240910163022.png)图标, 进入阅读模式, 以获得更好的阅读体验！
>
>作者：Nekasu/周肖桐

众所周知, 学校的服务器只能通过学校的内网连接. 如果在校外, 则无法连接, 那么有什么方法能解决呢？

可以使用 Zerotier 进行内网穿透, 为此, 我们需要一个 Zerotier 的账户充当管理员. 

## 步骤 1：内网穿透管理员前期工作

### 注册帐号

登录官网注册即可，填写你的邮箱和密码。

![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20241115165710.png)

注册之后是这样的，保持默认就好。

![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20241115165746.png)

### 网络配置

注册好之后，我们来建立一个 Network 并分配内网网段。

![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20241115165807.png)

NetworkID 需要分发给其他用户.

## 步骤 2：客户端操作

下载 [Zerotie](https://www.zerotier.com/download) 客户端, 并安装

###  windows

安装并启动后, 右击图标并输入管理员分配的 NetworkID

![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20241115170240.png)

![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20241115170402.png)

### Linux

请参考 [[linux 系统的 ubuntu 下 zerotier 的基本使用教程_ubuntu zerotier-CSDN博客.pdf]]

注意记得添加开机自启动：sudo systemctl enable zerotier-one.service

## 步骤 3：管理员同意申请

客户端加入后，zerotier 的 Web 管理页面就能看到该网络，勾选该网络，表示同意客户端接入

![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20241115170923.png)

勾选后，管理端会随机分配一个 IP 地址给这台客户端，同时也可以自定义一个 IP 地址。例如我加入了多台内网服务器，并自定义了 IP 地址和名称：

![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20241115170938.png)

## 步骤 3：管理员告知用户 ip

将设备 ip 告知给用户, 完成.