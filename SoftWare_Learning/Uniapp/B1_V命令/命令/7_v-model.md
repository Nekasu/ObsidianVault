- 获取和设置表单元素的值（双向数据绑定）
    
- 绑定的数据会和表单元素值相关联
    
- 绑定的数据对应表单元素的值

```html
<div id = "app">
    <input type="text" v-model="message">
</div>

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

<script>
	var app = new Vue({
    	el: "#app", 
    	data:{
			message:"这就是input标签的value值"
		}
	})
</script>

```