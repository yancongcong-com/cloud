# 	Shell

# 什么是自动化

# 自动化可以干什么

1. 自动化批量系统，初始化程序（update,软件安装，时区设置，安全策略）
2. 自动化批量软件部署程序（LAMP，LNMP，Tomcat,LVS,Nginx）
3. 管理应用程序（KVM，集群管理扩容，MYSQL）
4. 日志分析处理程序（PV，UV）
5. 自动化备份恢复程序
6. 自动化信息采集及监控程序（收集系统，应用状态信息）
7. 自动化管理程序
8. 自动化扩容（增加云主机--->业务上线）

## 用户登录

- su - user

  ```shell
  /etc/profile
  /etc/bashrc
  ~/.bash_profile
  ~/.bashrc
  ```

- su  user

  ```shell
  /etc/bashrc
  ~/.bashrc
  ```

### 用户离开

- ~/.bash_logout
- ~/.bash_history

## Shell脚本格式

### 脚本运行

```shell
#直接运行需要执行权限
./
#解释器调用
bash
```

## bash的特性

1. 命令补全
2. 命令历史记忆功能
3. 别名功能
4. 常用快捷键
5. 前后台作业控制
6. 输入输出重定向
7. 管道
8. 命令排序
9. shell通配符
   - *任意多个字符
   - ？任意单个字符
   - []
   - ()
   - {}
   - /
10. echo输出颜色，printf格式化输出文本

### 系统环境变量

1. 自定义变量

   ```shell
   定义变量：变量名=变量值 #区分大小写
   引用变量：$变量名 ${#变量名}
   查看变量：echo “$变量名” echo ${变量名}
   取消变量：unset变量
   作用范围：仅在当前shell中有效
   #示例
   vim /etc/profile
   export PATH=$PATH:/test/bin
   ```

2. 定义环境变量：export 变量 

   ```shell
   定义：export
   应用：$变量名
   查看：env
   取消：unset
   范围：在当前shell和子shell有效
   ```

3. 位置变量

   ```shell
   $1  ${10}
   ```

4. 预定义变量

   ```shell
   $0 脚本名
   $* 所有的参数
   $@ 所有的参数
   $# 参数的个数
   $$ 当前进程的 PID
   $! 上一个后台进程的 PID
   $? 上一个命令的返回值 0 表示成功
   文件名 basename 
   ```

   

### 变量传递

source ./变量文件

### 变量赋值

- 显示赋值

## 变量赋值运算

### 整数运算

```shell
expr + - \* / %
$(())
$[]
let sum=2+3
```

### 小数运算

```shell
echo "1+2" |bc 加减乘
echo "scale=2;5 / 2"|bc
```

### 变量删除和替换

```shell
echo ${var}		#变量显示	
echo ${#var}	#变量长度
echo ${var#*.}	#变量从前往后删除到第一个点
echo ${var##*.}	#变量从前往后删除到最后一个点
echo ${var%.*}	#变量从后往前删除到第一个点
echo ${var%%.*}	#变量从后往前删除到最后一个点
echo ${var:x:y}	#变量从x开始取y个 没有y就是到完
#变量替换
echo ${var/x/y}	#变量中第一个x替换成y
echo ${var//x/y}#变量中所有x替换成y
#变量替代
echo ${var-aaa} #如果变量没有定义过，aaa替代
echo ${var:-aaa}#如果变量没有值，aaa替代
```

### i++ ++i

```shell
先赋值在自增
```

### 特殊符号

```shell
()		#子shell中执行
(())	#数值比较，C语言风格
$()		#命令替换
$(())	#整数运算
{}		#集合
${}		#变量显示
[]		#条件测试
[[]]	#条件测试，正则
$[]		#整数运算
```

### 执行脚本

```shell
./shell.sh		#需要执行权限		在子shell中执行
bash shell.sh	#不需要执行权限   	在子shell中执行
.shell.sh		#不需要执行权限	在当前shell中执行
source shell.sh	#不需要执行权限	在当前shell中执行
```

