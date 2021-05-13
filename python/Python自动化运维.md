# Python

Python特点：

- 高级
- 面向对象
- 可升级
- 可扩展
- 可移植性
- 易学
- 易读
- 内存管理器

### 安装

```shell
# 安装中文
yum install ibus ibus-libpinyin
# 安装依赖
[root@workstation ~]#  yum -y install gcc gcc-c++ zlib-devel openssl-devel readline-devel libffi-devel sqlite-devel tcl-devel tk-devel make 
# 安装Python3
[root@workstation ~]# tar -xf Python-3.7.6.tgz 
[root@workstation ~]# cd Python-3.7.6/
[root@workstation Python-3.7.6]# ./configure --prefix=/usr/local
[root@workstation Python-3.7.6]# make && make install
# 配置python终端补齐
[root@workstation ~]# cat /usr/local/bin/tab.py 
from rlcompleter import readline
readline.parse_and_bind('tab_complete')
[root@workstation ~]# cat ~/.bashrc 
export PYTHONSTARTUP='/usr/local/bin/tab.py'
# windows终端补齐
pip install pyreadline
# 创建虚拟环境
# Pyhton3中已经自带虚拟环境模块venv
[root@workstation ~]# python3 -m venv ~/mypy
[root@workstation ~]# source ~/mypy/bin/activate
(mypy) [root@workstation ~]# python --version
Python 3.7.6
```

什么是IDE

- 实际开发中，除编译器是必须的，还需要很多辅助软件：
  1. 编辑器：
  2. 代码提示器：
  3. 调试器：
  4. 项目管理工具：
  5. 漂亮的界面：

PyCharm配置

```shell
[root@workstation ~]# yum -y install alacarte
```

### 基本语法

```shell
# 交互解释器
(mypy) [root@workstation ~]# python
Python 3.7.6 (default, Apr 30 2021, 10:24:35) 
[GCC 8.2.1 20180905 (Red Hat 8.2.1-3)] on linux
Type "help", "copyright", "credits" or "license" for more information.
readline: tab_complete: no key sequence terminator
>>> 
# 设置python解释器
(mypy) [root@workstation pythonProject2]# which python
/root/mypy/bin/python
```

语句块缩进

- python代码块通过缩进对齐代表代码逻辑而不是使用大括号
- 缩进风格：4个空格
- 缩进相同的一组语句构成一个代码块，称之代码块
- 首行一关键字开始，一冒号：结束，该行之后的一行或多行代码构成代码组
- 如果代码组只有一行，可以将其直接写在冒号后面，但是这样的写法可读性差，不推荐

注释及续行

- 尽管Python是可读性最好的语言之一，这并不意味着程序员在代码中就可以不写注释
- 和很多UNIX脚本类似，python注释语句从#字符开始
- 注释可以在一行的任何地址开始，解释器会忽略掉该行#之后的所有内容
- 一行过长的语句可以使用反斜杠分\解成几行
- 分号，允许你将多个语句写在同一行上
- 但是些语句不能在这行开始一个新的的代码块
- 因为可读会变差，所以不推荐使用

获得帮助

```python
help(print)
```

输出方式

```python
print("hello world")
print("hello", "world")
print("hello"+" world")
print("hello" ," world",seq="*")
```

输入方式

```python
input("please is a name")
```

#### 变量

变量定义

- 第一个字符只能是大小写字母或下划线
- 后续字符只能是大小写字母或数字或下划线
- 区分大小写

python是动态类型语言，既不需要预先声明变量的类型

推荐采用的全名方法

- 变量名全部采用小写字母
- 简短，有意义
- 多个单词间用下划线分割
- 变量名用名词，函数名用谓词（动词，名词）
- 类名采用驼峰形式

#### 数据类型

##### 进制

默认打印十进制

以0b开头的数是二进制   bin()转化成二进制

以0o开头是八进制，python2中以零开头也是八进制  oct()

以0x开头是十六进制   hex()

##### 数据类型的转换

转换成int  int()  print(x,16)十六进制
转换成float float()
转换成str  str()
转换成bool(数字一或零存储)  bool()  数字除了0都是True 字符串只有''是False  None是False []是False ()是False  {}是False set()是False

##### 运算符

```python
算数运算符 + — * / ** //整除（向下取整）   %取余
```


```python
赋值运算符  m,n = 3,5  q,*w,e=1,2,3,1,4,56
```

```python
比较运算符  不等于 （'a' == 97）
```

```python
 逻辑运算符	 and  or  not 短路 and false是不执行后面的语句，都是true取最后一个 or true不执行 
```

```python
位运算符
按位异或：相同为0，不同为1   ^
按位或：只要有一个为1，就为1  |
按位与：同1则为1，否则为0   &
按位左移   <<
按位右移   >>
```

##### 运算符优先级

```python
运算符           描述
**            指数
~+-           按位翻转 正负号
*/ % //       乘， 除，取模，取整除
+-            加减
>> <<         右移，左移
&             按位与
^ |           位运算符
<= < > >=     比较运算符
<> == !=      等于运算符
= %= /= //= -= += *= **= 赋值运算符
is  not is    身份运算符  是不是同时引用一个对象 
in  not in    成员运算符 属不属于一个队列
not>and>or    逻辑运算符
```

##### 逻辑运算符规则

```python
逻辑与运算
	#只要有一个运算数是False,结果就是False;只有所有的运算数都是True，结果才是True
    #短路：只要遇到了False，就停止，不在继续执行了
    #取值：取第一个为False，如果所有的运算数都是True,取最后一个运算数
逻辑或运算
	#只要有一个运算数是True,结果就是True;只有所有的运算数都是False，结果才是False
    #短路：只要遇到了True，就停止，不在继续执行了
    #取值：取第一个为True，如果所有的运算数都是False,取最后一个运算数
```

##### 列表|元组

##### 数据类型比较

- 按存储模型分类
  1. 标量类型：数值，字符串
  2. 容器类型：列表，元组，字典
- 按更新模式分类
  1. 可变类型：列表，字典
  2. 不可变类型：数字，字符串，元组
- 按访问模型分类
  1. 直接访问：数字
  2. 顺序访问：字符串，列表，元组
  3. 映射访问：字典

### 判断

- 标准if条件语句的语法

```python
if expression:
    if_suite
else:
    else_suite
```

- 如果表达式的值非0或者布尔值True，则代码组if_suite被执行；否则就去执行else_suite
- 代码组是一个python术语，它由一条或多条语句组成，表示一个子代码块

```python
import getpass
user = input('请输入用户名： ')
passwd = getpass.getpass('请输入密码： ')
if user == 'bob' and passwd == '123456':
    print('login sccue')
else:
    print('error')
a = 10
b = 20
s = a if a < b else b
```

条件表达式

```python
x,y = 3,4
smaller = x if x < y else y
print(smaller)
```

剪刀石头布

```python
import random

all_choice = ['剪刀', '石头', '布']
computer = random.choice(all_choice)
player = input('请出拳（剪刀/石头/布）： ')
if player == '石头':
    if computer == '石头':
        print('平局')
    elif computer == '剪刀':
        print('你赢了')
    elif computer == '布':
        print('你输了')
elif computer == "剪刀":
    if computer == '石头':
        print('你输了')
    elif computer == '剪刀':
        print('平局')
    elif computer == '布':
        print('你赢了')
else:
    if computer == '石头':
        print('你赢了')
    elif computer == '剪刀':
        print('你输了')
    elif computer == '布':
        print('平局')
```

### 循环

- 一组被重复执行的语句称之为循环体，能否继续重复，决定循环的终止条件
- Python中的循环有while循环和for循环
- 循环次数未知的情况下，建议采用while循环
- 循环次数预知的情况下，建议采用for循环

当需要语句不断的重复执行时，可以使用while循环

```python
while expression:
    while_suite
```

当预知次数执行时

```python
sum = 0
counter = 1
while counter <= 100:
    sum +=counter
    counter
print(sum)
array1 = [1, 100, 1]
an = array1[0] + (array1[1] - 1) * array1[2]
sn = (array1[1] * (array1[0] + an)) // 2
print(sn)
import random

player_sum = 0
computer_sum = 0
while True:
    while True:
        player = int(input('请输入石头（0），剪刀（1），布（2）: '))
        if player in [0, 1, 2]:
            break
    all_choice = ['石头', '剪刀', '布']
    computer = random.choice(all_choice)
    success = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
    player = all_choice[player]
    print('你出的是 %s,电脑出的 %s' % (player, computer))
    if computer == player:
        print('平局')
    elif [player, computer] in success:
        print('本局你赢了')
        player_sum += 1
    else:
        print('本局你输了')
        computer_sum += 1
    if player_sum >= 2:
        print('你赢了')
        break
    if computer_sum >= 2:
        print('你输了')
        break
```

break

- break语句可以结束当前循环然后跳转到一条语句
- 写程序时，尽量避免重复的代码，在种情况下可以使用while-break结构

```python
    while True:
        player = int(input('请输入石头（0），剪刀（1），布（2）: '))
        if player in [0, 1, 2]:
            break
```

continue

```python
sum = 0
counter = 0
while counter < 100:
    counter += 1
    if counter % 2:
        continue
    sum += counter
print(sum)
```

else语句

- python中的while语句也支持else子句
- else子句只在循环完成后执行
- break语句也会跳过else块

```python
import random

counter = random.randint(1, 100)
count = 0
while count < 5:
    ls = int(input('请输入您猜的数字（1~100）： '))
    if ls > counter:
        print("您输入的大了")
    if ls == counter:
        print('猜对了')
        break
    count += 1
else:
    print(counter)
```

for

- python中的for接受可迭代对象（例如序列和迭代器）作为其参数，每次迭代其中一个元素

```python
for iter_var in iterable:
    suite_to_repeat
```

- 与while循环一样，支持break，continue，else语句
- 一般情况下，循环次数未知采用while循环，循环次数已知，采用for循环

range函数

- for循环常与range函数一起使用
- range函数提供循环条件
- range函数的完整语法为：

```pyth
range(start,end,step=1)
```

斐波那契数列

```python
alist = [0, 1]
n = 10
for i in range(n-2):
    alist.append(alist[-2] + alist[-1])
print(alist)
print(len(alist))
```

列表解析

- 它是一个非常有用，简单，而且灵活的工具，可以用来动态地创建列表

- 语法：

  ```python
  [expr for iner_var in iterable]
  ```

- 这个语句和核心是for循环，它迭代inerable对象的所有条目

