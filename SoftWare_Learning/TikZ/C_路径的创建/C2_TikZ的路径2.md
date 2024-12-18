# 14.5 圆角与锐角操作

## 圆角操作

### 针对整个路径的圆角操作

圆角操作可以使所有line-to操作(--)或curve-to操作(..controls..)造成的角变得较为平滑, 以下是一个简单的实例

```latex
\begin{tikzpicture}
	\draw[rounded corners] (0,0) -- (1,1) -- (0,2);
\end{tikzpicture}
```

```tikz
\usepackage{tikz}
\usetikzlibrary{scopes}

\begin{document}
\begin{tikzpicture}
	\draw[rounded corners] (0,0) -- (1,1) -- (0,2);
\end{tikzpicture}
\end{document}
```

以下是一个较为复杂的实例
```latex
\begin{tikzpicture}
	\draw[rounded corners=10pt] (0,0) -- (1,1) -- (0,2);
\end{tikzpicture}
```

```tikz
\usepackage{tikz}
\usetikzlibrary{scopes}

\begin{document}
\begin{tikzpicture}
	\draw[rounded corners=10pt] (0,0) -- (1,1) -- (0,2);
\end{tikzpicture}
\end{document}

```

与上个例子相比, 这个例子的操作多加了`=10pt`语句, 这个语句可以控制圆角的曲率半径, 如下所示

### 针对单个角的圆角操作

除了对一个`\draw`命令进行圆角操作, 我们也可以<mark style="background: #CACFD9A6;">对单个角以及以后的角</mark>进行圆角操作, 如下例所示:
```latex
\begin{tikzpicture}
	\draw (0,0) -- (1,1)[rounded corners] -- (3,1) -- (3,0) -- cycle;
\end{tikzpicture}
```

```tikz
\usepackage{tikz}
\usetikzlibrary{scopes}

\begin{document}
\begin{tikzpicture}
	\draw (0,0) -- (1,1)[rounded corners] -- (3,1) -- (3,0) -- cycle;
\end{tikzpicture}
\end{document}
```
该例子中, 我们在角`(1,1)`后使用了`[rounded corners]`命令, 这使得`(1,1)`后面的角, 包括角(3,1)(3,0)与cycle, 变成了圆角

如果想针对单个角设置`[rounded corners]`, 可以参考以下例子
```latex
\begin{tikzpicture}
	\draw (0,0) [rounded corners]--  (1,1) [sharp corners]-- (2,0) -- (3,1);
\end{tikzpicture}
```
```tikz
\usepackage{tikz}
\usetikzlibrary{scopes}

\begin{document}
\begin{tikzpicture}
	\draw (0,0) [rounded corners]--  (1,1) [sharp corners]-- (2,0) -- (3,1);
\end{tikzpicture}
\end{document}
```

## 锐角操作

与圆角操作类似, 皆是对后面所有的角设置的, 如下例所示
```latex
\usepackage{tikz}
\usetikzlibrary{scopes}

\begin{document}
\begin{tikzpicture}
	\draw (0,0) [rounded corners]--  (1,1) [sharp corners]-- (2,0) -- (3,1);
\end{tikzpicture}
\end{document}
```

```tikz
\usepackage{tikz}
\usetikzlibrary{scopes}

\begin{document}
\begin{tikzpicture}
	\draw (0,0) [rounded corners]--  (1,1) [sharp corners]-- (2,0) -- (3,1);
\end{tikzpicture}
\end{document}
```

# 14.6 圆与椭圆

## 指令与可选项

可以用`circle`指令绘制圆与椭圆, 其代码如下所示
> \<坐标\> circle\[\<可选项\>]  

该命令用于在`<坐标>`处生成一个圆, 有以下`可选项`
1. x radius=\<value\>或rx=\<value\>
	- 设置椭圆的长轴, 长轴的值为`value`
2. y radius=\<value\>或ry=\<value\>
	- 设置椭圆的短轴, 短轴的值为`value`
3. radius=\<value\>或r=\<value\>
	- 同时这只椭圆的长轴与短轴, 也即设置圆的半径
