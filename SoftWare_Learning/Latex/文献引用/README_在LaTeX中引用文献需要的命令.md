
在 LaTeX 中引用文献时，通常需要以下几个必要的命令和步骤：

## 在导言区加载需要的包

```latex
\usepackage{cite} %使用\cite{}命令所必须的包
\usepackage[hidelinks]{hyperref} %使引用文献可以跳转的包
```

在 `\usepackage[hidelinks]{hyperref}` 中, 如果没有 `[hidelinks]` , 则生成的 PDF 中将有绿色的超链接框, 如下图所示：

![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240701170538.png)


## 在正文末尾指定参考文献样式

```latex
\bibliographystyle{IEEEtran} 
```

这里大括号里的 IEEEtran 文件的后缀为 `.bst`.

具体来说，`IEEEtrans.bst` 是一个 BibTeX 样式文件，用于格式化文献引用，符合 IEEE（电气电子工程师学会）的引用格式要求。

当你使用 `\bibliographystyle{IEEEtrans}` 时，LaTeX 系统会查找名为 `IEEEtrans.bst` 的文件来确定如何格式化你的参考文献列表。因此，你需要确保 `IEEEtrans.bst` 文件与你的主文件在同一目录中。

## 在正文末尾插入文献数据库文件

```latex
\bibliography{references}
```

这里 `references` 是你的 [[bib文件|.bib 文件]] 的名称，不需要写扩展名。

## 在文中插入引用 

```latex
这是一段文字\cite{key}.
```

   其中 `key` 是你在 [[bib文件|.bib 文件]] 中为特定文献条目指定的唯一标识符, 如下图中红色框所表示的内容：

![|500](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240628224241.png)

### 详细步骤

#### Step 1. 创建 `.bib` 文件

你需要一个包含所有参考文献条目的 `.bib` 文件，格式如下：
   
```bibtex
@article{key,
 author = {Author Name},
 title = {Title of the Article},
 journal = {Journal Name},
 year = {2023},
 volume = {42},
 number = {3},
 pages = {1-10},
 month = {Jan},
 note = {Some note},
 doi = {10.1234/example.doi}
}
```

创建 `.bib` 文件的方法请见 [[bib文件#bib 文件的创建]]

#### Step 2.  LaTeX 文件的导言区加载包

```latex
\usepackage{cite}
\usepackage{hyperref} %使引用文献可以跳转的包
```


#### Step 3.  指定参考文献样式

   在导言区指定你想使用的参考文献样式，例如 IEEE 格式：
   
```latex
\bibliographystyle{IEEEtran} % 这里的 IEEEtran 文件的后缀为 .bst
```

#### Step 4.  生成参考文献列表

在文档的结尾处添加 `\bibliography{references}` 命令：
   
```latex
\begin{document}
% 文档内容
\bibliography{references}
\end{document}
```

#### Step 5. 在文中插入引用

   在你需要引用的地方插入 `\cite{key}` 命令，例如：

```latex
根据文献\cite{key}，我们可以得出以下结论。
```


### 完整示例

以下是一个完整的 LaTeX 文件示例：

```latex
\documentclass{article}
\usepackage{cite}

\begin{document}

\title{Example Document}
\author{Author Name}
\date{\today}
\maketitle

\section{Introduction}
这是一个引用示例\cite{key}。

\bibliographystyle{IEEEtran}
\bibliography{references}

\end{document}
```

假设你的 `references.bib` 文件包含以下内容：

```bibtex
@article{key,
  author = {Author Name},
  title = {Title of the Article},
  journal = {Journal Name},
  year = {2023},
  volume = {42},
  number = {3},
  pages = {1-10},
  month = {Jan},
  note = {Some note},
  doi = {10.1234/example.doi}
}
```

### 编译过程

为了生成最终的 PDF 文档，你需要按照以下步骤编译你的 LaTeX 文件 (如果你使用的是 overleaf 则可以忽略以下操作)：

1. 使用 `pdflatex` 或`xelatex`编译你的主 `.tex` 文件。
2. 使用 `bibtex` 编译生成的 `.aux` 文件。
3. 再次使用 `pdflatex` 编译两次, 或使用 `xelatex` 编译两次，以确保引用和参考文献列表正确更新。

通过这些步骤，你可以在 LaTeX 中正确地插入和引用文献。

### 一些可能的问题

如果出现报错, 可以试着删除一些不重要的文件, 重新进行 bibtex 的编译. 如错误的 `.bbl` 文件可能导致整个 LaTeX 项目编译出错, 所以可能需要删除这个文件, 让 bibtex 重新进行编译

#### 没有使用 `\cite` 命令

如果使用了 `pdflatex->bibtex->pdflatex->pdflatex` 的编译链, 但文章中没有使用 `\cite` 命令, 可能导致整个项目编译出错. 