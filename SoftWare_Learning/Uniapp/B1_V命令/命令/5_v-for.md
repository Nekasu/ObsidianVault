- 根据传入的数据生成对应的列表结构，数组经常和v-for结合使用
    
- 语法是==v-for="(item,index) in List"== 或 ==v-for=“item in List”==,其中item代表每一项，index代表索引
    
- 数组长度的更新会同步到页面上，是响应式的

```html
<div id="app">
	<ul>
    	<li v-for="item in arr">元素：{{item}}</li>
    	<h2 v-for="(item,index) in student">{{index}}.{{item.name}}</h2>
	</ul>
</div>


```