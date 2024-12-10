`.bib` 文件是 BibTeX 用来管理文献引用的文件格式。它是纯文本文件，包含一个或多个 BibTeX 条目，每个条目描述一篇文献（例如书籍、文章、论文等）的详细信息。下面详细介绍 `.bib` 文件的结构和用法。

### `.bib` 文件结构

每个 BibTeX 条目都以一个条目类型（如 `@article`, `@book` 等）开始，后跟一个唯一的引用键（key）和一组字段，每个字段包含特定的信息。字段的值通常用大括号 `{}` 或双引号 `""` 括起来。

### 示例 `.bib` 文件

以下是一个包含多种类型条目的示例 `.bib` 文件：
```bibtex
@article{smith2023deep,
  author = {John Smith and Jane Doe},
  title = {Deep Learning Approaches for Computer Vision},
  journal = {Journal of Computer Vision},
  year = {2023},
  volume = {42},
  number = {3},
  pages = {123-134},
  month = {Mar},
  doi = {10.1234/jcv.2023.12345}
}

@book{doe2021ai,
  author = {Jane Doe},
  title = {Artificial Intelligence: Foundations and Trends},
  publisher = {Tech Books Publishing},
  year = {2021},
  edition = {2nd},
  isbn = {978-3-16-148410-0}
}

@inproceedings{lee2022cv,
  author = {Michael Lee and Alice Kim},
  title = {Computer Vision in Autonomous Vehicles},
  booktitle = {Proceedings of the International Conference on Robotics and Automation},
  year = {2022},
  pages = {456-467},
  publisher = {IEEE},
  doi = {10.1109/ICRA.2022.123456}
}

@misc{johnson2020arxiv,
  author = {Emily Johnson},
  title = {An Overview of Machine Learning Techniques},
  howpublished = {arXiv preprint arXiv:2001.12345},
  year = {2020}
}
```

#### 常见条目类型

1. **`@article`**：用于期刊文章
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

2. **`@book`**：用于书籍
   ```bibtex
   @book{key,
     author = {Author Name},
     title = {Title of the Book},
     publisher = {Publisher Name},
     year = {2023},
     volume = {1},
     series = {Series Name},
     address = {Publisher Address},
     edition = {2nd},
     month = {Jan},
     note = {Some note},
     isbn = {123-456-789}
   }
   ```

3. **`@inproceedings`**：用于会议论文集中的文章
   ```bibtex
   @inproceedings{key,
     author = {Author Name},
     title = {Title of the Paper},
     booktitle = {Title of the Proceedings},
     year = {2023},
     editor = {Editor Name},
     volume = {1},
     series = {Series Name},
     pages = {1-10},
     address = {Conference Address},
     month = {Jan},
     organization = {Organization Name},
     publisher = {Publisher Name},
     note = {Some note},
     doi = {10.1234/example.doi}
   }
   ```

4. **`@misc`**：用于无法归类到其他类型的文献
   ```bibtex
   @misc{key,
     author = {Author Name},
     title = {Title of the Work},
     howpublished = {How it was published},
     year = {2023},
     month = {Jan},
     note = {Some note}
   }
   ```

#### 字段说明

- **`author`**：作者姓名
- **`title`**：标题
- **`journal`**：期刊名称
- **`year`**：出版年份
- **`volume`**：卷号
- **`number`**：期号
- **`pages`**：页码范围
- **`month`**：出版月份
- **`note`**：附注
- **`doi`**：数字对象标识符
- **`publisher`**：出版社
- **`address`**：出版地
- **`edition`**：版次
- **`isbn`**：国际标准书号
- **`booktitle`**：会议论文集名称
- **`editor`**：编辑
- **`series`**：系列名称
- **`organization`**：组织名称
- **`howpublished`**：出版方式


## bib 文件的创建

以下两种创建方式二选一即可

### 手动创建

可以通过[谷歌学术](https://scholar.google.com/)获取 bib 文件中的参考文献条目, 流程如下所示：

![](https://raw.githubusercontent.com/Nekasu/Blog_pics/main/20240628224839.png)

### 通过 Zotero 创建

也可以通过 Zotero 文献管理软件与其插件, 实现对自己 Zotero 中所有文献 bib 文件的直接导出, 请见 [Zotero中文社区-直接生成参考文献](https://zotero-chinese.com/user-guide/create-bibliographies-within-zotero) 