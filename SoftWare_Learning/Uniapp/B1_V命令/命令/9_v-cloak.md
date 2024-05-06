- 可以解决加载Vue页面时，页面的闪烁问题
    
- 在使用插值表达式时，在页面没有及时地返回数据时，页面会闪烁"{{message}}"
    
- 需要在全局样式下添加如下样式，需要在HTML节点上添加 v-cloak 属性

```css
[v-cloak]{
	display:none;
}

```


```html
<div id="app" v-cloak>
  {{message}}
</div>

```