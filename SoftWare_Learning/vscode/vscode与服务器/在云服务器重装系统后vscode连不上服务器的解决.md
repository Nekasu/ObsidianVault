
>[!warning] 提示
>点击右上角「书本」![[Pasted image 20231125105318.png]]图标, 进入阅读模式, 以获得更好的阅读体验！

>[!tips] 声明
>本笔记转载自 [CSDN_在云服务器重装系统后vscode连不上服务器的解决](https://blog.csdn.net/weixin_39488566/article/details/107901407)与 [# vscode配置远程连接失败：过程试图写入的管道不存在（已解决）](https://www.jianshu.com/p/7c59ea90693b)

- 问题描述：
	- 之前用 vscode 连接云服务器正常使用，但是服务器重装系统后 vscode 连不上，用 xshell 可以连接，VScode 连接时候提示: 过程试图写入的管道不存在
- 查看报错日志
	- 提示 c:/user/. ssh/known_hosts 存在变化
- 解决
	- （防止误删，建议将 known_hosts 文件备份一下，不能解决再还原）
	- 将 known_hosts 中服务器 IP 所在那一行的内容删掉，重新用 vscode 登录。