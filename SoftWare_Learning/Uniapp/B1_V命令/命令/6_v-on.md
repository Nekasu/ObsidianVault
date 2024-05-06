为元素绑定事件，可以用简写为@，事件绑定的方法写成函数调用的形式，可传入自定义参数及事件修饰符

绑定的方法写在methods属性中，方法内部可以通过this关键字访问data中的数据

事件的后面跟上修饰符，可以对事件进行限制，事件修饰符有多种，.enter 可以限制触发的按键为回车

```html
<div id = "app">
    <input type="button" @click="doIt('nb',666)"
    <input type="text" @keyup.enter="sayHi";
</div>

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

<script>
	var app = new Vue({
   	 	el: "#app",
    	methods:{
			doIt:function(p1,p2){}
			sayHi:function(){}
		}
	})
</script>
```

