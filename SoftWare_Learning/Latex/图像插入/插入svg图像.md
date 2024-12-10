
>[!tips] 声明
>本笔记转载自 https://blog.csdn.net/qq_37085158/article/details/128875888

## 步骤

1. 使用浏览器将图像另存为 pdf 格式
2. 使用 pdfcrop 工具剪裁 pdf 文件
3. 导入裁剪后的 pdf 图像

## 具体步骤

### Step 1. 另存为 PDF

1. ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20241004233257.png)
2. 注意！记得取消勾选“页眉和页脚”
	1. ![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20241004233328.png)

### Step 2. 使用 `pdfcrop` 工具一键裁剪图片

这个工具是只要安装了 TeXLive 就有的

输入以下命令即可：

```bash
C:\Users\Administrator\Desktop> pdfcrop gather.pdf
PDFCROP 1.40, 2020/06/06 - Copyright (c) 2002-2020 by Heiko Oberdiek, Oberdiek Package Support Group.
==> 1 page written on `gather-crop.pdf'.
```

这里，原始文件为 `gather.pdf`，裁剪好的文件被保存为 `gather-crop.pdf`
