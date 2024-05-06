冒号+属性名其实就是v-bind的简写, 如下所示

```vue
<swiper :indicator-dots="true" :autoplay="true" :interval="3000" :duration="1000">
```

- 在「加了冒号」的情况下, 这些属性将会把后面引号里的字符串理解成「指令」
- 「没有冒号」则会将其解析成「字符串」