### 变量

* 在使用变量前，需要对其先赋值。

* 变量名可以包括字母、数字、下划线、但不能以数字开头。

* 字母可以是大写或者小写，但大小写是不同的。

* 创建字符串时，要在字符串两边加上引号，可以是单引号或者双引号。

* 如果字符串需要出现单引号或者双引号，例如打印：Let's go

  - 使用转义符号（\）

  - 在'' ''中嵌套' '

* 如果需要使用原始字符串，只需要在字符串前加上r即可。

* 如果需要使用长字符串（多行）的话，使用"""与"""或者'''与'''包裹起来即可。

------

以上笔记的代码如下：

```javascript
str1 = "Python\n"
str2 = 'Python\n'
#使用转义符
str3 = 'Let\'s go\n'
#在""中嵌套''
str4 = "Let's go\n"
#使用原始字符串，在字符串前加上r
str5 = r'C:\User\n'
#使用长字符串（多行）的话，使用"""与"""或者'''与'''包裹起来
str6 = """
你好Python!
Hello Python!
"""
str7 = '''
你好Python!
Hello Python!
'''
print(str1, str2, str3, str4, str5, str6, str7)
```

运行结果：

```javascript
Python
 Python
 Let's go
 Let's go
 C:\User\n 
你好Python!
Hello Python!
 
你好Python!
Hello Python!
```


## 持续更新中..

## 问题反馈
* 邮件:1297394526@qq.com
* QQ:1297394526
* Github: [@fangguizhen](https://github.com/fangguizhen)
