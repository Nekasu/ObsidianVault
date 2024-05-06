- 根据表达式的布尔值，通过style切换元素的display属性进行显示与隐藏
    
- 表达式为true则显示该节点，反之则反之
    
- 数据改变之后，对应元素的显示状态会同步更新

```html
<div id = "app">
    <img src="地址" v-show="isShow">
    <img src="地址" v-show="age>=18">
</div>

```