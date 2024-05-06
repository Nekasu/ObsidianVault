
# uni-ui是什么？

[链接](https://uniapp.dcloud.net.cn/component/uniui/uni-ui.html)

# 如何让项目自动引入Uni-ui的组件？

[链接](https://uniapp.dcloud.net.cn/component/uniui/quickstart.html)

![[Pasted image 20231220223256.png]]


# 安全起见, 请安装uni-ui的ts类型申明文件

## 安装

```
pnpm i -D @uni-helper/uni-ui-types
```


## 配置

```ts
// tsconfig.json
{
  "compilerOptions": {
    "types": [
      "@dcloudio/types",
      "@uni-helper/uni-app-types", // [!code ++]
      "@uni-helper/uni-ui-types" // [!code ++]增加这一行
    ]
  }
}
```