4. at=\<coordinate\>
	- 设置圆心所在, 如果显式申明了该变量, 则不会使用`circle`指令前的坐标作为圆心
5. rotate=\<angle\>
	- 用于设置椭圆的角度

##  绘制单个圆/椭圆

以下是一个画出圆的例子
```latex
\begin{tikzpicture}
	%一个在(0,0)处半径为1cm的圆
	\draw (0,0) circle[radius=1cm];
	%一个在(3,0)处, 长轴为1cm, 短轴为0.5cm的椭圆
	\draw (3,0) circle[x radius=1cm, y radius=0.5cm];
	%一个在(5,0)处, 长轴为1cm, 短轴为0.5cm, 旋转了30度的椭圆
	\draw (5,0) circle[x radius=1cm, y radius=0.5cm, rotate=30];
\end{tikzpicture}
```
```tikz
\usepackage{tikz}
\usetikzlibrary{scopes}

\begin{document}
\begin{tikzpicture}
	%一个在(0,0)处半径为1cm的圆
	\draw (0,0) circle[radius=1cm];
	%一个在(3,0)处, 长轴为1cm, 短轴为0.5cm的椭圆
	\draw (3,0) circle[x radius=1cm, y radius=0.5cm];
	%一个在(5,0)处, 长轴为1cm, 短轴为0.5cm, 旋转了30度的椭圆
	\draw (5,0) circle[x radius=1cm, y radius=0.5cm, rotate=30];
\end{tikzpicture}
\end{document}
```


## 在路径中使用圆/椭圆

可以在路径中使用圆与椭圆, 如下例所示:
```latex
\begin{tikzpicture}[radius=2pt]
	\draw (0,0) circle -- (1,1) circle -- ++(0,1) circle;
\end{tikzpicture}
```
```tikz
\usepackage{tikz}
\usetikzlibrary{scopes}

\begin{document}
\begin{tikzpicture}[radius=2pt]
	\draw (0,0) circle -- (1,1) circle -- ++(0,1) circle;
\end{tikzpicture}
\end{document}
```