- expr应用于序列的每个成员，最后的结果值该表达式产生的列表

```python
[2 + i for i in range(10) if i % 2 == 1 ]
['192.168.1.%d' % i for i in range(1, 255)]
['%s.com' % i for i in domains]
```

九九乘法表

```python
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%dx%d=%d' % (j, i, j * i), end=' ')
    print()
```

### 文件打开方法及读取

#### 打开文件

- 作为打开文件之门的”钥匙“，内建函数open()提供了初始化输入/输出（I/O）操作的通用接口
- 成功打开文件后会返回一个文件对象，否则引发一个错误
- 基本语法：

```python
file_object=open(file_name,mode='r',buffering=-1)
```

打开模式

| 文件模式 |                     操作                     |
| :------: | :------------------------------------------: |
|    r     |        读方式打开（文件不存在则报错）        |
|    w     | 以写方式打开（文件存在则清空，不存在则创建） |
|    a     |      以追加模式打开（必要时创建新文件）      |
|    r+    |           以读写模式打开（参见r）            |
|    w+    |           以读写模式打开（参见w）            |
|    a+    |           以读写模式打开（参见a）            |
|    b     |               以二进制模式打开               |

#### 文件输入

read()

- read()方式用来直接读取字节到字符串中，最多读取给定数目个字节
- 如果没有给定size参数（默认值-1）或者size值为负，文件将被读取直至尾部

readline()

- 读取打开文件的一行（读取下个行结束之前的所有字符）
- 然后整行，包括行结束符，作为字符串返回
- 他也有一个可选的size参数，默认为-1，代表读至行结束符
- 如果提供了该参数，那么在超过size个字节后会返回不完整的行

readlines()

- readlines()方法读取所有（剩余的）行然后把它们作为一个字符串列表返回

```python
f = open('D:\student\project\pythonProject\ls.py')
data = f.read(1)
data2 = f.readline()
print(data)
print(data2)
f.close()
```

文件迭代

- 如果需要逐行处理文件，可以结合for循环迭代文件
- 迭代文件的方法与处理其他序列类型的数据类似

```python
f = open('D:\student\project\pythonProject\ls.py')
for line in f:
    print(line, end='')
f.close()
```

### 写文件及文件指针

write()

- write()内建方法功能与read()和readline()相反，它把含有文本数据或二进制数据块的字符串写入到文件中去
- 写入文件时，不会自动添加行结束标志，需要程序员手工输入

writelines()

- 和readlines()一样，writelines()方法时针对列表的操作
- 它接受一个字符串列表作为参数，将它们写入文件
- 行结束符并不会被自动加入，所以如果需要的话，必须在调用writelines()前给每一行结尾加上行结束符

```python
f = open('D:\student\project\pythonProject\ls.py', 'w')
f.writelines(['sss\n', 'sss\n', 'sdada\n', 'yy\n'])
f.flush()
f.close()
```

```python
f = open('D:\student\project\pythonProject\ls.py', 'ab')
s1 = '中国\n'
f.write(s1.encode())
print(s1.encode())
print(b'\xe4\xb8\xad\xe5\x9b\xbd\n'.decode())
f.flush()
f.close()
```

#### 操作文件

with子句

- with语句时用来简化代码的
- 在将打开文件的操作放在with语句中，代码块结束后，文件将自动关闭

```python
with open('D:\student\project\pythonProject\ls.py') as f:
```

文件内移动

- seek(offset[,whence]):移动文件指针到不同的位置
  1. offset是相对与某个位置的偏移量
  2. whence的值，0表示文件开头，1表示当前位置，2表示文件的结尾
- tell():返回当前文件指针的位置

```python
with open('D:\student\project\pythonProject\ls.py', 'rb') as f:
    f.seek(6, 0)
    print(f.read(5))
    f.seek(-7, 2)
    print(f.readlines())
    x = '中国'
    print(x.encode())
```

```python
src_file = 'D:\student\project\pythonProject\ls.py'
dest_file = 'D:\student\project\pythonProject\ls4.py'

src_fobj = open(src_file, 'rb')
dest_fobj = open(dest_file, 'wb')
while 1:
    data = src_fobj.read(4096)
    # if data == b'':
    # if len(data) == 0:
    if not data:
        break
    dest_fobj.write(data)
src_fobj.close()
dest_fobj.close()
```

### 函数基础

函数基本操作

- 函数是对程序逻辑进行结构或过程化的一种编程方法
- 将整块代码巧妙地隔离成易于管理的小块
- 把重复代码放到函数中而不是进行大量的拷贝，这样既能节省空间，也有助于保持一致性
- 通常函数都是用于实现某一种功能

创建函数

- 函数是用def语句来创建的
- 标题行由def关键字，函数名字，以及参数的集合（如果有的话）组成
- def子句的剩余部分包括一个虽然可选但是强烈推荐的文档字串，和必需的函数体

调用函数

- 同大多数语言相同，python用一对圆括号调用函数
- 如果没有加圆括号，只是对函数的引用

函数的返回值

- 多数情况下，函数并不直接输出数据，而是向调用者返回值
- 函数的返回值使用return关键字
- 没有return的话，函数默认返回None

```python
def xiefbnq():
    counter = int(input('请输入斐波那契数列的长度： '))
    alist = [0, 1]
    for i in range(counter - 2):
        alist.append(alist[-1] + alist[-2])
    return alist


a = xiefbnq()
print(a)
```

### 函数参数

```python
def xiefbnq(n):
    alist = [0, 1]
    for i in range(n - 2):
        alist.append(alist[-1] + alist[-2])
    return alist


nlist = [10, 6, 5]
for i in nlist:
    print(xiefbnq(i))

l = int(input('请输入斐波那契数列的长度： '))
print(xiefbnq(l))
```

定义参数

- 形式参数
  1. 函数定义时，紧跟在函数名后（圆括号内）的参数被称为形式参数，简称形参。由于他不是实际存在变量，所以又称为虚拟变量
- 实际参数
  1. 在主调函数中调用一个函数时，函数名后面括弧中的参数（可以是一个表达式）称为”实际参数“，简称实参

传递参数

- 调用函数时，实参的个数需要与形参个数一致
- 实参将依次传递给形参

位置参数

- 与shell脚本类似，程序名以及参数都以位置参数的方式传递给python程序
- 使用sys模块的argv列表接收

```python
import sys
print(sys.argv)
print(sys.argv[0])
```

默认参数

- 默认参数就是声明了默认值的参数
- 因为给参数赋予了默认值，所以在函数调用时，不向该参数传入值也是允许的

```python
def pstar(n=30):
    print('*' * n)
pstar()
```

```python
import sys

src = sys.argv[1]
dest = sys.argv[2]


def cp2(src_file, dest_file):
    src_fobj = open(src_file, 'rb')
    dest_fobj = open(dest_file, 'wb')
    while 1:
        data = src_fobj.read(4096)
        # if data == b'':
        # if len(data) == 0:
        if not data:
            break
        dest_fobj.write(data)
    src_fobj.close()
    dest_fobj.close()


cp2(src, dest)
```

### 模块基础

- 模块是从逻辑上组织python代码的形式
- 当代码变得相当大的时候，最好把代码分成一些由组织的代码段，前提是保证它们的彼此交互
- 这些代码片段相互间有一定的联系，可能是一个包含数据成员和方法的类，也可能是一组相关但彼此独立的操作函数

创建模块

- 模块物理层面上组织模块的方法就是文件，每一个以.py作为结尾的python文件都是一个模块
- 模块名称切记不要与系统中已存在的模块重名
- 模块文件名字去掉后面的扩展名(.py)即为模块名

导入模块

- 使用import导入模块
- 模块属性通过”模块名.属性“的方法调用
- 如果仅需要模块中的某些属性，也可以单独导入

```python
import datetime  as dt
from random import randint

print(randint(1, 100))

print(datetime.datetime.now())
```

模块加载（load）

- 一个模块只被加载一次，无论它被导入多少次
- 只加载一次可以阻止多次重导入时代码被多次执行
- 如果两个文件相互导入，防止了无限的相互加载
- 模块加载时，顶层代码会自动执行，所以只将函数放入模块的顶层时良好的编程习惯

### 模块特性及案例

模块导入的特性

```python
# 模块具有一个__name__特殊属性
# 当模块文件直接执行时，__name__的值为 ‘__main__'
# 当模块被另一个文件导入时，__name__的值就是该模块的名字
# main+tab
```

```python
import random
from string import ascii_letters,digits
#all_char = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
all_char = ascii_letters + digits

def passwd(n=8):
    passwd = ''
    for i in range(n):
        nmb = random.choice(all_char)
        passwd += nmb
    return passwd


if __name__ == '__main__':
    print(passwd(5))
    print(passwd())
```

### shutil模块

