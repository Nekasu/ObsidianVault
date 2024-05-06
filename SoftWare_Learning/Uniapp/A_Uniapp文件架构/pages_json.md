本文旨在记录pages.josn文件中的各个组成, 可查看官方文档

[pages.json 页面路由](https://uniapp.dcloud.net.cn/collocation/pages.html)

- pages文件由一个大括号包围, 由一个个嵌套的键值对组成
	- ![[Pasted image 20231206225454.png]]


# "pages"键与对应的值

- 下图是一个“pages”键值对的例子
	- ![[Pasted image 20231206225706.png]]
- 名为`pages`的键对应的值为一个用`[]`表示的列表
	- 列表中的元素是一个个字典, 每个字典表示一个页面


# “globalStyle”键

- 下图是一个“gloabalStyle”键的例子
	- ![[Pasted image 20231206225902.png]]
- 表示全局的样式


# “tabBar”键

- 下图是一个`tabBar`键的例子
	- ![[Pasted image 20231206230229.png|222]]
	- 其中包含一个`[]`列表, 该列表以字典为元素
	- 列表中每个元素表示导航栏中的一个图标, 如下所示
	- ![[Pasted image 20231206230210.png|130]]