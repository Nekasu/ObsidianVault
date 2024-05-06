https://www.itxm.cn/post/hcbfi1a8.html

以下是连接GitHub的完整教程：

1. 安装Git

首先，你需要在你的计算机上安装Git。你可以从Git官网下载适合你操作系统的版本。安装完成后，你可以在命令行中输入以下命令来检查是否安装成功：

 
git --version 

2. 创建一个GitHub账户

如果你还没有GitHub账户，你需要先创建一个。在GitHub的官网上，点击“Sign up”按钮，填写你的个人信息并创建账户。

3. 创建一个新的仓库

在GitHub的主页上，点击“New repository”按钮，填写仓库的名称和描述，选择公开或私有，然后点击“Create repository”按钮。

4. 在本地计算机上创建一个新的Git仓库

在你的本地计算机上，创建一个新的文件夹来存放你的项目。在命令行中进入这个文件夹，然后输入以下命令来初始化一个新的Git仓库：

 git@github.com:Nekasu/ObsidianVault_Learn.git
git init 

5. 将本地仓库与GitHub仓库连接

在GitHub上创建的仓库有一个URL地址，你需要将这个地址添加到你的本地仓库中。在命令行中输入以下命令：

 
git remote add origin https://github.com/你的用户名/你的仓库名.git 

6. 将本地代码推送到GitHub仓库

在你的本地仓库中添加、修改或删除文件后，你需要将这些更改推送到GitHub仓库中。在命令行中输入以下命令：

 
git add . 
git commit -m "提交信息" 
git push origin master 

这些命令将会将你的本地代码推送到GitHub仓库中。

7. 克隆GitHub仓库到本地计算机

如果你需要在另一台计算机上继续开发你的项目，你可以将GitHub仓库克隆到这台计算机上。在命令行中进入你想要存放项目的文件夹，然后输入以下命令：

 
git clone https://github.com/你的用户名/你的仓库名.git 

这些命令将会将GitHub仓库克隆到你的本地计算机上。

以上就是连接GitHub的完整教程。