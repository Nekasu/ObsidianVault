原文来自[关于国内anaconda镜像站点看这一篇就够啦 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/584580420)

可参考另一篇文件[Windows安装Anaconda并且配置国内镜像教程 | AhtelekB's Blog (gitee.io)](https://ahtelekb.gitee.io/posts/89ec84c4/)

## **为什么要添加镜像？**

在国内使用conda的时候经常会遇到软件下载巨慢甚至直接无法连接的情况。

为了改善这一状况国内涌现出了很多的anaconda的镜像站点，比如清华大学tuna团队维护的清华镜像站点和北外镜像站点大概是目前国内使用人数最多更新也非常及时的站点之一了。

## **添加镜像的命令**

操作挺简单的，用下面这条命令就可以啦。后面`<URLS>`的地方用具体的频道的链接代替就可以了。

```text
conda config --add channels <URLS>
```

另外，在运行过一次上述命令之后，conda会很在家目录下生成`~/.condarc`这么一个文件用于记录信息，然后会自作主张地添加一个`defaults`频道。

然而这个频道是官方频道，（实际上等于添加官方的`main`和`R`这两个频道的内容。）而在国内访问官方频道的时候非常看运气。运气好的时候能连上甚至速度咻咻地，但是运气不好的时候就完全连不上，会遇到`condaHTTPError: HTTP OOO CONNECTION FAILED`的错误。

所以，在国内使用 conda 镜像的时候最好手动删除一下~/.condarc 里的 defaults 频道。否则可能会被它拖累着conda一直在转圈圈。

你可以直接 vim 打开~/.condarc 手动删除掉`defaults`这一行或者运行下面这句命令即可。

```text
sed '/defaults/d' ~/.condarc
```

## **添加镜像的几个注意事项**

1.  频道没必要重复添加。 比如你添加了清华镜像的bioconda频道之后，北外镜像的bioconda频道就没必要添加了，这俩的内容是一致的，没必要又去让conda搜索一遍。
2.  顺序是重要的。 conda在没有指定频道的前提下是从`~/.condarc`文件里从上往下一个频道一个频道去找软件的。所以如果把常用的频道放在最上面有利于更快地找到所需要安装的软件
3.  就我目前的使用体验来看，如果做生物信息学相关的话，只需要添加：

-   bioconda
-   conda-forge
-   main

这三个频道就足够了。剩下的一些不常用频道可以在安装软件的时候手动用`-c`指定。

## **现在可用的 conda 镜像站点**

接下来就盘点一下国内现在提供anaconda镜像服务的站点吧。顺便把命令也给大家准备好了，直接复制粘贴就可以使用啦。

### **1. 阿里云**

-   [https://mirrors.aliyun.com/anaconda/](https://link.zhihu.com/?target=https%3A//mirrors.aliyun.com/anaconda/)

```text
conda config --add channels https://mirrors.aliyun.com/anaconda/pkgs/main/
conda config --add channels https://mirrors.aliyun.com/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.aliyun.com/anaconda/cloud/bioconda/
```

### **2. 北京外国语大学**

-   [https://mirrors.bfsu.edu.cn/help/anaconda/](https://link.zhihu.com/?target=https%3A//mirrors.bfsu.edu.cn/help/anaconda/)

```text
conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/cloud/bioconda/
```

### **3. 清华大学**

-   [https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/](https://link.zhihu.com/?target=https%3A//mirrors.tuna.tsinghua.edu.cn/help/anaconda/)

```text
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
```

### **4. 北京大学**

-   [https://mirrors.pku.edu.cn/Help/Anaconda](https://link.zhihu.com/?target=https%3A//mirrors.pku.edu.cn/Help/Anaconda)

```text
conda config --add channels conda config --add channels https://mirrors.pku.edu.cn/anaconda/pkgs/main/
conda config --add channels conda config --add channels https://mirrors.pku.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels conda config --add channels https://mirrors.pku.edu.cn/anaconda/cloud/bioconda/
```

### **5. 哈尔滨工业大学**

-   [https://mirrors.hit.edu.cn/anaconda/](https://link.zhihu.com/?target=https%3A//mirrors.hit.edu.cn/anaconda/)

```text
conda config --add channels https://mirrors.hit.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.hit.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.hit.edu.cn/anaconda/cloud/bioconda/
```

### **6. 南京大学**

-   [https://mirror.nju.edu.cn/help/anaconda](https://link.zhihu.com/?target=https%3A//mirror.nju.edu.cn/help/anaconda)

```text
conda config --add channels https://mirror.nju.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirror.nju.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirror.nju.edu.cn/anaconda/cloud/bioconda/
```

### **7. 北京交通大学**

-   [https://mirror.bjtu.edu.cn/anaconda/](https://link.zhihu.com/?target=https%3A//mirror.bjtu.edu.cn/anaconda/)

```text
conda config --add channels https://mirror.bjtu.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirror.bjtu.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirror.bjtu.edu.cn/anaconda/cloud/bioconda/
```

### **8. 西安交通大学**

-   [https://mirrors.xjtu.edu.cn/](https://link.zhihu.com/?target=https%3A//mirrors.xjtu.edu.cn/)

```text
conda config --add channels https://mirrors.xjtu.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.xjtu.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.xjtu.edu.cn/anaconda/cloud/bioconda/
```

### **9. 重庆邮电大学**

-   [https://mirrors.cqupt.edu.cn/anaconda/](https://link.zhihu.com/?target=https%3A//mirrors.cqupt.edu.cn/anaconda/)

```text
conda config --add channels https://mirrors.cqupt.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.cqupt.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.cqupt.edu.cn/anaconda/cloud/bioconda/
```

### **10. 南方科技大学**

-   [https://mirrors.sustech.edu.cn/help/anaconda.html#introduction](https://link.zhihu.com/?target=https%3A//mirrors.sustech.edu.cn/help/anaconda.html%23introduction)

```text
conda config --add channels https://mirrors.sustech.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.sustech.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.sustech.edu.cn/anaconda/cloud/bioconda/
```

### **11. 上海交通大学**

-   [https://mirror.sjtu.edu.cn/docs/anaconda](https://link.zhihu.com/?target=https%3A//mirror.sjtu.edu.cn/docs/anaconda)
-   [https://mirrors.sjtug.sjtu.edu.cn/docs/anaconda](https://link.zhihu.com/?target=https%3A//mirrors.sjtug.sjtu.edu.cn/docs/anaconda)

上海交通大学有两个镜像站点，两个里都有 anaconda 的镜像，但是链接似乎跟其他的站点不太一样，因此我这边就不整理啦，需要的同学自己去研究一下吧~

## **已不提供 conda 镜像的站点**

有些站点以前提供过 conda 的镜像，但是后面因为各种原因已不再继续提供

### **中科大镜像**

> [https://mirrors.ustc.edu.cn/help/anaconda.html](https://link.zhihu.com/?target=https%3A//mirrors.ustc.edu.cn/help/anaconda.html)  

打开之后就只见一条警告：

> 由于合规性，Anaconda 源目前已经无限期停止服务。  

### **腾讯镜像**

> [https://mirrors.cloud.tencent.com/help/Anaconda.html](https://link.zhihu.com/?target=https%3A//mirrors.cloud.tencent.com/help/Anaconda.html)  

帮助文档还能打开，但是站点已经 404 了。或许以后会重新开启？我们将会看。

## **官方已废弃的频道：free**

> [https://www.anaconda.com/blog/why-we-removed-the-free-channel-in-conda-4-7](https://link.zhihu.com/?target=https%3A//www.anaconda.com/blog/why-we-removed-the-free-channel-in-conda-4-7)  

anaconda 官方在 2019 年的时候就发了一个推文介绍他们移除了 free 这个频道的原因。我看很多教程（也许包括我自己的）都还在继续使用这个频道。 `“如无必要，勿增实体”。`以后就不要再添加这个频道啦，况且里面的内容都已经分到别的频道里去了。

## **切换镜像站点记得清缓存**

当你从一个站点切换到另一个站点的时候记得运行下面这个命令，否则即使你更新了你的~/.condarc，你的软件还是会从之前的站点下载。

```text
conda clean -i
```

如果你想做个更彻底的清理的话，可以运行下面这个：

```text
conda clean -a
```

这个命令会清除掉：

1.  下载的安装包
2.  解压开但是当前未安装的软件包
3.  为镜像建立的index

## **萌哥碎碎念**

这篇文章实际上是我之前发布在简书的内容。这里略作删改重新po一遍。因为刚好群里有朋友问到conda镜像的问题，顺便就搬运一下过来。

我以前只用简书这一个平台，主要是它的SEO做得非常好搜索结果排名特别靠前。现在你在

-   **微信（萌哥与生信）**
-   **知乎（萌哥与生信）**
-   **简书（卖萌哥）**
-   **语雀（萌哥与生信）**

都能找到我啦。大家在b站会看技术贴吗？会的话我也再运营个b站专栏。有任何的想法和意见都欢迎在留言区跟我交流哦。