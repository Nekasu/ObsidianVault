
>[!warning] 提示
>推荐使用 [obsidian 软件](https://obsidian.md/), 以获得最好的阅读体验
>点击右上角「书本」![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240910163022.png)图标, 进入阅读模式, 以获得更好的阅读体验！
>
>作者：Nekasu/周肖桐

众所周知, 学校的服务器只能通过学校的内网连接. 如果在校外, 则无法连接, 那么有什么方法能解决呢？

可以使用 Zerotier 进行内网穿透, 对于用户而言, 使用以下命令即可

## Step 1. 下载 Zerotier 客户端


下载 [Zerotier](https://www.zerotier.com/download) 客户端, 并安装

###  windows

安装并启动后, 右击图标并输入管理员分配的 NetworkID

![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20241115170240.png)

![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20241115170402.png)


### Linux

请参考 [[linux 系统的 ubuntu 下 zerotier 的基本使用教程_ubuntu zerotier-CSDN博客.pdf]]

## 步骤 2：等待管理员回应

完成以上步骤后, 请通知负责 Zerotier 内网穿透的管理员, 等待他们给出设备 ip 地址.

## 步骤 3：通过 ip 连接设备

通过管理员给出的 ip, 可以访问对应设备, 这种情况下, 可以直接通过 ip 访问校内的服务器