- shutil.copy(src,dst,*,follow_symlinks=True

  将文件src复制到文件或目录dst。src和dst应为字符串。如果dst指定目录，则文件将使用src的基本文件名复制到dst中，返回新创建的文件的路径

- shutil.copy2(src,dst,*,follow_symlinks=True)

  与copy()相同，但是copy2()也尝试保留所有文件元数据

- shutil.move(src,dst,copy_function=copy2)

  递归地将文件或目录(src)移动到另一个位置(dst),并返回目标

- shutil.copytree(src,dst,symlinks=False,ignore=None,copy_function=copy2,ignore_dangling_symlinks=Flase)

  递归地复制以src为根的整个目录树，返回目标目录。由dst命名的目标目录不能已经存在

- shutil.rmtree(path,ignore_errors=False,onerror=None)

  删除整个目录树，路径必须指向目录（而不是指向目录的符号连接）

```python
import shutil

f1 = open('./ls.py', 'rb')
f2 = open('./ls7.py', 'wb')
shutil.copyfileobj(f1, f2)
f1.close()
f2.close()
shutil.copy('./ls.py', './ls8.py')
```

权限管理

- shutil.copymode(src,dst,*,follow_symlinks=True

  将权限位从src复制到dst.文件内容，所有者和组不受影响。src和dst是以字符串形式给出的路径名称

- shutil.copystat(src,dst,8,follow_symlinks=True)

  将权限位，最后访问时间，上次修改时间和标志从src复制到dst

- shutil.chown(path,user=None,group=None)

  更改给定路径的所有者用户和/或组

### subprocess模块

- subprocess模块主要用于执行系统命令
- subprocess模块允许你产生新的进程，连接到它们的输入/输出/错误管道，并获得它们的返回代码
- 本模块旨在替换几个较早的模块和功能，如：os.system,os.spawn*

run方法

- subprocess.run方法python3.5引入。早期版本可以使用subprocess.call方法

```python
import subprocess

result = subprocess.run('echo -E sadad', shell=True)
subprocess.run(['netstat', '-an'])
print(result.returncode)
print(result.args)
```

- run方法执行的结果默认打印在屏幕上，也可以通过管道将其存储在标准输出和标准错误中

```python
import subprocess
import sys


def ping(hosts):
    result = subprocess.run('ping -n 1 %s ' % hosts, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    if result.returncode == 0:
        return '%s is up' % hosts
    else:
        return '%s is down' % hosts


if __name__ == '__main__':
    host = sys.argv[1]
    print(ping(host))
```

### python语法风格及模块布局

变量赋值

- python支持链式多重赋值

  x = y = 10

- 另一种将多种变量同时赋值的方法称为多元赋值，采用这种方式赋值时，等号两边的对象都是元组

  a,b = 10,20

合法标识符

- python标识符字符串规则和其他大部分用C编写的高级语言相似
- 第一个字符必须时字母或下划线（_）
- 剩下的字符可以时字母和数字或下划线
- 大小写敏感

关键字

- 和其他的高级语言一样，python也拥有一些被称作关键字的保留字符
- 任何语言的关键字应该保持相对的稳定，但是因为python是一门不断成长和进化的语言，其关键字偶尔会更新
- 关键字列表和iskyword()函数都放入了keyword模块以便查阅

内建

- 除了关键字之外，python还有可以在任何一级代码使用的”内建“的名字集合，这些名字可以由解释器设置或使用
- 虽然built-in不是关键字，但是应该把它当作”系统保留字“

模块结构及布局

```python
#!/usr/local/bin/python3				# 起始行
"""this is a test module"""				# 模块文档字符串
import sys								# 导入模块
import os
debug = True							# 全局变量声明
class FooClass(object):					# 类定义
    'Foo class'
    pass
def test():								# 函数定义
    """test function"""
    foo = FooClass()
if __name__ == '__main__':				# 程序主体
    test()
```

```python
"""this is a test 关键字"""
from string import ascii_letters, digits
import sys
import keyword

first_chars = ascii_letters + '_'
other_chars = first_chars + digits


def test(idt):
    """this is a test function"""
    if keyword.iskeyword(idt):
        return '%s是关键字' % idt
    if idt[0] not in first_chars:
        return '首字不合法'
    for i in range(len(idt)):
        if i == 0:
            continue
        if idt[i] not in other_chars:
            return '第%d个字符%s不合法' % (i+1, idt[i])
    return '%s 是合法' % idt


if __name__ == '__main__':
    print(test(sys.argv[1]))
```

### 模块布局案例

```python
"""this is a test 关键字"""
from string import ascii_letters, digits
import sys
import keyword
import os

filename = input('请输入文件（必须是不存在的）： ')


def get_filename():
    while 1:
        if not os.path.exists(filename):
            break
        print('文件已存在')
    return filename


def get_content():
    content = []
    print('请输入文件内容,单独一行以end结束： ')
    while 1:
        line = input('(end to quit)> ')
        if line == 'end':
            break
        content.append(line + '\n')
    return content


def wfile(filename, content):
    with open(filename, 'w') as fobj:
        fobj.writelines(content)


if __name__ == '__main__':
    filename = get_filename()
    content = get_content()
    wfile(filename, content)
```

### 序列对象及字符串格式化

序列对象

| 序列操作符     | 作用                             |
| -------------- | -------------------------------- |
| seq[ind]       | 获得小标的ind的元素              |
| seq[ind1:ind2] | 获得小标为ind1到ind2间的元素集合 |
| seq * expr     | 序列重复expr次                   |
| seq1 + seq2    | 连接序列seq1和seq2               |
| obj in seq     | 判断obj元素是否包含在seq中       |
| obj not in seq | 判断obj元素是否不包含在seq中     |

内建函数

| 函数          | 含义                                          |
| ------------- | --------------------------------------------- |
| list(iter)    | 把可迭代对象转换为列表                        |
| str(obj)      | 把obj对象转换成字符串                         |
| tuple(iter)   | 把一个可迭代对象转换成一个元组对象            |
| len(seq)      | 返回seq的长度                                 |
| enumerate     | 接受可迭代对象作为参数，返回一个enumerate对象 |
| reversed(seq) | 接受序列作为参数，返回一个以逆序访问的迭代器  |
| sorted(iter)  | 接受可迭代对象作为参数，返回一个有序的列表    |

```python
users = ['tom', 'jack', 'alice', 'natasha']
for item in enumerate(users):
    print(item)
```

字符串操作符

- 比较操作符：字符串大小按ASCII码值大小进行比较
- 切片操作符：[],[:],[::]
- 成员关系操作符：in,not in

格式化操作符

- 字符串可以使用格式化符号来表示特定含义

| 格式化字符 | 转换方式                      |
| ---------- | ----------------------------- |
| %c         | 转换成字符                    |
| %s         | 优先用str()函数进行字符串转换 |
| %d/%i      | 转成有符号十进制数            |
| %o         | 转成无符号八进制数            |
| %e/%E      | 转成科学计数法                |
| %f/%F      | 转成浮点数                    |

```python
print('%8s %8s' % ('name', 'age'))
```

- 字符串可以使用格式化符号来表示特定含义

| 辅助指令 | 作用                                              |
| -------- | ------------------------------------------------- |
| *        | 定义宽度或者小数点精度                            |
| +        | 左对齐                                            |
| -        | 在正数前面显示加号                                |
| <sp>     | 在正数前面显示空格                                |
| #        | 在八进制数前显示零0，在十六进制前面显示’0x‘或'0X' |
| 0        | 显示的数字前面填充0而不是默认空格                 |

原始字符操作符

- 原始字符操作符是为了对付那些在字符串中出现的特殊字符
- 在原始字符串里，所有的字符都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符 r

```pyhon
"""this is a create user"""
import sys
from string import digits, ascii_letters
import random
import subprocess

all_chars = digits + ascii_letters


def passwd():
    password = ''
    for i in range(8):
        password += random.choice(all_chars)
    return password


def user_add(user, password, filename):
    for i in user:
        if i not in all_chars:
            return '用户名不合法'
    result = subprocess.run('id %s &>/dev/null' % (user), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print('用户已存在')
        return
    subprocess.run('useradd %s' % user, shell=True)
    subprocess.run('echo %s |passwd --stdin %s ' % (password, user), shell=True)
    info = '''用户信息
用户名： %s
密码： %s
''' % (user, password)
    with open(filename, 'a') as fobj:
        fobj.write(info)


if __name__ == '__main__':
    password = passwd()
    user_add(sys.argv[1], password, '/tmp/a.txt')
```

### 字符串常用方法

| 方法                                            | 作用                                                         |
| ----------------------------------------------- | ------------------------------------------------------------ |
| lower()                                         | 将字符串中所有大写英文字母转为小写                           |
| upper()                                         | 将字符串中所有小写英文字母转为大写                           |
| swapcase()                                      | 将字符串中的大写英文字母转为小写，小写英文字母转为大写       |
| capitalize()                                    | 将字符串中第一个字符转为大写，其余转为小写                   |
| title()                                         | 得到“标题化”的字符串，每个单词的首字符大写，其余小写         |
| center(width[, fillchar])                       | 返回一个指定width宽度的居中字符串，fillchar为填充字符串，默认为空格 |
| ljust(width[, fillchar])                        | 返回一个指定width宽度的左对齐字符串，fillchar为填充字符串，默认为空格 |
| rjust(width,[, fillchar])                       | 返回一个指定width宽度的右对齐字符串，fillchar为填充字符串，默认为空格 |
| zfill (width)                                   | 返回一个指定width宽度的右对齐字符串，默认填充0               |
| count(str[, beg= 0[,end=len(string)]])          | 返回str在string中出现的次数，如果beg或者end指定则返回指定范围内的出现次数 |
| find(str[, beg=0[, end=len(string)]])           | 检测str是否包含在string中，默认从左到右查找，如果存在则返回第一次出现的下标，否则返回-1，如果beg或者end指定则在指定范围内检测 |
| index(str[, beg=0[, end=len(string)]])          | 检测str是否包含在string中，默认从左到右查找，如果存在则返回第一次出现的下标，否则返回异常(报错)，如果beg或者end指定则在指定范围内检测 |
| rfind(str[, beg=0[,end=len(string)]])           | 检测str是否包含在string中，默认从右到左查找，如果存在则返回第一次出现的下标，否则返回-1，如果beg或者end指定则在指定范围内检测 |
| rindex(str[, beg=0[, end=len(string)]])         | 检测str是否包含在string中，默认从右到左查找，如果存在则返回第一次出现的下标，否则返回异常(报错)，如果beg或者end指定则在指定范围内检测 |
| lstrip([char])                                  | 截掉字符串左侧指定的字符，默认为空格                         |
| rstrip([char])                                  | 截掉字符右左侧指定的字符，默认为空格                         |
| strip([chars])                                  | 在字符串上执行lstrip和rstrip                                 |
| split(str=" "[, num=string.count(str)])         | 按照str(默人空格)切割字符串，得到一个列表，列表是每个单词的集合 |
| splitlines([keepends])                          | 按照行(’\r’、’\r\n’、’\n’)切割，如果keepends为False，不包含换行符，否则包含换行符 |
| join(seq)                                       | 指定字符拼接列表中的字符串元素                               |
| max(str)                                        | 返回字符串中最大的字符                                       |
| min(str)                                        | 返回字符串中最小的字符                                       |
| replace(old, new[, max])                        | 将字符串中的old替换为new，如果没有指定max值，则全部替换，如果指定max值，则替换不超过max次 |
| maketrans()                                     | 创建字符映射的转换表                                         |
| translate(table, deletechars="")                | 根据给出的转换表转换字符                                     |
| isalpha()                                       | 如果字符串至少有一个字符并且所有的字符都是英文字母则返回真，否则返回假 |
| isalnum()                                       | 如果字符串至少有一个字符并且所有的字符都是英文字母或数字字符则返回真，否则返回假 |
| isupper()                                       | 如果字符串至少有一个字符并且所有的字母都是大写字母则返回真，否则返回假 |
| islower()                                       | 如果字符串至少有一个字符并且所有的字母都是小写字母则返回真，否则返回假 |
| istitle()                                       | 如果字符串是标题化的则返回真，否则返回假                     |
| isdigit()                                       | 如果字符串只包含数字则返回真，否则返回假                     |
| isnumeric()                                     | 如果字符串只包含数字则返回真，否则返回假                     |
| isdecimal()                                     | 检测字符串是否只包含十进制数字                               |
| isspace()                                       | 如果字符串只包含空白符则返回真，否则返回假                   |
| startswith(str[, beg=0[,end=len(string)]])      | 检测字符串是否以str开头，是则返回真，否则返回假，可指定范围  |
| endswith(suffix, beg=0, end=len(string))        | 检测字符串是否以str结尾，是则返回真，否则返回假，可指定范围  |
| encode(encoding=‘UTF-8’,errors=‘strict’)        | 以encoding指定的编码格式进行编码，如果出错报一个ValueError的异常，除非errors指定的值是ignore或replace |
| bytes.decode(encoding=“utf-8”, errors=“strict”) | 以encoding指定的格式进行解码，注意解码时使用的格式要与编码时的一致 |
| ord()                                           | 获取字符的整数表示                                           |
| chr()                                           | 把数字编码转为对应的字符                                     |
| str()                                           | 转为字符串                                                   |
### 列表和元组

创建和访问列表

- 列表是有序，可变的数据类型
- 列表中可以包含不同类型的对象
- 列表可以由[]或工厂函数创建
- 支持小标及切片操作

更新列表

- 通过下标只能更新值，不能使用小标添加新值

列表常用方法

| 列表方法               | 操作                                                         |
| ---------------------- | ------------------------------------------------------------ |
| list.append(obj)       | 向列表中添加一个对象obj                                      |
| list.count(obj)        | 返回一个对象obj在列表中出现的次数                            |
| list.extend(seq)       | 把序列seq的内容添加到列表中                                  |
| list.index(obj)        | 返回obj对象的下标                                            |
| list.insert(index,obj) | 在索引量为index的位置插入对象obj                             |
| list.reverse()         | 原地翻转列表                                                 |
| list.sort()            | 排序                                                         |
| list.pop(index=-1)     | 移除列表中指定下标出的元素，默认移除最后一个，返回被删掉的数据 |
| list.remove(obj)       | 移除列表中第一次出现的obj元素                                |
| list.clear()           | 清空列表                                                     |
| list.max(seq)          | 返回列表中最大的元素                                         |
| list.min(seq)          | 返回列表中最大小的元素                                       |
| list.list(seq)         | 将其他类型的集合转为列表类型                                 |
| list.copy(seq)         | 深拷贝                                                       |

创建元组

- 通过()或工厂函数tuple创建元组
- 元组是有序的，不可变类型
- 与列表类似，作用与列表的操作，绝大多数也可以作用于元组

单元组

- 如果一个元组只有一个元素，那么创建该元组的时候，需要加上一个逗号

### 列表案例

```python
stack = []


def push_it():
    data = input('data: ').strip()
    if data:
        stack.append(data)
    else:
        print('不能为空')


def pop_it():
    if stack:
        print('from stack,popped %s' % stack.pop())
    else:
        print('Empty Stack')


def view_it():
    print(stack)


def show_menu():
    cmds = {'0': push_it, '1': pop_it, '2': view_it}
    prompt = '''(0) push it
(1) pop it
(2) view it
(3) exit
please input your choice(0/1/2/3):  '''
    while 1:
        choice = input(prompt)
        if choice not in ['0', '1', '2', '3']:
            print('重试')
            continue
        if choice == '3':
            print('再见')
            break
        cmds[choice]()


if __name__ == '__main__':
    show_menu()
```

### 字典及常用方法

创建字典

- 通过{}操作符创建字典
- 通过dict()工厂方法创建字典
- 通过fromkeys创建具有相同值的默认字典

```python
adict = dict(('ab', ('c', 'b'), ['d', 'b']))
print(adict)
cdict = {}.fromkeys(('box', 'natasha'), 23)
print(cdict)
```

访问字典

- 字典是映射类型，意味着没有下标，访问字典中的值需要使用相应的键

```python
for key in cdict:
    print(key,cdict[key])
print('%d is %d years old' % (cdict['box'], cdict['natasha']))
print('%(box)s is %(natasha)s' % cdict)
```

更新字典

- 通过键更新字典

  如果字典中有该键，则更新相关值；没有该键，则向字典中添加新值

删除字典

- 通过del可以删除字典中的元素或整个字典

  使用内部方法clear()可以清空字典；pop()方法”弹出“字典中的元素

作用于字典的函数

- len()：返回字典中元素的数目
- hash()：不是为字典设计，可以判断对象是否可以作为字典的键

字典方法

| 方法       | 作用                         |
| ---------- | ---------------------------- |
| get        | 返回key对应的值              |
| key        | 字典的key                    |
| values     | 字典的值                     |
| items      | 字典的key和值                |
| popitem    | 删除随机                     |
| pop        | 删除指定                     |
| update     | 将一个字典在添加到另一个字典 |
| clear      | 清空字典                     |
| copy       | 深拷贝                       |
| setdefault | 设置key的值，已存在不在改变  |

### 字典案例

```python
import getpass

user_db = {}


def register():
    username = input('用户名： ').strip()
    if username is None:
        register()
    if username and username not in user_db:
        password = input('请输入密码： ')
        user_db[username] = password
    else:
        print('用户名已存在')


def login():
    username = input('用户名： ').strip()
    password = getpass.getpass('密码： ')
    if user_db.get(username) != password:
        print('登录失败')
    else:
        print('登录成功')


def show_menu():
    cmds = {'0': register, '1': login}
    prompt = '''(0) 注册
(1) 登录
(2) 退出
请输入（0/1/2）'''
    while 1:
        choice = input(prompt)
        if choice not in ['0', '1', '2']:
            print('重试')
            continue
        if choice == '2':
            print('再见')
            break
        cmds[choice]()


if __name__ == '__main__':
    show_menu()
```

### 集合及常用方法

创建集合

- 数字上，把set称做由不同的元素组成的集合，集合(set)的成员通常被称做集合元素
- 集合对象是一组无序排列的可哈希的值
- 集合有两种类型
  1. 可变集合set
  2. 不可变集合frozeenset

集合类型操作符

- 集合支持用in和not in操作符检查成员
- 能够通过len()检查集合大小
- 能够使用for迭代集合成员
- 不能取切片，没有键
- |：联合，取并集
- &：交集
- -：差补

集合方法

- set.add()：添加成员
- set.update()：批量添加成员
- set.remove()：移除成员
- s.issubset(t)：如果s是t的子集，则返回True，否则返回False
- s.issuperset(t)：如果t是s的超集，则返回True，否则返回False
- s.union(t)：返回一个新的集合，该集合是s和t的并集
- s.intersection(t)：返回一个新的集合，该集合s和t的交集
- s.difference(t)：返回一个新的集合，该集合是s的成员，但不是t的成员

### 集合案例

去重

```python
from random import randint

alist = [randint(1, 50) for i in range(20)]
print(alist)
aset = set(alist)
print(aset)
```

文件对比

```python
import sys

file_name1 = sys.argv[1]
file_name2 = sys.argv[2]
file_name3 = 'list.txt'
with open(file_name1, encoding='utf-8') as file_obj1:
    a_set = set(file_obj1)

with open(file_name2, encoding='utf-8') as file_obj2:
    b_set = set(file_obj2)

with open(file_name3, 'w', encoding='utf-8') as file_obj3:
    file_obj3.writelines(a_set - b_set)
```

# 开发进阶

### time模块

时间表示方式

- 时间戳timestamp：表示的是从1970年1月1日00:00:00开始按秒计算的偏移量
- utc(Coordinated Universal Time,世界协调时)即是世界表最时间。在中国为UTC-8.
- 元组(struct_time)：由9个元素组成

| 索引 | 属性                    | 值             |
| ---- | ----------------------- | -------------- |
| 0    | tm_year                 | 2000           |
| 1    | tm_mon                  | 1~12           |
| 2    | tm_mday                 | 1~31           |
| 3    | tm_hour                 | 0~23           |
| 4    | tm_min                  | 0~59           |
| 5    | tm_sec                  | 0~61           |
| 6    | tm_wday                 | 0-6(0表示周一) |
| 7    | tm_yday(一年中的第几天) | 1~366          |
| 8    | tm_isdst(是否为dst时间) | 默认为-1       |

time模块方法

- time.localtime([secs])：将一个时间戳转换为当前时区的struct.time。secs参数未提供，则以当前时间为准
- time.gmtime([secs])：和localtime()方法类似，gmtime()方法是将一个时间戳转换为UTC时区（0时区）的struct_time
- time.time()：返回当前时间的时间戳
- time.mktime(t)：将一个struct_time转化为时间戳
- time.ctime
- time.sleep(3)：睡眠
- time.strftime

| 格式 | 含义                                            |
| ---- | ----------------------------------------------- |
| %a   | 本地简化星期名称                                |
| %A   | 本地完整星期名称                                |
| %b   | 本地简化月份名称                                |
| %B   | 本地简化月份名称                                |
| %c   | 本地相应的日期和时间                            |
| %d   | 一个月中的第几天（01~31）                       |
| %H   | 一天中的第几个小时（24小时制，00~23）           |
| %I   | 第几个小时（12小时制，01-12）                   |
| %j   | 一年中的第几天（001~366）                       |
| %Z   | 时区的名字                                      |
| %m   | 月份（01~12）                                   |
| %M   | 分钟数（00~59）                                 |
| %p   | 本地am或者pm的相对应符                          |
| %S   | 秒（01~61）                                     |
| %U   | 一年中的星期数（00~53，星期日是一个星期的开始） |
| %w   | 一个星期中的第几天（0~6，0是星期天）            |
| %x   | 本地相应日期                                    |
| %X   | 本地相应时间                                    |
| %y   | 去掉世纪的年份（00~99）                         |
| %Y   | 完整的年份                                      |

```python
import time

count = 0
print('*' * 30, end='')
while 1:
    time.sleep(0.3)
    print('\r%s@%s' % ('*' * count, '*' * (29 - count)), end='')
    count += 1
    if count == 30:
        count = 0
```

### datetime模块

datetime模块方法

- datetime.today()：返回一个表示当前本地时间datetime对象
- datetime.now([tz])：返回一个表示当前本地时间的datetime对象，如果提供了参数tz,则获取tz参数所指时区的本地时间
- datetime.strptime(date_string,format)：将格式字符串转换为datetime对象
- datetime.ctime(datetime对象)：返回时间格式字符串
- datetime.strftime(format)：返回指定格式字符串

时间计算

- 使用timedelta可以很方便的在日期上做天days,小时hour，分钟，秒，毫秒的时间计算

```python
import datetime

dt = datetime.datetime.now()
days = datetime.timedelta(days=100, hours=3)
print(dt + days)
```

```python
import datetime

t9 = datetime.datetime.strptime('2020-01-03 09:00:00', '%Y-%m-%d %H-%M-%S')
t12 = datetime.datetime.strptime('2020-01-03 12:00:00', '%Y-%m-%d %H-%M-%S')
with open('myweb.log') as fobj:
    for line in fobj:
        t = datetime.datetime.strptime(line[:19], '%Y-%m-d %H-%M-%S')
        if t >= t12:
            break
        if t >= t9:
            print(line, end='')
```

### 异常处理

什么是异常

- 当python检测到一个错误时，解释器就会指出当前流已经无法继续执行下去，这时候就出现了异常
- 异常是因为程序出现了错误而在正常控制流以外采取的行为
- 这个行为又分为两个阶段：
  1. 首先是引起异常发生的错误
  2. 然后是检测（和采取可能的措施）阶段

Python中的异常

- 当程序运行时，因为遇到未解的错误而导致中止运行，便会出现traceback消息，打印异常

| 异常              | 描述                      |
| ----------------- | ------------------------- |
| NameError         | 未声明/初始化对象         |
| IndexError        | 序列中没有此索引          |
| SyntaxError       | 语法错误                  |
| Keyboardinterrupt | 用户中断执行              |
| EOFError          | 没有内建输入，到达EOF标记 |
|                   |                           |
|                   |                           |
|                   |                           |
|                   |                           |

try-except语句

-  定义了进行异常监控的一段代码，并且提供了处理异常的机制
- 可以把多个except语句连接在一起，处理一个try块中可能发生的多种异常

异常参数

- 异常也可以有参数，异常引发后它会被传递给异常处理器
- 当异常被引发后参数时作为附加帮助信息传递给异常处理器的

else子句

- 在try范围中没有异常被检测到时，执行else子句
- 在else范围中的任何代码运行前，try中的所有代码必须完全成功

finally子句

- finally子句是无论异常是否放生，是否捕捉都会执行的一段代码
- 如果打开文件后，因为发生异常导致文件没有关闭，可能会发生数据损坏。使用finally可以保证文件总是能正常关闭

```python
try:
    n = int(input('number: '))
except ValueError as e:
    print('无效输入', e)
except (KeyboardInterrupt, EOFError):
    print('再见')
    exit()
else:
    print(n)
finally:
    print('done')
```

```python
try:
    number = int(input('请输入一个数字： '))
    new = 100 / number
except (EOFError, KeyboardInterrupt):
    exit()
except ValueError as e:
    print('请输入数字')
except ZeroDivisionError:
    print('0不能作为被除数')
else:
    print(new)
```

### 自定义异常

raise语句

- 要想引发异常，最简单的形式就是输入关键字raise，后面跟要引发的异常的名称
- 执行raise语句时，Python会创建指定的异常类的一个对象
- raise语句还可指定对异常对象进行初始化的参数

```python
def nameage(name, age):
    if not 1 < age < 120:
        raise ValueError('年龄不合法')
    else:
        print('%s is a %d year' % (name, age))


try:
    nameage('aa', 13)
except ValueError as e:
    print('错误', e)
    exit()
print('done')
```

断言（assert）

- 断言是一句必须等价于布尔值为真的判定
- 此外，发生异常也意外着表达式为假

```python
def nameage(name, age):
    assert 1 < age < 120, '无效的年龄'
    print('%s is a %d year' % (name, age))


try:
    nameage('aa', 143)
except AssertionError as e:
    print('错误', e)
    exit()
print('done')
```

### os模块

os模块简介

- 对文件系统的访问大多通过python的os模块实现
- 该模块是python访问操作系统功能的主要接口
- 有些方法，如copy等，并没有提供，可以使用shutil模块作为补充

os方法

| 命令                  | 书体         |
| --------------------- | ------------ |
| getcwd()              | pwd          |
| listdir()             | ls -a        |
| mkdir()               | mkdir        |
| makedirs()            | mkdir -p     |
| chdir()               | cd           |
| symlink()             | ln -s        |
| chmod('hosts', 0o600) | chmod        |
| remove()              | 删除文件     |
| rmdir()               | 删除空目录   |
| unlink()              | 删除链接文件 |
|                       |              |
|                       |              |
|                       |              |
|                       |              |
|                       |              |
|                       |              |
|                       |              |
|                       |              |
|                       |              |

os.path方法

| 急急急     | 可靠               |
| ---------- | ------------------ |
| abspath()  | 绝对路径           |
| basename() | 最右侧             |
| dirname()  | 最右边左侧         |
| split()    | 最右边/切割        |
| splitext() | 文件名和后缀名分割 |
| join()     | 拼接               |
| isabs()    | 是不是绝对路径     |
| isdir()    | 是不是目录         |
| isfile()   | 是不是文件         |
| islink()   | 是不是链接         |
| ismount()  | 是不是挂载点       |
| exists()   | 是否存在           |
|            |                    |
|            |                    |

### pickle模块及案例

pickle模块简介

- 把数据写入文件时，常规的文件方法只能把字符串对象写入。其他数据需先转换成字符串写入文件
- python提供了一个标准的模块，称为pickle。使用它可以在一个文件中存储任何python对象，之后又可以把完整无缺地取出来

pickle模块方法

- 分别调用dump()和load()可以存储，写入

```python
import pickle

shopping_list = ['apple', 'mango', 'carrot']
f = open('D:\student\project\pythonProject\sa.txt', 'wb')
pickle.dump(shopping_list, f)
f.close()

f = open('D:\student\project\pythonProject\sa.txt', 'rb')
stored_list = pickle.load(f)
f.close()
print(stored_list)
```

记账程序

```python
import pickle
import os
import time


def save(fname):
    date = time.strftime('%Y-%m-%d')
    amount = int(input('金额： '))
    comment = input('备注： ')
    with open(fname, 'rb') as fobj:
        content = pickle.load(fobj)
    balance = content[-1][-2] + amount
    line = [date, amount, 0, balance, comment]
    content.append(line)
    with open(fname, 'wb') as fobj:
        pickle.dump(content, fobj)


def cost(fname):
    date = time.strftime('%Y-%m-%d')
    amount = int(input('金额： '))
    comment = input('备注： ')
    with open(fname, 'rb') as fobj:
        content = pickle.load(fobj)
    balance = content[-1][-2] - amount
    line = [date, 0, amount, balance, comment]
    content.append(line)
    with open(fname, 'wb') as fobj:
        pickle.dump(content, fobj)


def query(fname):
    print('%-12s%-8s%-8s%-12s%-20s' % ('date', 'save', 'cost', 'balance', 'comment'))
    with open(fname, 'rb') as fobj:
        content = pickle.load(fobj)
    for line in content:
        print('%-12s%-8s%-8s%-12s%-20s' % tuple(line))


def show_menu():
    cmds = {'0': save, '1': cost, '2': query}
    fname = 'account.data'
    init_data = [['2020-1-1', 0, 0, 0, 'init data']]
    prompt = """(0) 收入
(1) 支出
(2) 查询
(3) 退出
请选择(0/1/2/3): """
    if not os.path.exists(fname):
        with open(fname, 'wb') as fobj:
            pickle.dump(init_data, fobj)
    while 1:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2', '3']:
            print('无效的选择，请重试')
            continue
        if choice == '3':
            break
        cmds[choice](fname)


if __name__ == '__main__':
    show_menu()
```

### 函数进阶

向前引用

- 函数不允许在函数未声明之前对其进行引用或者调用

函数操作符

- 使用一对圆括号()调用函数，如果没有圆括号，只是对函数的引用
- 任何输入的参数都是必须放置在括号中

关键字参数

- 关键字参数的概念仅仅针对函数的调用
- 这种理念时让调用者通过函数调用中的参数名字来区分参数
- 这样规范允许参数缺失或者不按顺序

参数组

- python允许程序员执行一个没有显式定义参数的函数
- 相应的方法时通过一个把元组（非关键字参数）或字典（关键字参数）作为参数传递给函数

```python
nums = [10, 20]
as_dict = {'name': 'box', 'age': 20}


def function1(*args):
    print(args)


def function2(**kwargs):
    print(kwargs)


def function3(a, b):
    return a + b


def function4(name, age):
    print('%s is a %s la' % (name, age))


function1('s', 1, '2')
function2(name='com', age=20)
print(function3(*nums))

function4(**as_dict)
```

数字游戏

```python
import random


def exam():
    nmb = [random.randint(1, 100) for i in range(2)]
    nmb.sort(reverse=True)

    op = random.choice('+-')
    if op == '-':
        result = nmb[0] - nmb[1]
    else:
        result = nmb[0] + nmb[1]
    count = 0
    prompt = '%s %s %s = ' % (nmb[0], op, nmb[1])
    while count < 3:
        try:
            answer = int(input(prompt))
        except:
            continue
        if answer == result:
            print('Very Good !')
            break
        print('Wrong Answer !')
        count += 1
    else:
        print('%s %s' % (prompt, result))


def main():
    while 1:
        exam()
        try:
            yn = input('Continue(y/n)').strip()[0]
        except IndexError as e:
            yn = 'y'
        except (KeyboardInterrupt, EOFError):
            yn = 'n'
        if yn in 'nN':
            print('退出')
            break


if __name__ == '__main__':
    main()
```

### 匿名函数

lambda

- python允许用lambda关键字创造匿名函数
- 匿名是因为不需要以标准的def方式来声明
- 一个完整的lambda'语句'代表了一个表达式，这个表达式的定义体必须和声明放在同一行

filter()函数

- filter(func,seq)：调用一个布尔函数func来迭代遍历每个序列中的元素；返回一个使func返回值为true的元素的序列
- 如果布尔函数比较简单，直接使用lambda匿名函数就显得非常方便了

```python
from random import randint


def func1(x):
    return True if x % 2 == 1 else False


if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    result = filter(func1, nums)
    #result2 = filter(lambda x: True if x % 2 == 1 else False,nums)
    print(list(result))
```

map()函数

- map(func,seq):调用一个函数func来迭代遍历每个序列中的元素；返回一个经过func处理过的元素序列

```python
    result1 = map(lambda x: x * 2 + 1, nums)
    print(list(result1))
```

reduce()函数

- reduce(func,seq):调用一个函数func来迭代遍历每个序列中的元素；返回一个经过func处理后得到的结果

```python
from functools import reduce

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    result = reduce(lambda x, y: x + y, nums)
    print(result)
```

```python
import random


def exam():
    cmds = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
    nmb = [random.randint(1, 100) for i in range(2)]
    nmb.sort(reverse=True)
    op = random.choice('+-')
    result = cmds[op](*nmb)
    count = 0
    prompt = '%s %s %s = ' % (nmb[0], op, nmb[1])
    while count < 3:
        try:
            answer = int(input(prompt))
        except:
            continue
        if answer == result:
            print('Very Good !')
            break
        print('Wrong Answer !')
        count += 1
    else:
        print('%s %s' % (prompt, result))


def main():
    while 1:
        exam()
        try:
            yn = input('Continue(y/n)').strip()[0]
        except IndexError as e:
            yn = 'y'
        except (KeyboardInterrupt, EOFError):
            yn = 'n'
        if yn in 'nN':
            print('退出')
            break


if __name__ == '__main__':
    main()
```

### 变量作用域

全局变量

- 标识符的作用域是定义为其声明在程序里的可应用范围，也就是变量的可见性
- 在一个模块中最高级别的变量有全局作用域
- 全局变量的一个特征是除非被删除掉，否则它们的存活到脚本运行结束，且对于所有的函数，他们的值都是可以访问的

局部变量

- 局部变量之时暂时地存在，仅仅只依赖于定义它们的函数阶段是否处于活动
- 当一个函数调用出现时，其局部变量就进入声明它们的作用域。在那一刻，一个新的局部变量名为那个对象创建了
- 一旦函数完成，框架被释放，变量将会离开作用域
- 如果局部于全局有相同名称的变量，那么函数运行时，局部变量的名称将会把全局变量名称掩盖住

global语句

- 因为全局变量的名字被局部变量给掩盖掉，所以为了明确地引用一个已命名的全局变量，必须使用global语句

### 偏函数

- 偏函数的概念是将函数式编程的概念和默认参数以可变参数结合在一起
- 一个带有多个参数的函数，如果其中某些参数基本上固定的，那么就可以通过偏函数为这些参数赋默认值

```python
from functools import partial


def add(a, b, c, d):
    print(a + b + c + d)


add10 = partial(add, 10, 20, 30)
add(10, 20, 30, 40)
add10(40)
```

递归函数

- 如果函数包含了对其自身的调用，该函数就是递归的
- 在操作系统中，查看某一个目录所有文件等操作都是递归的应用

```python
def jc(x):
    if x == 1:
        return 1
    return x * jc(x - 1)


if __name__ == '__main__':
    print(jc(5))
```

快速排序

```python
from random import randint

a = [randint(1, 100) for i in range(10)]


def fast_sort(seq):
    if len(seq) < 2:
        return seq
    middle = seq[0]
    smaller = []
    larger = []
    for i in seq[1:]:
        if i <= middle:
            smaller.append(i)
        else:
            larger.append(i)

    return fast_sort(smaller) + [middle] + fast_sort(larger)


if __name__ == '__main__':
    print(a)
    print(fast_sort(a))
```

列出目录文件

```python
import os
import sys


def list_files(path):
    if os.path.isdir(path):
        # print(path + ":")
        content = os.listdir(path)
        print(content)
        # for fname in content:
        #    fname = os.path.join(path, fname)
        #    list_files(fname)


if __name__ == '__main__':
    list_files(sys.argv[1])
```

### 生成器

- 从语法上讲，生成器是一个带yield语句的函数
- 一个函数或者子程序只返回一次，但一个生成器能暂停执行并返回一个中间的结果
- yield语句返回一个值给调用者并暂停执行
- 当生成器的next()方法被调用的时候，他会准确地从离开地方继续

生成器表达式

- 生成器的另一种形式是生成表达式
- 生成器表达试语法于列表解析一样

```python
def gen_block(fobj):
    lines = []
    counter = 0
    for line in fobj:
        lines.append(line)
        counter += 1
        if counter == 10:
            yield lines
            lines = []
            counter = 0
    if lines:
        yield lines


if __name__ == '__main__':
    fname = '/etc/passwd'
    fobj = open(fname)
    for block in gen_block(fobj):
        print(block)
    fobj.close()
```

### 模块和文件

什么是模块

- 模块支持从逻辑上组织python代码
- 当代码量变得相当大的时候，最好把代码分成一些有组织的代码段
- 代码片段相互有一定的联系，可能是一个包含数据成员和方法的类，也可能是一组相关但彼此独立的操作函数
- 这些代码是共享的，所以python允许“调入“一个模块，允许使用其他模块的属性利用之前的工作成果，实现代码重用

模块文件

- 说模块是按照逻辑来组织python代码的方法，文件是物理层上组织模块的方法
- 一个文件被看作是一个独立模块，一个模块也可以被看作是一个文件
- 模块的文件名就是模块的名字加上扩展名.py

搜索路径

- 模块的导入需要一个叫做”路径搜索“的过程
- python在文件系统”预定义区域“中查找要调用的模块
- 搜索路径在sys.path中定义
- 也可以通过PYTHONPATH环境变量引入自定义目录

```python
import mytest.start #引入二级目录 
```

内置模块

tarfile模块

- tarfile模块允许创建，访问tar文件
- 同时支持gzip,bzip2格式

```python
import tarfile
tar = tarfile.open('/home/demo.tar.gz','w:gz')
tar.add('demo')
tar.close()
tar = tarfile.open('/home/demo.tar.gz')
tar.extractall(path='/var/demo')
tar.close()
```

hashlib模块

- hashlib用来替换md5和sha模块，并使他们的API一致，专门提供hash算法
- 包括MD5,sha1,使用非常简单，方便

```python
import hashlib

m = hashlib.md5()
m.update(b'a')
print(m.hexdigest())
```

md5sum

```python
import hashlib
import sys


def check_md5(filename):
    m = hashlib.md5()
    with open(filename, 'rb') as fobj:
        while 1:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()


if __name__ == '__main__':
    print(check_md5(sys.argv[1]))
```

备份

```python
from time import strftime
import hashlib
import tarfile
import pickle
import os


def check_md5(filename):
    m = hashlib.md5()
    with open(filename, 'rb') as fobj:
        while 1:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()


def full_back(src, dest, md5file):
    # 拼接出文件名
    filename = os.path.basename(src)
    filename = '%s_full_%s' % (filename, strftime('%Y%m%d'))
    filename = os.path.join(dest, filename)
    # 备份
    tar = tarfile.open(filename, 'w:gz')
    tar.add(src)
    tar.close()
    # 计算文件的md5值
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)
    # 保存到文件中
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)


def free_back(src, dest, md5file):
    # 拼接出文件名
    filename = os.path.basename(src)
    filename = '%s_free_%s' % (filename, strftime('%Y%m%d'))
    filename = os.path.join(dest, filename)
    # 计算文件的md5值
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)
    # 读取前一天的md5值
    with open(md5file, 'rb') as fobj:
        old_md5 = pickle.load(fobj)
    # 将新增的文件和改动的文件备份
    tar = tarfile.open(filename, 'w:gz')
    for key in md5dict:
        # if key not in old_md5 or md5dict[key] != old_md5[key]:
        if old_md5.get(key) != md5dict[key]:
            tar.add(key)
    tar.close()

    # 更新md5值
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)


if __name__ == '__main__':
    src = '/tmp/security'
    dest = '/tmp/backup'
    md5file = '/tmp/md5.data'
    if strftime('%a') == 'Mon':
        full_back(src, dest, md5file)
    else:
        free_back(src, dest, md5file)
```

### OOP基础

OOP介绍

基本概念

- 类（class）：用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每一对象所共有的属性和方法。对象是类的实例。
- 实例化：创建一个类的实例，类的具体对象
- 方法：类中定义的函数
- 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法

创建一个类

- 使用class语句来创建一个新类，class之后为类的名称并以冒号结尾
- 类名建议使用驼峰形式

```python
class BearToy:
    pass
```

创建实例

- 类是蓝图，实例是根据蓝图创建出来的具体对象

```python
tidy = BearToy()
```

绑定方法

构造器方法

- 当实例化类的对象是，构造器方法默认自动调用
- 实例本身作为第一个参数，传递给self

```python
class OOP:
    def __init__(self, size, color):
        self.size = size
        self.color = color


if __name__ == '__main__':
    tidy = OOP('small', 'orange')
    print(tidy.color)
    print(tidy.size)
```

其他绑定方法

- 类中定义的方法需要绑定在具体的实例。有实例调用
- 实例方法需要明确调用

```python
class OOP:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def speak(self):
        print('hahaha')


if __name__ == '__main__':
    tidy = OOP('small', 'orange')
    print(tidy.color)
    print(tidy.size)
    tidy.speak()
```

角色

```python
class Role:
    def __init__(self, name, wapon):
        self.name = name
        self.wapon = wapon

    def attack(self, target):
        print('我是%s，真正攻击%s' % (self.name, target))


if __name__ == '__main__':
    lb = Role('吕布', '方天画戟')
    lb.attack('张飞')
```

### 组合和派生

- 类被定义后，目标就是要把它当成一个模块来使用，并把这些对象嵌入到你的代码中
- 组合就是让不同的类混合并加入到其他类中来增加功能和代码重用性
- 可以在一个大点的类中创建其他类的实例，实现一些其它属性和方法来增强对原来的类对象

组合应用

- 两个类明显不同
- 一个类是另一个类的组件

```python
class Role:
    def __init__(self, name, wapon):
        self.name = name
        self.wapon = wapon

    def attack(self, target):
        print('我是%s，真正攻击%s' % (self.name, target))


if __name__ == '__main__':
    lb = Role('吕布', '方天画戟')
    lb.attack('张飞')
```

创建子类

- 当类之间有显著的不同，并且较小的类是较大的类所需的组件时组合表现得很好；但当设计”相同的类但有一些不同的功能“时，派生就是一个更加合理的选择了
- OOP的更强大方面之一时能够使用一个已经定义好的类，扩展它或者对其进行修改，而不会影响系统中使用现存类的其他代码片段
- OOD(面向对象设计)允许类特征在子孙类或者子类中进行继承

- 创建子类自需要在圆括号中写明从哪个父类继承即可

```python
class Role:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def show_me(self):
        print('我是%s,使用%s' % (self.name, self.weapon))


class Warrior(Role):
    pass


class Mage(Role):
    pass


if __name__ == '__main__':
    lb = Warrior('吕布', '方天画戟')
    lb.show_me()
```

继承

- 继承描述了基类的属性如何”遗传“给派生类
- 子类可以继承它的基类的任何属性，不管是数据属性还是方法

```python
class Role:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def show_me(self):
        print('我是%s,使用%s' % (self.name, self.weapon))


class Warrior(Role):
    def attack(self):
        print('千军万马一将在，探囊取物有何难')


class Mage(Role):
    pass


if __name__ == '__main__':
    lb = Warrior('吕布', '方天画戟')
    lb.show_me()
    lb.attack()
```

通过继承覆盖方法

- 如果子类中有和父类同名的方法，父类方法将被覆盖
- 如果需要访问父类的方法，则要调用一个未绑定的父类方法，明确给子类的实例

```python
class Role:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def show_me(self):
        print('我是%s,使用%s' % (self.name, self.weapon))


class Warrior(Role):
    def __init__(self, name, weapon, ride):
        # Role.__init__(self, name, weapon)
        super(Warrior,self).__init__(name,weapon)
        self.ride = ride
        # self.name = name
        # self.weapon = weapon
        # self.ride = ride

    def attack(self):
        print('千军万马一将在，探囊取物有何难')


class Mage(Role):
    def __init__(self, name, weapon, ride):
        self.name = name
        self.weapon = weapon
        self.ride = ride


if __name__ == '__main__':
    lb = Warrior('吕布', '方天画戟')
    lb.show_me()
    lb.attack()
```

多重继承

- python允许多重继承，即一个类可以是多个父类的子类，子类可以拥有所有父类的属性
- 自下向上，自左向右

```python
class A:
    def foo(self):
        print('foo')


class B:
    def bar(self):
        print('bar')


class C(A, B):
    pass


c = C()
c.foo()
c.bar()
```

### 类的特殊方法

魔法方法

magic基础

- 在python中，所有”__“下划线包起来的方法，都统称为”Magic Method“
- 如果对象实现（重载）了这些魔法方法中的某一个，那么这个方法就会在特殊的情况下被python调用
- 通过dir()可以查看对象的全部属性

```python
class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other

    def __radd__(self, other):
        return self.num + other

    def __sub__(self, other):
        return self.num - other

    def __rsub__(self, other):
        return self.num - other


if __name__ == '__main__':
    n = Number(4)
    print(n + 1)
    print(1 + n)
    print(n - 2)
    print(2 - n)
    print(n.num + 1)
```

__init__方法

- 实例化实例时默认会调用的方法

__str__方法

- 打印/显示实例时调用方法
- 返回字符串

```python
class Number:
    def __init__(self, num, size):
        self.num = num
        self.size = size

    def __str__(self):
        return "%s" % self.num


if __name__ == '__main__':
    n = Number(4, 3)
    print(n)
```

__call__方法

- 用于创建可调用的实例

```python
class Number:
    def __init__(self, num, size):
        self.num = num
        self.size = size

    def __str__(self):
        return "%s" % self.num

    def __call__(self, *args, **kwargs):
        print('%s' % self.num)


if __name__ == '__main__':
    n = Number(4, 3)
    print(n)
    n()
```

图书管理

```python
class Book:
    def __init__(self, name, ye, stu):
        self.name = name
        self.ye = ye
        self.stu = stu

    def __str__(self):
        return "《%s》" % self.name

    def __call__(self, *args, **kwargs):
        print('《%s》是由%s编写的' % (self.name, self.stu))


if __name__ == '__main__':
    n = Book('清明上河图', 1550, '刘仲元')
    print(n)
    n()
```

### 正则表达式及re模块

正则表达式

匹配单个字符

| 记号          | 说明                                      |
| ------------- | ----------------------------------------- |
| .             | 匹配任意字符（换行符除外）                |
| [....x-y...]  | 匹配字符组里的任意字符                    |
| [^....x-y...] | 匹配不在字符组里的任意字符                |
| \d            | 匹配任意数字，于【0-9】同义               |
| \w            | 匹配任意数字字母字符，于【0-9a-zA-Z】同义 |
| \s            | 匹配空白字符，于【\r\v\f\t\n】同义        |

匹配一组字符

| 记号     | 说明                     |
| -------- | ------------------------ |
| literal  | 匹配字符串的值           |
| re1\|re2 | 匹配正则表达式re1或者re2 |
| *        |                          |
| +        |                          |
| ?        |                          |
| {m,n}    |                          |

其他元字符

| 记号 | 说明             |
| ---- | ---------------- |
| ^    | 匹配字符串的开始 |
| $    | 匹配字符串的结尾 |
| \b   | 匹配单词的边界   |
| ()   | 对正则表达式分组 |
| \nn  | 匹配已保存的子组 |

match函数

- 尝试用正则表达式模式从字符串的开头匹配，如果匹配成功，则返回一个匹配对象；否则返回None

```python
import re

m = re.match('foo', 'food')
print(m)
m = re.match('foo', 'seafood')
print(m)
```

search函数

- 在字符中查找正则表达式模式第一次出现，如果匹配成功，则返回一个匹配对象；否则返回None

```python
import re

m = re.search('foo', 'food')
print(m)
m = re.search('foo', 'seafood')
print(m)
```

group方法

- 使用match或search匹配成功后，返回的匹配对象可以通过group方法获得匹配内容

```python
import re

m = re.search('foo', 'food')
print(m.group())
m = re.search('foo', 'seafood')
print(m.group())
```

findall函数

- 在字符串查找正则表达式模式的所有（非重复）出现；返回一个匹配对象的列表

```python
import re

m = re.search('foo', 'food')
print(m.group())
m = re.findall('foo', 'seafood is food')
print(m)
```

split方法

- 根据正则表达式中的分隔符把字符分割为一个列表，并返回成功匹配的列表
- 字符串也有类似的方法，但是正则表达式更灵活

```python
import re

m = re.split('\.|-', 'hello-world.data')
print(m)
```

sub

- 把字符串中所有匹配正则表达式的地方替换成新的字符串

```python
import re

m = re.sub('X', 'Mr.Smith', 'attn:X\nDear X')
print(m)
```

compile函数

- 对正则表达式模式进行编译，返回一个正则表达式对象
- 不是必须要用这种方式，但是在大量匹配的情况下，可以提升效率

```python
import re

patt = re.compile('foo')
m = patt.search('food is food')
print(m.group())
```

### 正则表达式案例

日志分析

```python

```

### Python模块安装

PYPI

- PYPI即PYthon Package Index
- 是python官方的第三方库，所有人都可以下载或上传Python库到PYPI
- 官方站点为https://pypi.org

本地安装pip

- pip是python包管理工具
- 提供了对python包的查找，下载，安装，卸载的功能
- 下载pip后解压并安装

```shell
tar -xf pip.tar.gz
cd pip
python setup,py install
```

在线安装模块

- 为了实现安装加速，可以设置pip安装时采用国内镜像站点

```python
mkdir ~/.pip
vim ~/.pip/pip.conf
[global]
index-url=http://pypi.douban.com/simple/
[install]
trusted-host=pypi.douban.com
```

配置pip支持tab键补全

- pip命令默认不支持tab键提示
- 配置pip支持tab键补全的方法如下

```python
pip completion --bash >>~/.bash_profile
source ~/.bash_profile
```

查看软件包版本

- pip在线安装软件包时，默认安装最新版本
- 查看软件包版本，安装指定版本方式如下

```python
C:\Users\ycc>pip install wget==
WARNING: Ignoring invalid distribution -ip (d:\python\lib\site-packages)
WARNING: Ignoring invalid distribution -ip (d:\python\lib\site-packages)
Looking in indexes: http://pypi.douban.com/simple
ERROR: Could not find a version that satisfies the requirement wget== (from versions: 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 2.0, 2.1, 2.2, 3.0, 3.1, 3.2)
ERROR: No matching distribution found for wget==
```

### 准备数据库

### PyMySQL模块应用

### SQLAIchemy概述

### 数据库对象管理

### SQLAIchemy应用

# DevOps

### 多进程概述

forking工作原理

什么是forking

- fork（分岔）在Linux系统中使用非常广泛
- 当某一命令执行时，父进程（当前进程）fork出一个子进程
- 父进程将自身资源拷贝一份，命令在子进程中运行时，就具有和父进程完全一样的运行环境

进程的生命周期

- 父进程fork出子进程并挂起
- 子进程运行完毕后，释放大部分资源并通知父进程，这个时候子进程被称作僵尸僵尸
- 父进程获知子进程结束，子进程所有资源释放

```python
import subprocess


def ping(host):
    result = subprocess.run('ping -n 1 %s' % host, shell=True)
    if result.returncode == 0:
        print('%s通了' % host)
    else:
        print(host)


if __name__ == '__main__':
    ips = ['192.168.1.%s' % i for i in range(1, 255)]
    for ip in ips:
        ping(ip)
```

forking编程

forking编程基本思路

- 需要使用os模块
- os.fork()函数实现forking功能
- python中，绝大多数的函数只返回一次，os.fork将返回两次
- 对fork()调用，针对父进程返回子进程的PID；对于子进程，返回PID0

```python
import os

print('sting..')
ret_va = os.fork()
if ret_va:
    print('hello world!')
else:
    print('ssssssssssss')
```

### 多进程应用

- 父进程负责生成子进程
- 子进程做具体的工作
- 子进程结束后彻底退出

```python
import os
import time

print('starting...')
ret_val = os.fork()
if ret_val:
    print('in parent')
    time.sleep(10)
    print('parent exit')
else:
    print('in chile')
    for i in range(1, 11):
        print(i)
        time.sleep(1)
    print('child exit')
```

ping_fork

```python
import os
import subprocess


def ping(host):
    result = subprocess.run('ping -c1 W1 %s &>/dev/null' % host, shell=True)
    if result.returncode == 0:
        print('%s:up' % host)
    else:
        print('%s:down' % host)


if __name__ == '__main__':
    ips = ['192.168.10.%s' % i for i in range(1, 255)]
    for ip in ips:
        ret_val = os.fork()
        if not ret_val:
            ping(ip)
            exit()
```

僵尸进程

- 僵尸进程没有任何可执行代码，也不能被调度
- 如果系统中存在过多的僵尸进程，将因为没有可用的进程号而导致系统不能产生新的进程
- 对系统管理员来说，可以试图杀死其父进程或重启系统来消除僵尸进程

```python
import os
import time

print('starting')
ret_val = os.fork()
if ret_val:
    print('in parent')
    time.sleep(30)
    print('parent done')
else:
    print('in child')
    time.sleep(15)
    print('child done')
```

解决zombie问题

- 父进程通过os.wait()来得到子进程是否终止的信息
- 在子进程终止和父进程调用wait()之间的这段时间，子进程被称为zombie(僵尸)进程
- 如果子进程还没有终止，父进程先退出了，那么子进程会持续工作。系统自动将子进程的父进程设置为init进程，init来将来负责清理僵尸进程
- python可以使用waitpid()来处理子进程
- waitpid()接受两个参数，第一个参数设置为-1，表示于wait()函数相同；第二个参数如果设置为0表示挂起父进程，直到子程序退出，设置1表示不挂起父进程
- waitpid()返回值：如果子进程尚未结束则返回0，否则返回子进程PID

```python
import os
import time

print('starting')
ret_val = os.fork()
if ret_val:
    print('in parent')
    # result = os.waitpid(-1, 0) # 挂起父进程
    result = os.waitpid(-1, 1)		# 不挂起父进程
    print(result)   # result是元组：（子进程pid,0）或(0,0)
    time.sleep(3)
    print('parent done')
else:
    print('in child')
    time.sleep(50)
    print('child done')

```

### 多线程应用

多线程的动机

- 在多线程（MT）编程出现之前，电脑程序是运行有一个执行顺序组成，执行序列按顺序在主机的中央处理器（CPU）中运行
- 无论是任务本身要求顺序执行还是整个程序是由多个子任务组成，程序都是按这种方式执行的
- 即使子任务相互独立，互相无关（即，一个子任务的结果不影响其他子任务的结果）时也是这样
- 如果并行运行这些相互独立的子任务可以大幅度地提升整个任务的效率

什么是进程

- 计算机程序只不过是磁盘中可执行的，二进制的数据
- 进程（有时被称为重量级进程）是程序的一次执行
- 每个进程都有自己的地址空间，内存以及其它记录其运行轨迹的辅助数据
- 操作系统管理在其上运行的所有数据，并为这些进程公平地分配时间

什么是线程

- 线程（有时被称为轻量级进程）跟进程有些相似。不同的是，所有的线程运行在同一个进程中，共享相同的运行环境
- 一个进程中各个线程之间共享同一片数据空间，所以线程之间可以比进程之间更方便地共享数据以及相互通讯

```python
# 主线程只负责生成工作线程
# 工作线程做具体的工作
import threading


def say_hi():
    print('hello World!')


if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=say_hi)
        t.start()
```

线程相关模块

- thread和threading模块允许程序员创建和管理线程
- thread模块供了基本的线程和锁的支持，而threading提供了跟高级别，功能更强的线程管理功能
- 推荐使用更高级别的threading模块

```python
# 主线程只负责生成工作线程
# 工作线程做具体的工作
import threading


def say_hi(word):
    print('hello %s!' % word)


if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=say_hi, args=('tedu',))
        t.start()
```

传递函数给Thread类

- 多线程编程有多种方法，传递函数给threading模块的Thread类是介绍的第一种方法
- Thread对象使用start()方法开始线程的执行，使用join()方法挂起程序，直到线程结束

```python
import os
import subprocess
import threading


def ping(host):
    result = subprocess.run('ping -c1 -W1 %s &>/dev/null' % host, shell=True)
    if result.returncode == 0:
        print('%s:up' % host)
    else:
        print('%s:down' % host)


if __name__ == '__main__':
    ips = ['192.168.10.%s' % i for i in range(1, 255)]
    for ip in ips:
        t = threading.Thread(target=ping,args=(ip,))
        t.start()
```

传递可调用类给Thread类

- 传递可调用给Thread类是介绍的第二种方法
- 相对于一个或几个函数来说，由于类对象里可以使用类的强大的功能，可以保存更多的信息，这种方法更为灵活

```python
import os
import subprocess
import threading


class Ping:
    def ping(self, host):
        result = subprocess.run('ping -c1 -W1  %s &>/dev/null' % host, shell=True)
        if result.returncode == 0:
            print('%s:up' % host)
        else:
            print('%s:down' % host)


if __name__ == '__main__':
    ips = ['172.16.10.%s' % i for i in range(1, 255)]
    for ip in ips:
        t = threading.Thread(target=Ping().ping, args=(ip,))
        t.start()
```

```python
import os
import subprocess
import threading


class Ping:
    def __call__(self, host):
        result = subprocess.run('ping -c1  -W1 %s &>/dev/null' % host, shell=True)
        if result.returncode == 0:
            print('%s:up' % host)
        else:
            print('%s:down' % host)


if __name__ == '__main__':
    ips = ['172.16.10.%s' % i for i in range(1, 255)]
    for ip in ips:
        t = threading.Thread(target=Ping(), args=(ip,))
        t.start()
```

```python
import os
import subprocess
import threading


class Ping:

    def __init__(self, host):
        self.host = host

    def __call__(self):
        result = subprocess.run('ping -c1  -W1 %s &>/dev/null' % self.host, shell=True)
        if result.returncode == 0:
            print('%s:up' % self.host)
        else:
            print('%s:down' % self.host)


if __name__ == '__main__':
    ips = ['172.16.10.%s' % i for i in range(1, 255)]
    for ip in ips:
        t = threading.Thread(target=Ping(ip))
        t.start()
```

### urllib模块概述

urllib简介

- 在Python2版本中，有urllib和urllib2两个库可以用来实现request的发送。而在Python3中，已经不存在urllib2这个库了，统一为urllib

- urllib中包括了四个模块
  1. urllib.request可以用来发送request和获取request的结果
  2. urllib.error包含了urllib.request产生的异常
  3. urllib.parse用来解析和处理URL
  4. urllib.robotparse用来解析页面的robots.txt文件

爬取网页

- 先需要导入用到的模块：urllib.request
- 在导入了模块之后，我们需要使用urllib.request.urlopen打开并爬取一个网页
- 读取内容常见有3种方式：
  1. read()读取文件的全部内容，于readlines()不同的是，read()会读取到的内容赋给一个字符串变量
  2. readlines()读取文件的全部内容，readlines()会把读取到的内容赋值给一个列表变量
  3. readline()读取文件的一行内容

```python
from urllib import request

html = request.urlopen('http://www.baidu.com')
with open('a.html', 'wb') as fobj:
    fobj.write(html.read())
```

```python
import urllib.request
html = urllib.request.urlopen('http://www.baidu.com')
print(html.readline())
print(html.read(4096))
print(html.readlines())
```

```python
import urllib.request

url = 'https://img1.baidu.com/it/u=2496571732,442429806&fm=26&fmt=auto&gp=0.jpg'
html = urllib.request.urlopen(url)
with open('a.jpg', 'wb') as fobj:
    fobj.write(html.read())
```

网络资源下载

- urllib不仅可以下载网页，其他网络资源均可下载
- 有些文件比较大，需要像读取文件一样，每次读取一部分数据

```python
import urllib.request

url = 'http://sthjj.km.gov.cn/upload/resources/file/2018/11/28/2868835.pdf'
html = urllib.request.urlopen(url)
with open('tupa.pdf', 'wb') as fobj:
    while 1:
        data = html.read(4096)
        if not data:
            break
        fobj.write(data)
```

wget

```python
import wget

wget.download('http://sthjj.km.gov.cn/upload/resources/file/2018/11/28/2868835.pdf', 'a.pdf')
```

```python
#!D:\Python\Python.exe
import wget
import os
import re


def get_url(filename, patt):
    result = []
    cpatt = re.compile(patt)
    with open(filename) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                result.append(m.group())
    return result


if __name__ == '__main__':
    path = 'image'
    filename = 'image/cntcvc.html'
    url = 'https://www.163.com'
    if not os.path.exists(path):
        os.mkdir(path)
    if not os.path.exists(filename):
        wget.download(url, filename)

    url_patt = '(http|https)://[\w.-/]+\.(jpg|jpeg|png|gif)'
    img_list = get_url(filename, url_patt)
    # print(img_list)
    for img in img_list:
        wget.download(img, path)
```

### urllib应用



### paramiko模块应用

安装paramiko模块

- 本地安装

```python
yum -y install gcc gcc-c++ python-devel
tar -xf paramiko.tar.gz
pyhton setup.py install
```

- 网络安装

```python
pip install paramiko
```

基础使用介绍

- sshClient

  1. 创建用于连接ssh服务器的实例

     ```python
     ssh = paramiko.SSHClinet()
     ```

- paramiko.autoaddpolicy
  1. 设置自动添加主机密钥
- ssh.connect
  1. 连接ssh服务器
- ssh.exec.comand
  1. 在ssh服务器上执行指定命令

实例

- 编写用于实现ssh访问的脚本
  1. 创建SSHClient实例
  2. 设置添加主机密钥策略
  3. 连接ssh服务器
  4. 执行指令命令
  5. 在shell命令行中接受用于连接服务器的密码以及在远程主机上执行的命令

```python
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.16.10.25', username='root', password='1qaz!QAZ')
result = ssh.exec_command('id root')
print(result)
#print(result[0].read())
print(result[1].read().decode())
print(result[2].read().decode())
ssh.close()
```

多线程主机远程管理

```python
import paramiko
import os
import sys
import getpass
import threading


def rcmd(host, user, passwd, port=22, cmds=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=passwd)
    stdint, stdout, stderr = ssh.exec_command(cmds)
    out = stdout.read()
    err = stderr.read()
    if out:
        print('[%s] OUT:\n%s' % (host, out.decode()))
    if err:
        print('[%s] ERR:\n%s' % (host, err.decode()))
    ssh.close()


if __name__ == '__main__':
    # rcmd('172.16.10.25', 'root', '1qaz!QAZ', cmds='id root')
    if len(sys.argv) != 3:
        print('Usage: %s ipfile "commands"' % sys.argv[0])
        exit(1)
    if not os.path.isfile(sys.argv[1]):
        print('No such file', sys.argv[1])
        exit(2)
    ipfile = sys.argv[1]
    passwd = getpass.getpass()
    cmds = sys.argv[2]
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()
            t = threading.Thread(target=rcmd, args=(ip, 'root', '1qaz!QAZ', 22, cmds))
            t.start()
```

### 邮件编程

### JSON

### requests基础

### 钉钉机器人案例

### zabbix APi概述

### zabbix编程

# Django

