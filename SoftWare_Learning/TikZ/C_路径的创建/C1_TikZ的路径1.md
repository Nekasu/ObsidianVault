本章内容来自TikZ官方文档的第14章(p153)

# 总览

## 路径的含义与作用

路径是一系列直的或弯的线, 他们有着自己的语法

在TikZ中，`path`是一种用于绘制图形的基本命令。它由一系列的点和线段组成，用于描述绘制的路径。
可以通过在路径上设置不同的样式和属性来控制路径的外观，例如线条颜色、粗细、线型、填充颜色等。
路径可以是闭合的或非闭合的，可以包含多个子路径。路径可以用于绘制任何类型的图形，如直线、曲线、多边形、圆、椭圆等。

# 14.1 Move-to操作

## 简单的move-to指令

`move-to`操作是最简单的操作, 该操作一般以一个坐标作为开始, 每`个move-to`命令都会重新画一条线, 且不会进行平滑处理, 这一点与[[C1_TikZ的路径1#14.2 Line-to操作|line-to指令]]有明显区别, 以下是`move-to`操作的代码
```latex
\begin{tikzpicture}[thick]
	%一个简单的move-to指令, 可以用"--"或"to"实现
	\draw (0,0) -- (2,0) (0,1) to (2,1);
\end{tikzpicture}
```
效果如下所示
```tikz
\usepackage{tikz}
\usetikzlibrary{scopes}
\begin{document}
\begin{tikzpicture}[thick]
	\draw (0,0) -- (2,0) (0,1) to (2,1);
\end{tikzpicture}
\end{document}
```
其中, `(0,0) to (2,0)`和`(0,1) to (2.1)`是两个`move to`指令
`to (2,0)`和`to (2,1)`是两个[[C1_TikZ的路径1#14.2 Line-to操作|line-to]]指令, 在后面会介绍


## current subpath start命令

该命令代表一个坐标, 该坐标是当前路径的第一个坐标(起始坐标, 开始坐标), 如下所示
```latex
\begin{tikzpicture}[line width=2mm]
	{\draw (0,0) -- (1,0) -- (1,1) -- (0,1) -- (current subpath start);}
\end{tikzpicture}
```
效果如下所示:
```tikz
\usepackage{tikz}
\usetikzlibrary{scopes}

\begin{document}
\begin{tikzpicture}[line width=2mm]
	{\draw (0,0) -- (1,0) -- (1,1) -- (0,1) to (current subpath start);}
\end{tikzpicture}
\end{document}

```

注意! 使用`(current subpath start)`并不会造成路径的闭合, 这与[[C1_TikZ的路径1#cycle指令|`cycle`命令]]有区别!

# 14.2 Line-to操作

## 简单的line-to指令

将多个`move-to`操作进行合并就是`line-to`操作, 以下是一个例子
```latex
\begin{tikzpicture}[line width=5pt]
	%一系列move-to指令
	\draw (0,0)--(0,1) (0,1)--(1,1);
	%对应的line-to指令
	\draw (2,0)--(2,1)--(3,1);
\end{tikzpicture}
```
效果如下所示:
```tikz
\usepackage{tikz}
\usetikzlibrary{scopes}

\begin{document}

\begin{tikzpicture}[line width=5pt]
	%一系列move-to指令
	\draw (0,0)--(0,1) (0,1)--(1,1);
	%对应的line-to指令
	\draw (2,0)--(2,1)--(3,1);
\end{tikzpicture}

\end{document}
```

左边为`move-to`指令, 右边为`line-to`指令, 可以发现明显区别: <mark style="background: #FFB8EBA6;">line-to指令会对中间的点做平滑处理, 但move-to不会</mark>

## cycle指令

该命令代表一个坐标, 该坐标是当前路径的第一个坐标, 如下所示
```latex
\begin{tikzpicture}[line width=2mm]
	{\draw (0,0) -- (1,0) -- (1,1) -- (0,1) to (cycle);}
\end{tikzpicture}
```
效果如下所示:
```tikz
\usepackage{tikz}
\usetikzlibrary{scopes}

\begin{document}
\begin{tikzpicture}[line width=2mm]
	{\draw (0,0) -- (1,0) -- (1,1) -- (0,1) to cycle;}
\end{tikzpicture}
\end{document}

```

注意! 使用`cycle`并会造成路径的闭合, 这与[[C1_TikZ的路径1#current subpath start命令|current subpath start命令]]有区别!

## 垂直与水平的折线

可以使用`|-`表示`先垂直后水平`的线段, 使用时代替`--`即可,
同理, 可以使用`-|`表示`先水平后垂直的`线段, 使用时代替`--`即可.

以下是一个例子
```latex
\begin{tikzpicture}
	%在(0,0)处画一个节点A
	\draw (0,0) node(a) [draw] {A};
	%在(1,1)处画一个节点B
	\draw (1,1) node(b) [draw] {B};
	\draw (a.north) |- (b.west);
	\draw[color=red] (a.east) -| (2,1.5) -| (b.north);
\end{tikzpicture}
```
效果如下所示

```tikz
\usepackage{tikz}
\usetikzlibrary{scopes}

\begin{document}
\begin{tikzpicture}
	\draw (0,0) node(a) [draw] {A};
	\draw (1,1) node(b) [draw] {B};
	\draw (a.north) |- (b.west);
	\draw[color=red] (a.east) -| (2,1.5) -| (b.north);
\end{tikzpicture}
\end{document}
```

# 14.3 Curve-to操作

利用[贝塞尔曲线原理](https://zhuanlan.zhihu.com/p/344934774)进行曲线绘制的操作,  其代码如下所示
```latex
<x> ..controls<c>and<d>.. <y or cycle>
```
其中, `x`表示曲线的起始点, `y`表示曲线的终止点, 其中的`c`和`d`表示控制曲线走向的点, 可以用`cycle`替换`y`

以下是一段简单的示例代码
```latex
\begin{tikzpicture}
	%利用贝塞尔曲线原理绘制的曲线
	\draw[line width=5pt] (0,0) .. controls (1,1)and(3,2).. (4,0);
	%路径上的点
	\draw[color=gray] (0,0) -- (1,1) -- (3,2) -- (4,0);
\end{tikzpicture}
```

```tikz
\usepackage{tikz}

\begin{document}
\begin{tikzpicture}
	%利用贝塞尔曲线原理绘制的曲线
	\draw[line width=5pt] (0,0) .. controls (1,1)and(3,2).. (4,0);
	%路径上的点
	\draw[color=gray] (0,0) -- (1,1) -- (3,2) -- (4,0);
\end{tikzpicture}
\end{document}
```

以下是一段较为复杂的代码样例
```latex
\begin{tikzpicture}
	\draw[line width=3pt] (0,0) .. controls(1,3).. (4,0) ..controls(5,1)and(4,3).. cycle;
	\draw[color=gray] (0,0)-- (1,3) -- (4,0) -- (5,1) -- (4,3) -- cycle;
\end{tikzpicture}
```
以下是实例:
```tikz
\usepackage{tikz}


\begin{document}
\begin{tikzpicture}
	\draw[line width=3pt] (0,0) .. controls(1,3).. (4,0) ..controls(5,1)and(4,3).. cycle;
	\draw[color=gray] (0,0)-- (1,3) -- (4,0) -- (5,1) -- (4,3) -- cycle;
\end{tikzpicture}
\end{document}
```

# 14.4 Rectangle操作

一个矩形显然可以用四条直线和一个`cycle`指令创建。然而，由于经常需要矩形，因此对于矩形有特殊的语法。以下是一个简单的例子

```latex
\begin{tikzpicture}
	\draw (0,0) rectangle (1,1);
\end{tikzpicture}
```
对应结果如下所示: 

```tikz
\usepackage{tikz}
\usetikzlibrary{scopes}

\begin{document}
\begin{tikzpicture}
	\draw (0,0) rectangle (1,1);
\end{tikzpicture}
\end{document}
```

以下是一个稍微复杂一些的例子
```latex
\begin{tikzpicture}
	\draw (0,0) rectangle (1,1);
	\draw (.5,1) rectangle (2,0.5) (3,0) rectangle (3.5,1.5) -- (2,0);
\end{tikzpicture}
```
对应结果如下所示:
```tikz
\usepackage{tikz}
\usetikzlibrary{scopes}

\begin{document}
\begin{tikzpicture}
	\draw (0,0) rectangle (1,1);
	\draw (.5,1) rectangle (2,0.5) (3,0) rectangle (3.5,1.5) -- (2,0);
\end{tikzpicture}
\end{document}
```
