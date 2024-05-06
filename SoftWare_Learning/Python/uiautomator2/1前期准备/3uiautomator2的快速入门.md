# 一段简单的链接代码

```python
import uiautomator2 as u2

# 链接手机
device = u2.connect();

#打开被测试的app
if(device):
    print("1\n")
    print(device)
    device(text='阴阳师').click()
else:
    print ("0")
```

这是一段简单的连接手机并打开被测试软件的代码


其中对于`device(text='阴阳师').click()`的解释如下
[[9什么是元素定位#^292d2b]]

