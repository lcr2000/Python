## Python数据类型

#### 1、获得关于类型的信息

* 使用type()

```javascript

a = '123'
type(a)
<class 'str'>
type(1.1)
<class 'float'>
type(True)
<class 'bool'>

```


* 使用isinstance()


```javascript

a = 'Python'
isinstance(a,str)
True
isinstance(a,int)
False
isinstance(520,int)
True

```
