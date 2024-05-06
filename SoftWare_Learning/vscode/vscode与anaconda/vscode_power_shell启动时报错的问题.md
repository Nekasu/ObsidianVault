
>[!warning] 提示
>点击右上角「书本」![[Pasted image 20231125105318.png]]图标, 进入阅读模式, 以获得更好的阅读体验！

在 windows 中, 启动 vscode 的 power shell 时, 可能会出现报错：Using UTF-8 Encoding (CHCP 65001) in Command Prompt / Windows Powershell, 并打印长长的错误信息

由于问题已经解决, 所以无法截图解决. 此处记录我的解决方案. 解决方法来自于 stack overflow 中的 [Using UTF-8 Encoding (CHCP 65001) in Command Prompt / Windows Powershell (Windows 10)](https://stackoverflow.com/questions/57131654/using-utf-8-encoding-chcp-65001-in-command-prompt-windows-powershell-window).

## 问题分析

由于 vscode 使用的是 UTF-8 编码方式, 而中文 windows 系统默认使用的是 gbk 编码方式, 产生了冲突

若想解决, 则有两种方法：将 vscode 的编码方式改成 gbk, 或将 windows 系统的编码方式改为 utf-8.

我选择第二种方法：将 windows 系统的编码改为 utf-8, 具体流程如下

## 解决方案

1. 按下 `ctrl+r`, 并输入 power shell.
2. 输入 `intl.cpl`, 这个命令将打开 windows 的地区设置
3. 按下图步骤进行操作
	1. ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240506112013.png)
4. 在 power shell 中输入 `$OutputEncoding = [System.Text.UTF8Encoding]::new()`

对于上述命令的解释, 请点开 [Using UTF-8 Encoding (CHCP 65001) in Command Prompt / Windows Powershell (Windows 10)](https://stackoverflow.com/questions/57131654/using-utf-8-encoding-chcp-65001-in-command-prompt-windows-powershell-window) 原文链接进行阅读