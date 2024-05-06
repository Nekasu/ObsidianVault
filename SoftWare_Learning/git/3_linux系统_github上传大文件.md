https://cloud.tencent.com/developer/article/1677003

>[!warning] 提示
>点击右上角「书本」![[Pasted image 20231125105318.png]]图标, 进入阅读模式, 以获得更好的阅读体验！


>[!tips] 声明
>本笔记参考了[这里](https://cloud.tencent.com/developer/article/1677003)与[这里](https://zhuanlan.zhihu.com/p/65131817)

## 引言 

在软件开发和协作过程中，版本控制系统是至关重要的工具。GitHub 作为最受欢迎的代码托管平台之一，为开发人员提供了一个便捷的方式来托管、共享和协作开发项目。

然而，在处理大型文件 (>100mb) 时，git 可能会面临一些挑战，比如文件大小限制、存储成本以及传输效率等问题。为了解决这些问题，GitHub 引入了 Git LFS（Large File Storage），这是一个用于管理和存储大型文件的扩展。

Git LFS 使得开发团队能够轻松地处理大型数据文件、多媒体文件和其他体积庞大的资源，而无需担心存储限制或传输效率。本文将介绍如何使用 Git LFS 将大型文件上传到 GitHub

## 安装 git gfs

在 ubuntu 的命令行中运行以下代码可以安装 git gfs

```console
sudo apt-get install git-lfs
```

- 进入需要使用 git gfs 的仓库
	- 如果没有 git 仓库, 则需要按以下步骤创建 git 仓库
	- ![[2_将本地仓库推送到远程仓库#第1步：建立本地 git 仓库]]

## 安装检测

在命令行中输入以下命令：

```console
git lfs install
```

如果显示"Git LFS initialized"则表示安装成功

## 使用 git lfs

### 创建".gitattributes"文件

进入需要使用 git lfs 管理的 git 仓库, 使用以下命令将需要上传的大文件加入列表

```console
git lfs track "大文件的文件名"
```

如果想要加入一个类型的文件, 可以使用如下命令 (以.jpg 文件为例)

```console
git lfs track ".jpg"
```

执行完命令后会发现目录下生成了一个"**.gitattributes**"文件，文件内记录了我们要上传文件的信息。只有先把".gitattributes"传上去，才可以上传大文件。

### 提交".gitattributes"文件

使用以下命令提交".gitattributes"文件

```console
git add .gitattributes 
git commit -m "submit file"
git push -u origin master
```

完成后, 即可向 github 提交大文件
