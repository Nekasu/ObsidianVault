- 主要作用是设置标签内的文本为message
    
- 一般来说会用message取代标签内的所有内容
    
- 可以用{{message}}插值表达式代替v-text
    

注：message可以是文本，变量，表达式

```html
<div id='app'>
	<h2 v-text = 'message'></h2>
	<h3>{{message}}</h3>
</div>

```


