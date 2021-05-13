# Pyhton

数据存储：计算机存储数据，先开辟内存空间，再存储数据。计算机开辟内存的最小单位是字节。在存储数据时，用最高位标识符号，1表示负数，0表示正数

源码：规定了字节数，写明了符号位，就得到了数据的源码

反码：正数的反码是其源码。负数的反码是其源码的符号位不动，其他取反

### 3. 补码

补码的表示方法是:

- 正数的补码就是其本身
- 负数的补码是在其原码的基础上, 符号位不变, 其余各位取反, 最后+1. (即在反码的基础上+1)

## 变量与运算符

标识符：是一串字符串

规则：只能由字母，数字，下划线组成。开头不能时数字。不能时关键字.区分大小写。见名知意

作用：给函数和变量命名

注意：在python3中，非ASCII标识符也是允许的

> 关键字
>
> ```python
> import keyword
> print(keyword.kwlist)
> ```

变量：程序可操作的存储空间的名称

​			程序运行期间可以改变的数据

​			每个变量都有特定的类型****

​			变量使用前必须被定义

数据存储：变量名 = 变量值

删除变量：del 变量名  --->删除后无法引用

程序执行的过程至上而下，顺序执行

id内存首地址

**常量**：程序运行中不能改变的数据

```python
abs(num) 绝对值
max(num1,num2) 最大值
min(num1,num2) 最小值
pow(2,5) 求x的y次2……5
round(3.2154,1) 
import math
math.ceil(18.1) 向上取整
math.floor(19.2) 向下取整
math.modf(22.3) 返回整数部分和小数部分
math.sqrt(16) 开方
import random
random.choice([1,3,5,6,7]) //随机
print(random.randrange(1,100,2)) 开始结束（不包含）和步长
random.random()零到一之间 的小数
random.shuffle(list) 列表随机
random.uniform(3,9)生产一个实数，他在【3，9】之间
```

### 运算符和表达式

- 表达式：由变量，常量和运算符组成的

### 

## 元组

```shell
key的特性
1.字典中的key必须唯一
2.key必须不可变对象
3.字符串，整数等都是不可变的，可以作为key
4.list是可变，不能作为key
#无序
#查找速度快
#内存占用多
pri = {"tom": 70, "cat": 60}
print(pri["tom"])
print(pri.get("tom")
#添加
pri["jack"] = 99
#删除
pri.pop("tom")
print(pri)
#遍历
for key in pri:
    print(key, pri[key])
for value in pri.values():
    print(value)
for k, v in pri.items():
    print(k, v)
for i, v in enumerate(pri):
    print(i, v)
```

时间下一秒

```shell
timeStr = input()
# 12:12:12
# 时:分:秒
timeList = timeStr.split(":")
h = int(timeList[0])
m = int(timeList[1])
s = int(timeList[2])
s += 1
if s == 60:
    m += 1
    s = 0
    if m == 60:
        h += 1
        m = 0
        if h == 24:
            h = 0
print("%d:%d:%d" % (h, m, s))
```



## 集合

```shell
#需要一个列表，元组或字典
#无序的，无重复的
#重复元素在set中会自动过滤
s1 = set([1, 2, 3, 4, 5, 5, 5])
print(s1)
s2 = set((1, 2, 3, 4, 2, 1, 2, 2))
print(s2)
s3 = set({1: "good", 2: "nice"})
print(s3)
#添加
s4 = set([1,2,3,4,5])
s4.add(6)
#s4.add([7,8,9]) 列表是可变对象，不能为key
s4.add((7,8,9))
#插入
s5 = set([1, 2, 3, 4, 5])
s5.update([6, 7, 8])
s5.update((9, 10))
s5.update("ycc")
print(s5)
#删除
s6 = set([1, 2, 3, 4, 5])
s6.remove(3)
print(s6)
# 遍历
s7 = set([1, 2, 3, 4, 5])
for i in s7:
    print(i)
#显示索引
for index, data in enumerate(s7):
    print(index, data)
#集合交集
s8 = set([1, 2, 3, 4, 5])
s9 = set([3, 4, 5, 6, 7])
# 交集
intersection = s8 & s9
print(intersection)
print(type(intersection))
# 并集
union = s8 | s9
print(union)
print(type(union))
### list>set
set(list)
list(set)
tuple(set)
### 列表去重
s10 = [1, 2, 3, 4, 2, 2, 1, 2, 3, 1, 2, 3]
print(s10)
s11 = []
for i in s10:
    if i in s11:
        continue
    s11.append(i)
print(s11)
#可迭代对象：可以直接用于for循环的对象都是可迭代对象
# isinstance()判断一个对象是不是可迭代对象
#for循环的对象分为两类
# 一类：list tuple,dict,set ,string
# 二类：包括生成器和带yield的generator function
from collections.abc import Iterable

print(isinstance([], Iterable))

```

迭代器

```shell
迭代器：不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后跑到一个stopIteration错误表示无法继续返回一下个值
可以被next()函数调用并不断返回下一个值的对象称为迭代器
可以使用isinsance()函数判断一个对象是不是Iterator
from collections.abc import Iterable
from collections.abc import Iterator

print(isinstance([], Iterable))
print(isinstance([], Iterator))


line = (i for i in range(5))
print(next(line))
print(next(line))
print(next(line))
print(next(line))
print(next(line))
#转成迭代器
line = iter([1,2,3,4,5])
print(next(line))
#定义输出
endstr = "end"
str = ""
for line in iter(input, endstr):
    str += line + "\n"
print(str)
```

## 函数

```shell
认识函数：在一个完整的项目中，某些功能会反复的使用。会将功能封装成函数，直接调用函数
本质：函数就是对功能的封装
优点：
1. 简化代码的结构，增加了代码的复用度
2. 如果想修改某些功能或者修改某个BUG
# 定义函数
格式：
def 函数名(参数列表):
	语句
	return 表达式
def关键字
函数名：遵循标识符规则
（）：参数列表
参数列表：逗号分隔，函数调用
冒号：函数开始
语句：函数封装的功能
return: 一般用于结束函数，并返回信息改函数调用者（默认NOne）
表达式：返回的信息


#值传递《不可变类型
def num(number):
    number = 2


ls = 23
num(ls)
print(ls)



#参数传递 可变类型
def copy(li):
    li[0] = 100


lis = [0, 1, 2, 3, 4]
copy(lis)
print(lis)
```



装饰器

```python
def say(age):
    print("is good  %d man" % (age))


say(-10)


def outer(func):
    def inner(age):
        if age < 0:
            age = 0
        func(age)

    return inner


say = outer(say)
say(-10)
```















































































