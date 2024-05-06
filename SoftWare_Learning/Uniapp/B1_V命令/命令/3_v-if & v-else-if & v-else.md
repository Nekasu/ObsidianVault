- 类似于逻辑结构，根据条件判断选择性的渲染DOM结构
    
- 表达式为true则渲染该节点的DOM结构，反之则反之
    
- 频繁切换可以用[v-show](https://so.csdn.net/so/search?q=v-show&spm=1001.2101.3001.7020)，减小切换损耗

```html
<div id = "app">
    <p v-if="isShow">我是一个p标签</p>
    <p v-else-if="表达式">我是一个p标签</p>
    <p v-else">我是一个p标签</p>
</div>

```