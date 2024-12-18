# 14.9 抛物线绘制

在TikZ中，使用`parabola`操作可以绘制抛物线。

parabola操作的语法如下：

```latex
\draw (x1,y1) parabola [bend (x3,y3)] (x2,y2);
```

其中，`(x1,y1)`是抛物线的起点，`(x2,y2)`是抛物线的终点。抛物线的顶点由`bend (x3, y3)`确定。

下面是一个简单的例子，演示如何使用parabola操作绘制抛物线：
```latex
\begin{tikzpicture}
\draw[->] (-2,0) -- (2,0) node[right] {$x$};
\draw[->] (0,-1) -- (0,4) node[above] {$y$};
\draw[blue] (-1.5,1) parabola bend(0,0) (1.5,1);
\end{tikzpicture}
```



```tikz
\usepackage{tikz}

\begin{document}
\begin{tikzpicture}
\draw[->] (-2,0) -- (2,0) node[right] {$x$};
\draw[->] (0,-1) -- (0,4) node[above] {$y$};
\draw[blue] (-1.5,1) parabola bend(0,0) (1.5,1);
\end{tikzpicture}
\end{document}
```

总之，parabola操作是TikZ中绘制抛物线的重要操作之一，可以通过调整起点、顶点和控制点的位置来实现不同形状的抛物线。

# 14.10 sin与cos

用于绘制`sin`与`cos`的函数图像, 可以用plot代替,

# 14.11 svg操作

# 14.12 plot操作

第22章详解