代码中, 的`(0,0) circle`表示在坐标`(0,0)`上绘制一个`circle`, 这与[[C2_TikZ的路径2#14.5 圆角与锐角操作|圆角与锐角操作]]对后面所有的点生效是不一样的

代码中, `(1,1)-- ++(1,0)`表示从`(1,1)`处往上画一个单位的线段

# 14.7 绘制圆弧与椭圆弧


## 圆弧

`tikz` 的 `arc` 操作用于绘制弧线。其基本语法为：

```latex
%绘制圆弧
\draw (x,y) arc [start angle=<degrees>, end angle=<degrees>, radius=<values>, delta angle=<degrees> ];
%或
\draw (x,y) arc(start angle:end angle: radius);
```

其中 `(x,y)` 为圆弧的圆心坐标，`start angle` 为起始角度，`end angle` 为终止角度，`radius` 为圆弧的半径, `delta angle`为角度的增量。
`start angle` 和 `end angle` 的单位为度数，以三点钟方向为 0 度，逆时针方向为正。如果要顺时针绘制弧线，需要使用负的角度值。

下面是一个简单的例子，绘制一个以原点为圆心，半径为 1 的圆弧，起始角度为 30 度，终止角度为 120 度：

```latex
\begin{tikzpicture}
  \draw (0,0) arc [start angle=30, end angle=120, radius=1];
\end{tikzpicture}
```

绘制结果如下：

```tikz
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}

    \draw (0,0) arc[start angle=30, end angle=120,radius=1, ];

\end{tikzpicture}

\end{document}
```

除了绘制圆弧，`arc` 操作还可以绘制扇形。只需要在绘制圆弧的基础上，将起始点和终止点之间的线段与圆心相连，就可以得到一个扇形。下面是一个例子，绘制一个以原点为圆心，半径为 1 的扇形，起始角度为 30 度，终止角度为 120 度：

```latex
\begin{tikzpicture}
  \fill[gray!50] (0,0) -- (30:1) arc (30:120:1) -- cycle;
  \draw (0,0) -- (30:1) arc (30:120:1) -- cycle;
\end{tikzpicture}
```

绘制结果如下：
```tikz
\begin{document}
\begin{tikzpicture}
  \fill[color=gray] (0,0) -- (30:1) arc (30:120:1) -- cycle;
  \draw (0,0) -- (30:1) arc (30:120:1) -- cycle;
\end{tikzpicture}
\end{document}
```

在绘制扇形时，我们使用 `fill` 命令填充扇形内部，使用 `draw` 命令绘制扇形的边缘。

## 椭圆弧

`arc`指令也可以绘制椭圆弧, 其基本语法为:

```latex
%绘制椭圆弧
\draw (x,y) arc [start angle=<degrees>, end angle=<degrees>, x radius=<values>, y radius = <values>, delta angle=<degrees> ];
```
与[[C2_TikZ的路径2#圆弧|绘制圆弧]]的基本语法相比, 其区别仅仅在于将绘制圆弧中的`radius`可选项变为了`x radius`与`y radius`可选项, 以下是一个例子:
```latex
\begin{tikzpicture}
	\draw (0,0) arc[start angle=30, end angle=120, x radius=1, y radius=2];
\end{tikzpicture}
```

```tikz
\begin{document}
\begin{tikzpicture}
	\draw (0,0) arc[start angle=30, end angle=120, x radius=1, y radius=2];
\end{tikzpicture}
\end{document}
```

# 14.8 网格绘制

`tikz` 的 `grid` 操作用于绘制弧线。其基本语法为：

```latex
(x1,y1) grid[<options>] (x2,y2)
```
其中, 可选项可以为
1. step=\<number or dimension or coordinate\>
	- 用于设置网格的步长
	- 如果给定了number, 如数字2, 绘制时x方向与y方向的步长都会为默认值的两倍
	- 如果给定了dimension, 如单位2cm, 则绘制时x方向与y方向的步长都会为2cm
	- 如果给定了一个coordinate, 则x方向的步长为给定坐标的x, y方向的步长为给定的y值
1. xstep=\<number or dimension\>
	- 用于设定网格x方向上的步长
	- 如果给定了number, 如数字2, 绘制时x方向为默认值的两倍
	- 如果给定了dimension, 如单位2cm, 则绘制时x为2cm
	- 如果仅给出了xstep而未给出ystep, 或此时ystep的数值为非正数, 则不会绘制y方向上的线条
1. ystep= \<number or dimension\>
	- 用于设定网格y方向上的步长
	- 如果给定了number, 如数字2, 绘制时y方向为默认值的两倍
	- 如果给定了dimension, 如单位2cm, 则绘制时y方向为2cm
	- 如果仅给出了ystep而未给出xstep, 或此时xstep的数值为非正数, 则不会绘制x方向上的线条

以下是一些例子
```latex
\begin{tikzpicture}
	%一个最简单的grid命令
	\draw (0,0) grid (3,2);
	%使用了step可选项的grid_1
	\draw[red!50] (0,0) grid[step=2cm](4,4);
	\draw[purple] (3,2) circle[radius=2cm];
	%使用了step可选项的grid_2
	\draw (5,0) grid[step=1] (6,3);
	%使用了step可选项的grid_3
	\draw[blue] (5,0) grid[step=(45:1)] (8,3);
	%仅给出xstep的grid命令
	\draw[ultra thick] (0,0) grid[xstep=2, ystep=0](4,4);
	\end{tikzpicture}
```
```tikz
\begin{document}
\begin{tikzpicture}
	%一个最简单的grid命令
	\draw (0,0) grid (3,2);
	%使用了step可选项的grid_1
	\draw[red!50] (0,0) grid[step=2cm](4,4);
	\draw[purple] (3,2) circle[radius=2cm];
	%使用了step可选项的grid_2
	\draw (5,0) grid[step=1] (6,3);
	%使用了step可选项的grid_3
	\draw[blue] (5,0) grid[step=(45:1)] (8,3);
	%仅给出xstep的grid命令
	\draw[ultra thick] (0,0) grid[xstep=2, ystep=0](4,4);
	\end{tikzpicture}
\end{document}
```