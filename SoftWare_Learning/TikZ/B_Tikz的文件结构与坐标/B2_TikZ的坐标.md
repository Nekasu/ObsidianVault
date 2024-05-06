# 总览
本章为官方文档的13.1-13.2节
## 坐标的定义

坐标用于指定画布上的某个位置, 可以使用不同的坐标系进行坐标的定位, 如`直角坐标系`, `极坐标系`, `球坐标系`等. 无论使用什么坐标系, 坐标都表示画布上特定的某个点

简单来说, 在TikZ中, 使用表示坐标的语句如下: ^21dec2
```latex
[<options>]<coordinate specification>
%[<可选项>]<坐标>
```
`[<options>]`表示一些可选项, 一般用中括号括起来
`<coordinate specifivation>`表示一个坐标, 一般用小括号(圆括号)括起来

## 两种申明坐标系的方式

### 显示申明

如果想显式地指定一个坐标, 我们可以这样做: 
```Latex
(<coordinate system> cs:<list of key–value pairs specific to the coordinate system>)
```

^131d75

这个语句是[[B2_TikZ的坐标#^21dec2|上面说的"简单语句"]]的扩展, "cs:"后面的部分即为原来的语句
该语句用于进行坐标的申明, 注意两侧的小括号

其中, 两侧的小括号表示这是一个坐标

`<coordinate system>`表示坐标系统, 可以为`canvas`, `xyz`,`canvas polor`, `xyz polor`, `xy`, `barycentric` 等, 在[[B2_TikZ的坐标#TikZ的一般坐标系]]以及以后的章节中会讲到

`cs:`是一个固定字符, 表示"coordinate system"

`<list of key–value pairs specific to the coordinate system>`表示坐标的申明, 以下是一个例子

```Latex
\usepackage{tikz}
%\usetikzlibrary{a,b,c}

\begin{document}

	\begin{tikzpicture} 
		\draw[help lines](0,0) grid (3,2); 
		\draw (canvas cs:x=0cm,y=2mm) --(canvas polar cs:radius=2cm,angle=30) ; 
	\end{tikzpicture}

\end{document}
```

### 隐式申明

当需要给定大量的坐标时，显式规范往往过于冗长。正因为如此，对于你可能使用的坐标系，往往会提供一种特殊的语法。当使用特殊语法指定的坐标时，TikZ会注意到并自动选择正确的坐标系。

# TikZ的一般坐标系

## Canvas坐标系

Canvas Polar坐标系统使用屏幕坐标系作为参考，并以指定的极坐标为基准进行定位。
在Canvas Polar坐标系统中，角度（极角）的起始方向是水平向右的正方向，角度的增加方向是逆时针方向。这意味着，角度为0度时，极坐标位于水平向右的位置。
Canvas Polar坐标系<mark style="background: #FFB8EBA6;">不考虑当前的变换（旋转、缩放等）</mark>，因此在进行变换操作后，绘制的图形位置不会发生变化。

### Canvas坐标系的使用

#### 显式申明

基于[[B2_TikZ的坐标#^131d75|坐标显式表示的一般公式]], 可以得出canvas坐标系的显式表示如下:
```latex
(canvas cs: x=x1, y=y1)
```

基于上述代码, 可以得出显式使用canvas坐标系的方式如下例所示
```latex
\usepackage{tikz}
\usetikzlibrary{scopes}

\begin{document}

	\begin{tikzpicture}
		%\draw (canvas cs: x= x_1,y= y_1) -- (canvas cs: x= x_2,y= y_2);
		\draw [help lines] grid (3,2);
		\draw (canvas cs: x=0cm, y=0cm) -- (canvas cs: x=1cm, y=2cm); 
	\end{tikzpicture}

\end{document}

```

```tikz
\usepackage{tikz}
\usetikzlibrary{scopes}

\begin{document}

	\begin{tikzpicture}
		%\draw (canvas cs: x= x_1,y= y_1) -- (canvas cs: x= x_2,y= y_2);
		\draw [help lines] grid (3,2);
		\draw (canvas cs: x=0cm, y=0cm) -- (canvas cs: x=1cm, y=2cm); 
	\end{tikzpicture}

\end{document}

```

#### 隐式申明

canvas坐标系的隐式申明如下所示:
```Latex
(x1, y1)
```

基于上述代码, 可以得出隐式使用canvas坐标系的方式如下例所示:
```latex
\usepackage{tikz}

\begin{document}

	\begin{tikzpicture}
		\draw[help lines] grid (3,2);
		%\draw (x1,y1)--(x2,y2);
		\draw (0,0)--(1,2);
	\end{tikzpicture}

\end{document}
```
```tikz
\usepackage{tikz}

\begin{document}

	\begin{tikzpicture}
		\draw[help lines] grid (3,2);
		\draw (0,0)--(1,2);
	\end{tikzpicture}

\end{document}
```


### 加不加单位的区别

#### 显式表示时会有区别

- 加单位的写法为:`\draw (canvas cs: x=0cm, y=0cm) -- (canvas cs: x=2cm, y=2cm);`
	- 为了美观, 我将10cm写成了2cm, 否则会太大, 如下所示
```tikz
\usepackage{tikz}
%\usetikzlibrary{a,b,c}

\begin{document}
	\begin{tikzpicture}
		\draw[help lines] (0,0) grid (3,2);
		\draw (canvas cs: x=0cm, y=0cm) -- (canvas cs: x=2cm, y=2cm);%区别所在
	\end{tikzpicture}	
\end{document}

```
- 不加单位的写法为: `\draw (canvas cs: x=0, y=0) -- (canvas cs: x=10, y=10);`, 如下所示:
```tikz
\usepackage{tikz}
%\usetikzlibrary{a,b,c}

\begin{document}
	\begin{tikzpicture}
		\draw[help lines] (0,0) grid (3,2);
		\draw (canvas cs: x=0, y=0) -- (canvas cs: x=10, y=10);%区别所在
	\end{tikzpicture}	
\end{document}
```

这两张图片的代码仅仅在`\draw`命令上有区别, 这说明在显式表示时
- 如果使用单位, 即会按照单位来计算
- 如果没有使用单位, 会按像素点的个数来计算

#### 隐式表示时没有区别

- 加单位的写法为:`\draw (x=0cm, y=0cm) -- (x=2cm, y=2cm);`, 结果如下所示:
```tikz
\usepackage{tikz}

\begin{document}

	\begin{tikzpicture}
		\draw[help lines] grid (3,2);
		\draw (0,0)--(1cm,2cm);
	\end{tikzpicture}

\end{document}
```
- 不加单位的写法为:`\draw (x=0, y=0) -- (x=2, y=2);`, 结果如下所示:
```tikz
\usepackage{tikz}

\begin{document}

	\begin{tikzpicture}
		\draw[help lines] grid (3,2);
		\draw (0,0)--(1,2);
	\end{tikzpicture}

\end{document}
```

这两张图片的代码仅仅在`\draw`命令上有区别, 这说明在隐式表示时, 是否使用单位对绘制的图片没有影响


## xyz坐标系

官方文档13.2.1(p137)中的内容, 是三维的坐标系, 以后用到的时候再学

## canvas polor-极坐标系

官方文档13.2.1(p138)中的内容, 是二维的极坐标系, 以后用到的时候再学

## xyz polor-三维极坐标系

官方文档13.2.1(p138)中的内容, 是三维的极坐标系, 以后用到的时候再学

## xy polor-极坐标系

XY Polar坐标系统使用当前的坐标变换（如旋转、缩放等）作为参考，并以指定的极坐标为基准进行定位。在XY Polar坐标系统中，角度（极角）的起始方向和增加方向由当前的坐标变换决定。如果进行了坐标变换，XY Polar坐标系<mark style="background: #FFB8EBA6;">会考虑这些变换</mark>，并相对于变换后的坐标系进行定位。


### xy-polor与canvas-polor的区别

在TikZ中，Canvas Polar（`canvas polar`）和 XY Polar（`xy polar`）是两种不同的极坐标系统，用于在绘图中描述和定位极坐标。

- 不同点：
  - Canvas Polar基于屏幕坐标系，XY Polar基于当前的坐标变换。
  - Canvas Polar不受坐标变换的影响，绘制的图形位置在变换后保持不变；XY Polar考虑了当前的坐标变换，绘制的图形位置会随着变换而变化。
  
- 相同点：
  - 两者都是极坐标系统，用于描述和定位极坐标。
  - 两者都使用极径和极角来表示点的位置。

在使用TikZ绘图时，可以根据需要选择使用Canvas Polar或XY Polar坐标系统，以实现所需的极坐标绘制效果。

# TikZ的重心(Barycentric)坐标系

官方文档13.2.2(p139)中的内容, 通过给定一些参数, 并在中心公式的协助下完成坐标定位

# TikZ的节点(Node)坐标系

官方文档13.2.3(p140)中的内容,通过定位Node并在Node的上下左右处进行操作的定位方式

## 节点坐标系的GPT解释

在TikZ中，节点坐标系（node coordinate system）是用于定位和操作节点的一种坐标系统。每个节点在TikZ中都有一个独特的名称，可以通过该名称引用和操作节点。

节点坐标系相对于节点本身进行定义和使用，其中节点的锚点（anchor）作为参考点。每个节点都有一个主要锚点，默认情况下是中心锚点。除了中心锚点外，每个节点还可以有其他的锚点，例如边界上的角点、顶点等。

通过节点坐标系，可以使用以下方法来操作节点：

1. 定位节点：可以使用节点名称和节点坐标系来定位和放置节点在画布上的位置。例如，`(A.north)` 表示节点 `A` 的上边界的点。

2. 连接节点：可以使用节点名称和节点坐标系来连接节点之间的线段或曲线。例如，`\draw (A.north) -- (B.south);` 表示从节点 `A` 的上边界到节点 `B` 的下边界绘制一条直线。

3. 标记节点：可以在节点的指定位置上添加标签或其他装饰物。例如，`\node at (A.north) {$\circ$};` 在节点 `A` 的上边界上添加一个圆圈标记。

节点坐标系允许对节点进行相对定位和操作，而不受节点的形状或大小的限制。这为在TikZ中创建复杂的图形和图形布局提供了便利性和灵活性。


# 切线(Tangent)坐标系

官方文档13.2.4(p142)中的内容, 用于绘制某个图形的切线

## 切线坐标系的GPT解释

在TikZ中，切线坐标系（tangent coordinate system）是一种相对于路径或曲线的切线方向进行定位的坐标系统。它允许你在路径上的特定点处定义和操作坐标。

切线坐标系使用路径的切线方向作为参考方向，并将切线方向定义为正 x 轴方向。因此，切线坐标系的 x 轴与切线方向相对应，y 轴垂直于切线方向。

通过切线坐标系，可以使用以下方法来操作路径上的点：

1. 定位点：可以使用路径上的特定点和切线坐标系来定位和放置该点在画布上的位置。例如，`(tangent cs:node=A,point={(A)},solution=2)` 表示路径上与节点 `A` 相切的第二个点。

2. 连接点：可以使用路径上的特定点和切线坐标系来连接路径上的点之间的线段或曲线。例如，`\draw (tangent cs:node=A,point={(A)},solution=1) -- (tangent cs:node=B,point={(B)},solution=2);` 表示从与节点 `A` 相切的第一个点到与节点 `B` 相切的第二个点之间绘制一条直线。

3. 标记点：可以在路径的特定点上添加标签或其他装饰物。例如，`\node at (tangent cs:node=A,point={(A)},solution=1) {$\circ$};` 在与节点 `A` 相切的第一个点上添加一个圆圈标记。

切线坐标系允许你相对于路径的切线方向进行定位和操作，从而实现在TikZ中绘制和处理与路径相关的图形和效果。它特别适用于绘制曲线、路径上的点和曲线上的标记等场景。

# 自定义坐标系