> 提示：通常修改系统配置文件中如：/etc/profile的PATH等变量后，使之在当前shell中生效

### 调试脚本

```shell
sh -n shell.sh	#仅调试 syntax error
sh -vx shell.sh	#以调试的方式执行，查询整个执行过程
```

#### 输出字体

```shell
#字体色范围：30-37  
echo -e "\033[30m 黑色字 \033[0m"  
echo -e "\033[31m 红色字 \033[0m"  
echo -e "\033[32m 绿色字 \033[0m"  
echo -e "\033[33m 黄色字 \033[0m"  
echo -e "\033[34m 蓝色字 \033[0m"  
echo -e "\033[35m 紫色字 \033[0m"  
echo -e "\033[36m 天蓝字 \033[0m"  
echo -e "\033[37m 白色字 \033[0m"  
#字背景颜色范围：40-47  
echo -e "\033[40;37m 黑底白字 \033[0m"  
echo -e "\033[41;30m 红底黑字 \033[0m"  
echo -e "\033[42;34m 绿底蓝字 \033[0m"  
echo -e "\033[43;34m 黄底蓝字 \033[0m"  
echo -e "\033[44;30m 蓝底黑字 \033[0m"  
echo -e "\033[45;30m 紫底黑字 \033[0m"  
echo -e "\033[46;30m 天蓝底黑字 \033[0m"  
echo -e "\033[47;34m 白底蓝字 \033[0m"  
```



## 条件测试

- 文件测试
- 数值比较
- 字符串比较

```shell
格式1：test 条件表达式
格式2：[ 条件测试 ]
格式3：[[ 条件测试 ]]
       EXPRESSION1 -a EXPRESSION2
              both EXPRESSION1 and EXPRESSION2 are true
       EXPRESSION1 -o EXPRESSION2
              either EXPRESSION1 or EXPRESSION2 is true
       -n STRING
              the length of STRING is nonzero
       STRING equivalent to -n STRING
       -z STRING
              the length of STRING is zero
       STRING1 = STRING2
              the strings are equal
       STRING1 != STRING2
              the strings are not equal
       INTEGER1 -eq INTEGER2
              INTEGER1 is equal to INTEGER2
       INTEGER1 -ge INTEGER2
              INTEGER1 is greater than or equal to INTEGER2
       INTEGER1 -gt INTEGER2
              INTEGER1 is greater than INTEGER2
       INTEGER1 -le INTEGER2
              INTEGER1 is less than or equal to INTEGER2
       INTEGER1 -lt INTEGER2
              INTEGER1 is less than INTEGER2
       INTEGER1 -ne INTEGER2
              INTEGER1 is not equal to INTEGER2
       FILE1 -ef FILE2
              FILE1 and FILE2 have the same device and inode numbers
       FILE1 -nt FILE2
              FILE1 is newer (modification date) than FILE2
       FILE1 -ot FILE2
              FILE1 is older than FILE2
       -b FILE
              FILE exists and is block special
       -c FILE
              FILE exists and is character special
              FILE exists and is character special
       -d FILE
              FILE exists and is a directory
       -e FILE
              FILE exists
       -f FILE
              FILE exists and is a regular file
       -g FILE
              FILE exists and is set-group-ID
       -G FILE
              FILE exists and is owned by the effective group ID
       -h FILE
              FILE exists and is a symbolic link (same as -L)
       -k FILE
              FILE exists and has its sticky bit set
       -L FILE
              FILE exists and is a symbolic link (same as -h)
       -O FILE
              FILE exists and is owned by the effective user ID
       -p FILE
              FILE exists and is a named pipe
       -r FILE
              FILE exists and read permission is granted
       -s FILE
              FILE exists and has a size greater than zero
       -S FILE
              FILE exists and is a socket
       -t FD  file descriptor FD is opened on a terminal
       -u FILE
              FILE exists and its set-user-ID bit is set
       -w FILE
              FILE exists and write permission is granted
       -x FILE
              FILE exists and execute (or search) permission is granted
```
```shell
[ 1 -lt 2 -a 5 -gt 10];echo $?
[ 1 -lt 2 -o 5 -gt 10];echo $?
[[ 1 -lt 2 && 5 -gt 10]];echo $?
[[ 1 -lt 2 || 5 -gt 10]];echo $?
```



