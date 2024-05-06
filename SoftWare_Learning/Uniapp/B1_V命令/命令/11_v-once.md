- 只在第一次渲染时执行，在之后的执行中都会被当作静态内容，跳过之后所有的渲染过程
    
- 如下代码，开始显示1，点击后显示2，再次点击不会改变前端页面数值

```html
<div id = "app">
	<h1>{{cnt}}</h1>
    <button @click='cnt++'>点我cnt+1</button>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

<script>
	var app = new Vue({
    	el: "#app", 
    	data:{
			cnt=1
		}	
	})
</script>

```