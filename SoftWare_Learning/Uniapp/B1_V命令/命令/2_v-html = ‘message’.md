- 主要作用是设置标签内的HTML结构，类似于JS中的 innerHTML
    
- v-html会把字符串解析为HTML代码（区别于v-text的文本）
    
- 解析文本内容使用v-text,需要解析HTML结构使用v-HTML

```html
<div id='app'>
	<p v-html = 'message'></p>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

<script>
	var app = new Vue({
    	el: "#app", 
    	data:{
			message:"<strong> 这个就是v-html</strong>"
		}
	})
</script>

```
