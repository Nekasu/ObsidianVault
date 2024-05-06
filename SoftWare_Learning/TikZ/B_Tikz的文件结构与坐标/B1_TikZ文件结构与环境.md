# Latex的组织架构

```LateX
% 导言区
\usepackage{tikz}
\documentclass{article}
%...

% 正文区
\begin{document}
\end{document}
```

# TikZ包及其扩展包的导入

```LateX
% This will automatically load the pgf and the pgffor package.
\usepackage{tikz}
% Once TikZ has been loaded, you can use this command to load further libraries.
\usetikzlibrary{<list of libraries>}

\begin{document}
	% TikZ代码
\end{document}
```

首先需要使用`\usepackage{tikz}`命令导入tikz包

在成功导入tikz包后, 可以使用`\usetikzlibrary{}`命令导入额外的包, 大括号里的内容为包名, 注意:
1. 当导入多个 包时, 可以使用逗号隔开
2. 第二次导入一个相同的包时, 不会发生任何事
以下是一个例子
```Latex
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
```
The above command will load a whole bunch of extra arrow tip definitions. 

What this command does is to load the file `tikzlibrary〈library〉.code.tex` for each 〈library〉 in the 〈list of libraries〉. 
- 如使用了`\usetikzlibrary{arrows.meta}`, 则会加载`tikzlibrary.arrows.meta.code.tex`文件

If this file does not exist, the file `pgflibrary〈library〉.code.tex` is loaded instead. 

If this file also does not exist, an error message is printed. 

Thus, to write your own library file, all you need to do is to place a file of the appropriate name somewhere where TEX can find it. LATEX, plain TEX, and ConTEXt users can then use your library.

# TikZ图的最外层环境--tikzpicture

如何在LateX正文中绘制TikZ图? 代码如下所示
```latex
\usepackage{tikz}
\begin{document}

	\begin{tikzpicture}<animations spec>[<options>]
		% TikZ绘图代码
	\end{tikzpicture}

\end{document}
```

除了`\tikzset`以外的tikz命令, 必须全部写在`tikzpicture`环境中
> All TikZ commands should be given inside this environment, except for the \tikzset command.

`<aimiations spec>`在后期会讲, 在官方文档的第26章详细讲解
> Before the options you can specify animation commands, provided that the animations library is loaded, see Section 26 for details.


`<options>`在后期会讲, 在官方文档的12.4节详细讲解
> When this environment is encountered, the 〈options〉 are parsed, see Section 12.4. All options given here will apply to the whole picture.

# Scope环境

## Scope环境基础

可以在[[B1_TikZ文件结构与环境#TikZ图的最外层环境--tikzpicture|`tikzpicture`]]环境中添加`scope`环境, 如下所示
```LateX
\begin{scope}<animations spec>[options]
	<environment contents>
\end{scope}
```
>Inside a `{tikzpicture}` environment you can create scopes using the `{scope}` environment. This environment is available only inside the `{tikzpicture}` environment, so once more, there is little chance of doing anything wrong.


以下是一个演示实例
```Latex
\usepackage{tikz}
% \usetikzlibrary{...}

\begin{document}
	\begin{tikzpicture}[ultra thick]
		\begin{scope}[red]
			\draw (0mm, 10mm) -- (10mm, 10mm);
			\draw (0mm, 8mm) -- (10mm, 8mm);
		\end{scope}	

		\draw (0mm, 6mm)-- (10mm, 6mm);
	
		\begin{scope}[green]
			\draw (0mm, 4mm) -- (10mm, 4mm);
			\draw (0mm, 2mm) -- (10mm, 2mm);
			\draw[blue] (0mm, 0mm) -- (10mm, 0mm);
		\end{scope}	
	\end{tikzpicture}
\end{document}
```
这段代码对应的图像如下: 
```tikz
\usepackage{tikz}
% \usetikzlibrary{...}

\begin{document}
	\begin{tikzpicture}[ultra thick]
		\begin{scope}[red]
			\draw (0mm, 10mm) -- (10mm, 10mm);
			\draw (0mm, 8mm) -- (10mm, 8mm);
		\end{scope}	

		\draw (0mm, 6mm)-- (10mm, 6mm);
	
		\begin{scope}[green]
			\draw (0mm, 4mm) -- (10mm, 4mm);
			\draw (0mm, 2mm) -- (10mm, 2mm);
			\draw[blue] (0mm, 0mm) -- (10mm, 0mm);
		\end{scope}	
	\end{tikzpicture}
\end{document}
```


## Scope环境的简写

在调用`scops`的tikzlibrary后, 可以直接用大括号代替`\begin{scope}`与`\end{scope}`的命令, 如下

```Latex
\usepackage{tikz}
\usetikzlibrary{scopes}

\begin{document}

	\begin{tikzpicture}
		% 由于使用了\usetikzlibrary{scopes}语句, 所以可以使用"{}"来代替"\begin{scope}", "\end{scope}"
		{[red, ultra thick]
			\draw (0mm, 0mm) -- (-10mm, -10mm);
			\draw (0mm, 0mm) -- (10mm, 10mm);
		}
		{[blue, ultra thick]
			\draw (0mm, 0mm) -- (10mm, -10mm);
			\draw (0mm, 0mm) -- (-10mm, 10mm);
		}
	\end{tikzpicture}

\end{document}
```
图像如下所示

```tikz
\usepackage{tikz}
\usetikzlibrary{scopes}

\begin{document}

	\begin{tikzpicture}
		{[red, ultra thick]
			\draw (0mm, 0mm) -- (-10mm, -10mm);
			\draw (0mm, 0mm) -- (10mm, 10mm);
		}
		{[blue, ultra thick]
			\draw (0mm, 0mm) -- (10mm, -10mm);
			\draw (0mm, 0mm) -- (-10mm, 10mm);
		}
	\end{tikzpicture}

\end{document}
```
