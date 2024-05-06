- 设置元素的属性（比如：src,title,class），
    
- 完整格式为：==v-bind:属性名 = 表达式==，简写的话可以直接省略v-bind，只保留 :属性名
    
- 需要动态的增删class建议使用对象的方式

```html
<div id = "app">
    <img v-bind:src="imgSrc">  //正常格式
    <img :src="imgSrc"> //简写格式
    <img :src="imgSrc" :class="{active:isActive}"> //对象的方式增删class
</div>

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

<script>
	var app = new Vue({
    	el: "#app", 
    	data:{
			imgSrc:图片地址,
			isActive:false
		}	
	})
</script>

```