> ***字符串比较使用   " ".***  变量未定义或者为空都是0

```shell
read -p "please user name: " user
id $user &>/dev/null && echo "user exists"|| (useradd $user && echo "user $user success")
```

```shell
read -p "please user name: " user
#if 后面可以跟任何语句
if id $user &>/dev/null;then
        echo "user $user exists"
else
        useradd $user
        if [ $? -eq 0 ];then
                echo "$user success"
        fi
fi
```

磁盘空间

```shell
disk_use=$(df -Th |grep '/$'| awk '{print $(NF-1)}'|awk -F"%" '{print $1}')
if [ $disk_use -ge 90 ];then
	echo "`data +%F-%H`"
fi
```

> 邮件：echo "please example" |mail -s 'root' root

内存空间

```shell
mem_used=`free -m |grep '^Mem'|awk '{print $3}'`
mem_total=`free -m |grep '^Mem'|awk '{print $2}'`
mem_percent=$((mem_used*100/mem_total))
war_file=/tmp/mem.war.txt
rm -rf $war_file
if [ $mem_percent -ge 80 ];then
	echo "Out of available memory"
	echo "`date +%F-%H` memory:${mem_percent}%" > $war_file
fi
if [ -f $war_file ];then
	mail -s "mem war..." ycc <$war_file
	rm -rf $war_file
fi
```

用户创建

> {1...$num} ???

```shell
#!/usr/bin/bash
#useradd
#v1.0 by ycc
while :
do
read -p "Please input number: " num
        if [[ ! "$num" =~ ^[0-9]+$ || "$num" =~ ^0+$ ]];then
                echo "error number!"
        else
                break
        fi
done
while :
do
read -p "Please input prefix: " prefix
        if [ -z "$prefix" ];then
                echo "prefix error"
        else
                break
        fi
done
for i in `seq $num`
do
        user=$prefix$i
        useradd $user
        echo "${prefix}123" |passwd --stdin $user
        if [ $? -eq 0 ];then
                echo "$user is created."
        fi
done
```

> seq 起始，步长，结束 

Mysql备份

```shell
Mysql_Dump=/usr/bin/mysqldump
User=root
Pass=1
Data=ycc
Backup_Dir=/backup
Date=$(data +%F)
Backup_Path=$Backup_Dir/$Date
test -d $Backup_Path || mkdir -p $Backup_Path
if [ $? -eq 0 ];then
	echo "-------Backup is String-----"
	$Mysql_Dump -u$User -p$Pass -B $Data >$Backup_Path/mysql_db.sql
	if [ $? -eq 0 ];then
		echo “------mysql done-----”
	fi
fi
```

系统负载

```shell
load=$(w |head -1|awk -F'.' '{print $1}' |awk -F':' '{print $5}')
if [ $load -ge 1];then
	echo -e "Err"
else
	echo -e "ok"
fi
```

用户删除

```shell
#!/usr/bin/bash
read -p "Please input username: " user
id $user >/dev/null
if [ $? -ne 0 ];then
	echo "no such user $user"
	exit 1
fi
read -p "Are you sure?[y/n]: " action
case "$action" in
y|Y|yes|YES)
	useradd -r $user
	echo "$user is deleted!"
	;;
*)
	echo "error delete!"
esac
```









## bash -vx

### 用户输入

```shell
read -p “提示”  变量名
read -t 自动推出
read 多个变量名空格拆分
read -n 2 两个字符
```

> 引号:强引号'',弱引号“”，变量解析。

### shell判断

```shell
#!/usr/bin/bash
if [ ];then
fi
```



