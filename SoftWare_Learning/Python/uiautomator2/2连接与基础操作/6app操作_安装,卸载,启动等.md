本文中所有代码均有以下前置代码

```python
import uiautomator2 as u2
device = u2.connect()
```

# 安装

```python
device = u2.connect()
device.app_install(url)
#url是需要下载的软件的apk的地址
```

以下是如何复制apk的链接的一个方法

![[Pasted image 20230401181631.png|复制apk的下载地址]]

以下是一个下载夸克浏览器的例子

```python
import uiautomator2 as u2

device = u2.connect('127.0.0.1:62001')

url = 'https://umcdn.uc.cn/download/36734/quark/kk@other_zcwkaic409/QuarkBrowser_V6.2.5.247_android_pf3300_(zh-cn)_release_(Build230331123444-arm32).apk'

if(device):
    print("yes")
    device.app_install(url)
    print("success")
else:
    print("sorry")
```

# 打开并关闭app

打开app

```python
device(text="阴阳师").click() #在首页点击
device.app_start('包名') #利用包名打开软件 
```


关闭app

```python
device.app_stop('包名')#利用包名关闭app
```

# 获取app的包名

## 1. 利用uiautomator2函数获取包名
```python
device.app_current()#在启动状态下获取app的包名
device.app_list_running()#获得所有的正在运行的app的包名
```

以下是一个获得quark浏览器包名的代码

```python
import uiautomator2 as u2

device = u2.connect('127.0.0.1:62001')
if(device):# 如果连接成功

    print("success in connecting!")#给出提示
    
    if(device(text='夸克')):#如果软件存在
    
        device(text="夸克").click()#打开软件
        
        print(device.app_current())#打印包名
        
    else:#如果软件不存在, 开始下载
    
        print("begin to download")
        
        url = 'https://umcdn.uc.cn/download/36734/quark/kk@other_zcwkaic409/QuarkBrowser_V6.2.5.247_android_pf3300_(zh-cn)_release_(Build230331123444-arm32).apk'
        device.app_install(url)
        
        print("success")
        
else:#如果连接失败

    print("sorry, failed to connect the device")#给出提示
```

## 2. 利用adb指令获取包名

# 卸载app

```python
device.app_uninstall('包名')
```

包名是用`device.app_current()`获取的

# 清除app数据

清除app的缓存

```python
device.app_clear()
```