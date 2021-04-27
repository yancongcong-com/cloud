# 	Shell脚本

1. 自动化批量系统，初始化程序（update,软件安装，时区设置，安全策略）
2. 自动化批量软件部署程序（LAMP，LNMP，Tomcat,LVS,Nginx）
3. 管理应用程序（KVM，集群管理扩容，MYSQL）
4. 日志分析处理程序（PV，UV）
5. 自动化备份恢复程序
6. 自动化信息采集及监控程序（收集系统，应用状态信息）
7. 自动化管理程序
8. 自动化扩容（增加云主机--->业务上线）

## 登录shell

### 用户登录

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

### bash的特性

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

### 变量赋值运算

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

### 输出字体

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

安装不版本yum源

```shell
os_version=$(hostnamectl  |grep System|awk '{print $5}')
wget=$(yum -y install wget)
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
case $os_version in
7)
	curl -o /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo
	$wget
	wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
	;;
8)
	curl -o /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-8.repo
	$wget
	yum install -y https://mirrors.aliyun.com/epel/epel-release-latest-8.noarch.rpm
	sed -i 's|^#baseurl=https://download.fedoraproject.org/pub|baseurl=https://mirrors.aliyun.com|' /etc/yum.repos.d/epel*
sed -i 's|^metalink|#metalink|' /etc/yum.repos.d/epel*
	;;
6)
	curl -o /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-6.repo
	$wget
	wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-6.repo
	;;
*)
	echo "Unknown system"
esac
```

信号

```shell
信号名称	信号数	描述
SIGINT	2	程序终止(interrupt)信号, 在用户键入INTR字符(通常是Ctrl+C)时发出。
SIGQUIT	3	和SIGINT类似, 但由QUIT字符(通常是Ctrl /)来控制. 进程在因收到SIGQUIT退出时会产生core文件, 在这个意义上类似于一个程序错误信号。
SIGFPE	8	在发生致命的算术运算错误时发出. 不仅包括浮点运算错误, 还包括溢出及除数为0等其它所有的算术的错误。
SIGKILL	9	用来立即结束程序的运行. 本信号不能被阻塞, 处理和忽略。
SIGALRM	14	时钟定时信号, 计算的是实际的时间或时钟时间. alarm函数使用该信号。 SIGTERM
```

shell配置文件应用顺序

```shell
#登录式shell配置文件执行顺序
/etc/profile->/etc/profile.d/*.sh->~/.bash_profile->~/.bashrc->/etc/bashrc
#非登录式shell配置文件执行顺序
~/.bashrc->etc/bashrc->/etc/profile.d/*.sh
```

```shell
#!/usr/bin/bash
clear
echo "######################"
echo "#####1. install php5.5"
echo "#####2. install php5.6"
echo "#####3. install php7.0"
echo "######################"
read -p "please inupt install php version num: " num
if [[ ! $num =~ ^[0-9]+$ ]];then
        clear
        echo "not number"
        exit 1
fi

if [ $num -eq 1 ];then
        echo "install php5.5...."


elif [ $num -eq  2 ];then
        echo "install php5.6...."


elif [ $num -eq 3 ];then
        echo "install php7.0...."
fi
```

跳板机

```shell
#!/usr/bin/bash
clear
[ -f ~/.ssh/idrsa ] ||  ( ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa )
web1=172.16.10.22
web2=192.168.10.33
mysql=192.168.10.22
while :
do
        cat <<-EOF
        1. web1
        2. web2
        3. mysql
        EOF
        read -p "Please input number: " num
        case "$num" in
        1)
                ssh alice@${web1}
                ;;
        2)
                ssh alice@${web2}
                ;;
        3)
                ssh alicei@$mysql
                ;;
        "")
                ;;
        *)
                ;;
        esac
done
```

## 流程控制

if安装apache

```shell
gateway=$(ip r |head -1|awk '{print $3}')
dns=$(cat /etc/resolv.conf |grep nameserver |head -1 |awk '{print $2}')
myping(){
        ping $1 -c1 &>/dev/null
}
myping $gateway
echo "网关是：$gateway"
if [ $? -ne 0 ];then
        echo "网关不可达！"
        exit
fi
myping $dns
echo "DNS是：$dns"
if [ $? -ne 0 ];then
        echo "dns不可达！"
        exit
fi
read -p "请输出url,测试外网可达性[默认为www.baidu.com]：" extranet
extranet=${extranet:-www.baidu.com}
myping $extranet
if [ $? -ne 0 ];then
        echo "dns不可解析！"
        exit
fi
echo "完成"

```

安装apache

```shell
gateway=$(ip r |head -1|awk '{print $3}')
ping -c1 www.baidu.com &>/dev/null
if [ $? -eq 0];then
	yum -y install httpd
	systemctl start httpd
	systemctl enable httpd
	firewalld-cmd --permanent --add-service=http
	firewalld-cmd --permanent --add-service=https
	firewalld-cmd --reload
	sed -ri '' /etc/selinux/config
	setenforce 0
elif ping -c1 $gateway &>/dev/null;then
	echo "check dns.."
else
	echo "check ip address!"
fi
```

## 服务信息

```shell
#!/usr/bin/bash
server=vsftpd
rpm -q $server &>/dev/null
if [ $? -ne 0 ];then
        yum -y install $server &>/dev/null
fi

systemctl status $server &>/dev/null
if [ $? -eq 0 ];then
        netstat=$(ss -napt |grep vsftpd|awk '{print $4}')
        port=${netstat##*:}
        addr=${netstat%:*}
        pid=$( ss -antp |grep $server |awk -F'pid=' '{print $2}'|awk -F',' '{print $1}')
        echo "$server is running"
        echo "$server 监听端口是：$port"
        echo "$server 监听地址是：$addr"
        echo "$server pid是：$pid"
else
        systemctl start $server
        echo " $server no running"
fi
```

nginx启动

```shell
#!/usr/bin/bash
source /etc/init.d/functions
acl=$1
alert(){
        if [ $? -eq 0 ];then
                action "nginx is $acl" /bin/true
        else
                action "nginx is $acl" /bin/false
        fi
}

start(){
        ss -napt |grep nginx >/dev/null || /usr/sbin/nginx &>/dev/null
        alert 
}
stop(){
        /usr/sbin/nginx -s stop &>/dev/null
        alert
}

restart(){
        /usr/sbin/nginx -s stop >/dev/null;sleep 1 && /usr/sbin/nginx &>/dev/null
        alert
}

reload(){
        /usr/sbin/nginx -s reload
        alert
}

status(){
        server=nginx
        netstat=$(ss -napt4 |grep $server|awk '{print $4}')
        port=${netstat##*:}
        addr=${netstat%:*}
        pid=$( ss -antp4 |grep $server |awk -F'pid=' '{print $2}'|awk -F',' '{print $1}')
        [ "$pid" != "" ] && echo "$server is running" ||  echo "$server is stopping" 
        if [ "$pid" != ""  ];then        
        echo "$server 监听端口是：$port";
        echo "$server 监听地址是：$addr";
        echo "$server pid是：$pid"
        fi
        alert   


}

force-reload(){
        killall nginx &>/dev/null
        start
        alert
}

if [ "$1" = "start" ];then
        start
elif [ "$1" = "stop" ];then
        stop
elif [ "$1" = "restart" ];then
        restart
elif [ "$1" = "reload" ];then
        reload
elif [ "$1" = "status" ];then
        status
elif [ "$1" = "force-reload" ];then
        force-reload
else
        echo "Usage: $0 {start|stop|status|restart|force-reload}"
fi
```

## 循环

```shell
for特点：固定循环次数
{起始值..结束值}
seq 起始值 步长 结束值
#!/usr/bin/bash
for i in {1..254}
do
		{
        ip=172.16.10.$i
        ping -c1 -W1 $ip &>/dev/null
        if [ $? -eq 0 ];then
                echo "$ip" |tee -a ip.txt
        fi
        }&
done
wait #等待所有的后台进程完成
echo "finishi...."

time时间
```

```shell
#!/usr/bin/bash
for i in `cat ip.txt`
do
        ping -c1 -W2 $i &>/dev/null
        if [ $? -eq 0 ];then
                echo "$i is up"
        else
                echo "$i is down"
        fi
done
```

用户创建

```shell
while :
do
	read -p "Please enter prefix & pass &num: " prefix pass num
	printf "user information:
	-------------------------
	user prefix: $prefix
	user password: $pass
	user number: $num
	--------------------------
	"
	read -p "Are you sure?[y/n]: " action
	if [ "$action" = "y" -o "$cation" = "Y" -o "$cation" = "yes" -o "$cation" = "YES"];then
		break
	fi
done 
for i in `seq $num`
do
	id $prefix$i &>/dev/null
	if [ $? -eq 0 ];then
		echo "user $prefix$i already exists"
	else
		useradd $prefix$i
		echo $pass |passwd --stdin $prefix$i &>/dev/null
		if [ $? -eq 0 ];then
			echo "$user is created"
		fi
done
```
用户创建

> IFS内部分割符
>
> IFS=$'\n'
>
> IFS='
>
> '
>
> for跳过空行

```shell
#!/usr/bin/bash
if [  $# -eq 0 ];then
        echo "usage: `basename $0` file"
        exit 1
fi

if [ ! -f $1 ] ;then
        echo "error file"
        exit 2
fi
IFS=$'\n'
for line  in `cat $1`
do
		if [ ${#line} -eq 0 ];then
			continue
		fi
        user=`echo "$line" |awk '{print $1 }'`
        pass=`echo "$line" |awk '{print $2 }'`
        id $user &>/dev/null
        if [ $? -eq 0 ];then
                echo "user $user already exists"
        else
                useradd $user
                echo "$pass" |passwd --stdin $user &>/dev/null
                if [ $? -eq 0 ];then
                        echo "$user is created"
                fi
        fi
        
done
```

EXPECT

```shell
#!/usr/bin/expect
set ip [ lindex $argv 0 ]
set user root
set password 1qaz!QAZ
set timeout 5
spawn ssh $user@$ip

expect {
        "yes/no" { send yes\r exp_continue }
        "password:" { send $password\r }
}
#非交互
#interact
expect "#"
        send "useradd bb\r"
        send "pwd\r"
        send "exit\r"
expect eof


```

### 批量修改主机用户

```shell
#!/usr/bin/bash
>fail.txt
>ok.txt
date +%F
read -p "Please enter a New Password:  " pass
for ip in $(cat ip.txt)
do
        {
        ping -c1 -W1 $ip &>/dev/null
        if [ $? -eq 0 ];then
                ssh $ip "echo $pass |passwd --stdin root"
                if [ $? -eq 0 ];then
                        echo "$ip" >>ok.txt
                else
                        echo "$ip" >>fail.txt
                fi
        else
                echo "$ip" >>fail.txt
        fi
        }&
done
wait
```

ssh配置文件

```shell
#ssh连接时间长
UseDNS no
#!/usr/bin/bash
#!/usr/bin/bash
for ip in `cat ip.txt`
do
        {
        ping -c1 -W1 $ip &>/dev/null
        if [ $? -eq 0 ];then
                ssh $ip "sed -ri '/^#UseDNS/cUseDNS no' /etc/ssh/sshd_config"
                ssh $ip " sed -ri '/^GSSAPIAuthentication/cGSSAPIAuthentication no' /etc/ssh/sshd_config"
                ssh $ip "systemctl stop firewalld;systemctl disable firewalld"
                ssh $ip "sed -ri '/^SELINUX=/cSELINUX=disabled' /etc/selinux/config"
                ssh $ip "setenforce 0"
        else
                echo "$ip" >ftil.txt
        fi

        }&
done

```

while循环

> 循环次数不一定是固定的

```shell
#!/usr/bin/bash
while read line
do
        user=`echo $line|awk '{print $1}'`
        pass=`echo $line|awk '{print $2}'`
        id $user &>/dev/null
        if [ $? -ne 0 ];then
                useradd $user &>/dev/null
                if [ $? -eq 0 ];then
                        echo "$user is created"
                fi
        else
                echo "$user is  exstis"
        fi
        echo "$pass" |passwd --stdin $user &>/dev/null
        if [ $? -eq 0  ];then
                echo "pass修改成功"
        else
                echo "pass修改失败"
        fi
done < user.txt
```

|            | for                                        | while                                      | until                                      |
| ---------- | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| 特点：     | 循环次数固定                               | 循环次数不一定固定                         | 循环次数不一定固定                         |
| 换行符：   | 空格或者制表符                             | 行，回车                                   | 回车                                       |
| 使用场景： | 循环次数固定                               | 文本处理                                   | 文本处理                                   |
| 空行处理： | 跳过，当做分割                             | 处理空行                                   | 处理空行                                   |
| 循环条件： | 当条件测试成立（条件测试为真），执行循环体 | 当条件测试成立（条件测试为真），执行循环体 | 当条件测试成立（条件测试为假），执行循环体 |
|            |                                            |                                            |                                            |

```shell
#主机连通性测试
while ping -c1 -W1 $ip &>/dev/null
do
        sleep 1
done
echo "$ip is down"
```

```shell
#!/usr/bin/bash
i=2
while [ $i -le 254 ]
do
        {
        ip=172.16.10.$i
        ping -c1 -W1 $ip &>/dev/null
        if [ $? -eq 0 ];then
                echo "$ip is up"
        fi
        }&
        let i++
done
wait
echo "all finish"
```

```shell
#!/usr/bin/bash
i=2
until [ $i -gt 254 ]
do
        {
        ip=172.16.10.$i
        ping -c1 -W1 $ip &>/dev/null
        if [ $? -eq 0 ];then
                echo "$ip is up"
        fi
        }&
        let i++
done
wait
echo "all finish"
```

```shell
#!/usr/bin/bash
i=1
while [ $i -le 254 ]
do
	let sum+=$i
done
echo ":sum: $sum"
```

### 并发控制

```shell
#file Descriptors（FD，文件描述符）或文件句柄：
#进程使用文件描述符来管理打开的文件
#手动定义
exec 6<> ./ping.sh
#手动关闭
exec 6<&
#复制保存
cp
#命名管道
mkfifo /tmp/tmpfifo
file /tmp/tmpfifo
```

```shell
#!/usr/bin/bash
thread=1
tmp_fifofile=/tmp/$$.fifo
mkfifo $tmp_fifofile
exec 8<> $tmp_fifofile
rm $tmp_fifofile
for i in `seq $thread`
do
        echo >&8
done
for i in {1..254}
do
        read -u 8
        {
        ip=172.16.10.$i
        ping -c1 -W1 $ip &>/dev/null
        if [ $? -eq 0 ];then
                echo "$ip is up"
        else
                echo "$ip is down"      
        fi
        echo >&8
        } &
done
wait
exec 8
echo "all finish..."
```

EXPECT

```shell
#!/usr/bin/expect
#产生会话
spawn ssh root@172.16.10.22
expect {
	"yes/no" { send "yes\r"; exp_continue }
	"password:" { send "centos\r" }
}
#交互停在哪里
interact
```

公钥推送

```shell
#!/usr/bin/bash
>ip.txt
password=1qaz!QAZ
rpm -q expect &>/dev/null
if [ $? -ne 0 ];then
        yum -y install expect
fi
if [ ! -f ~/.ssh/id_rsa ];then
ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa -P ""
fi

for i in {2..254}
do
        {
        ip=172.16.10.$i
    ping -c1 -W1 $ip &>/dev/null
    if [ $? -eq 0 ];then
        echo "$ip" >>ip.txt
        /usr/bin/expect <<-EOF
                        spawn ssh-copy-id $ip
                        expect {
                                "yes/no" { send "yes\r"; exp_continue }
                                "password:" { send "$password\r" }
                        }
                        spawn  ssh $ip
                        expect "#"
                                                send "useradd ycc\r"
                                                send "echo 1qaz!QAZ |passwd --stdin ycc\r"
                                                send "mkdir /ycc\r"
                                                send "exit\r"
                        expect eof
                                EOF
    fi
        }&
done
wait

#超时
set timeout 10
#位置变量
set ip [lindex $argv 0]
```

循环for

```shell
#!/usr/bin/bash
for 变量名 in [取值列表]
do
	循环体
done
```

##  数组

1. 数组的分类

   - 普通数组：只能使用整数作为数组索引
   - 关联数组：可以使用字符串，作为数组索引

2. 数组的定义

      ```shell
      #普通数组
      数组名=(`cat /etc/passwd` [200]=1)
      echo $数组名[@]
      数组名[0]=x
      
      #关联数组
      declare -A 数组名
      ```

3. 数组的取值

   ```shell
   #数组的值
   array=([20]=s)
   echo ${arr[@]}
   #数组的索引
   echo ${!arr[@]}
   ```

4. 统计数组的个数

   ```shell
   echo ${#arr[@]}
   ```

5. 数组的切片

   ```shell
   echo ${arr[0]}
   #访问数据的值，从第一个到第二个
   echo ${arr[@]:1:2}
   ```

6. 数组的赋值

   ```shell
#关联数组
   declare -A sex
sex=([m]=1)
   sex+=([f]=1)
let sex[m]++
   ```

7. 数组的遍历

      > 1. 通过数组元素的个数进行遍历（不推荐）
      >
      > > 2. 通过数组元素 的索引进行遍历（推荐）
      > >
      > >    > 3. 将统计的对象作为数组的索引，仅针对关联数据
```shell
      #!/usr/bin/bash
      #for arry
      OLD_IFS=$IFS
      IFS=$'\n'
      for line in `cat /etc/hosts`
      do
              hosts[i++]=$line
      done
      
      for i in ${!hosts[@]}
      do
              echo "$i:${hosts[$i]}"
      done
      IFS=$OLD_IFS
```
```shell
#!/usr/bin/bash
while read line
do
        hosts_array[i++]=$line

done </etc/hosts

echo "索引的1值：${hosts_array[1]}"

for i in ${!hosts_array[@]}
do
        echo "hosts的索印是：$i,hosts的对应索引的值是：${hosts_array[$i]}"
done
```

关联数组

```shell
#!/usr/bin/bash
declare -A shells
while read line
do
        type=`echo $line|awk -F":" '{print $NF}'`
        let shells[$type]++
done </etc/passwd

for i in ${!shells[@]}
do
        echo "$i:${shells[$i]}"
done
```

```shell
#!/usr/bin/bash
declare -A status
type=$(ss -an |grep -v State |awk '{print $2}')

for i in $type
do
        let status[$i]++
done

for i in ${!status[@]}
do
        echo "$i:${status[$i]}"
done
```

## 函数

> 完成特定功能的代码片段（块）
>
> 在shell中定义函数可以使用代码模块化
>
> 函数必须定义才可以使用

### 定义函数

方法一：

函数名（）{

}

方法二：

function 函数名（）{

}

调用函数

```shell
函数名
函数名 参数
函数的返回值是函数最后一条命令的状态码
return 返回值，状态码（最大255）
```

```shell
#!/usr/bin/bash
factorial(){
        factorial=1
        for((i=1;i<=5;i++))
        do
          # let factorial=$factorial*$i
           factorial=$[$factorial*$i]
#               let factorial*=$i
        done
        echo "$factorial" 
}
factorial
```

```shell
#!/usr/bin/bash
function fun() {
        read -p "enter num: " num
        let 2*$num
}
fun
echo "fun return value: $?"
```

reutrn

```shell
#!/usr/bin/bash
function fun() {
        read -p "enter num: " num
        echo  $[2*$num]
}
result=$(fun)
echo "fun return value: $result"
```

数组

```shell
#!/usr/bin/bash
num=(1 2 3 4 5)
array() {
		#局部变量，本函数生效
        local factorial=1
        for i in "$@"
        do
                factorial=$[$factorial*$i]
        done
        echo "$factorial"
}
array ${num[*]}
```

```shell
#!/usr/bin/bash
if [ $# -ne 3 ];then
        echo "usage: `basename $0` par1 par2 par3"
        exit
fi
fun(){
        echo "$[$1*$2*$3]"
}
result=`fun $1 $2 $3`
echo "$result"
```

```shell
#!/usr/bin/bash
for i 
do
	let i++
done
echo "i"
```

函数输出数组

```shell
#!/usr/bin/bash
num=(1 2 3)
array() {
        #       echo "all parameters: $*"
        local newarray=(`echo $*`)
        local i
        for((i=0;i<$#;i++))
        do
                out_array[$i]=$(( ${newarray[$i]} * 5 ))
        done
        echo "${out_array[@]}"
}
result=`array ${num[*]}`
echo ${result[*]}
```

```shell
#!/usr/bin/bash
num=(1 2 3)
array () {
        local newarray=()
        for i in $*
        do
                newarray[++j]=$[$i*5]
        done
        echo "${newarray[@]}"
}
result=`array ${num[*]}`
echo ${result[*]}
echo "i是：$1"
```

> 全局变量 local局部变量。i= 在本shell中，local i在本函数中

> echo -n 不换行

```shell
#!/usr/bin/bash
for i in {a..d}
do
        echo -n $i
        for i in {1..9}
        do
                if [ $i -eq 5 ];then
                        break 2
                fi
                echo -n $i
        done
        echo 
done
```

```shell
#!/usr/bin/bash
while [ $# -ne 0 ]
do
        let sum+=$1
        shift 1
done
echo "sum: $sum
```

```shell
#名词解释
shift 使位置参数向左移动，默认移动一位
exit	退出整个程序
break	结束当前循环，跳出本层循环
continue 忽略本次循环，直接进行下次循环	
```

### 用户输入

```shell
read -p “提示”  变量名
read -t 自动推出
read 多个变量名空格拆分
read -n 2 两个字符
```

> 引号:强引号'',弱引号“”，变量解析。

### 指定位置参数

```shell
set 1 2 3 4 
#重置位置参数
```

### 函数库

```shell
#!/usr/bin/bash
source /etc/init.d/functions
if_else() {
        if [ $? -eq 0 ];then
                action  "$1  is OK " /bin/true
        else
                action  "$1 is Err " /bin/false
        fi
}
read -p "Please input filename: " file
if [ -f $file ];then
        if_else $file
else
        if_else $file
fi

```

```shell
source /etc/init.d/functions
server_manager() {
		systemctl stop $1 &>/dev/null
        systemctl enable $1 &>/dev/null
        systemctl start $1 &>/dev/null
        if [ $? -eq 0 ];then
                action  "$1 is enable" /bin/true
        else
                action  "$1 not enable" /bin/false
        fi
}
server_manager nfs
```

## 正则表达式

> 正则表达式(regular experssion.RE)是为了处理大量的字符串而定义的一套规则和方法，通过定义的这些特殊符号的辅助，系统管理员可以快速过滤，替换或输出需要的字符串。Linux正则表达式一般以行为单位处理的

> 元字符：他们代表是不同于字面本身的含义

#### 基本元字符

| 元字符   | 功能                     | 示例        |
| -------- | ------------------------ | ----------- |
| ^        | 行首定位符               | ^love       |
| $        | 行尾定位符               | love$       |
| .        | 匹配单个字符             | l..e        |
| *        | 匹配前导字符出现0到多次  | ab*love     |
| .*       | 任意多个字符             |             |
| []       | 匹配指定范围内的一个字符 | [Ll]ove     |
| [ - ]    | 匹配指定范围内的一个字符 | [0-9a-Z]ove |
| [^ ]     | 匹配不在指定组内的字符   | [^a-z0-9]   |
| \        | 转义元字符               | love\.      |
| \<       | 词首定位符               | \<love      |
| \>       | 词尾定位符               | love\>      |
| \(...\)  | 匹配稍后使用的字符的标签 |             |
| x\{m\}   | 字符x重复出现m次         |             |
| x\{m,\}  | 字符x重复出现m次以上     |             |
| x\{m,n\} | 字符x重复出现m到n次      |             |

#### 扩展元字符

| 元字符       | 功能                     | 例子           |
| ------------ | ------------------------ | -------------- |
| +            | 匹配一个或者多个前导字符 | [a-z]+ove      |
| ？           | 匹配0或多个前导字符      | lo?ve          |
| a\|b         | 匹配a或b                 | love\|hate     |
| ()           | 组字符                   |                |
| (..)(..)\1\2 | 标签匹配字符             | (love)able\1er |
| x{m}         | 字符x重复m次             | o{5}           |
| x{m,}        | 字符x重复至少出现m次     | o{5,}          |
| x{m,n}       | 字符x重复m到n次          | o{5,10}        |

```shell
#空行
/^$/
/^[\t]*$/
#注释行
/^#/
/^[\t]*$/
```

## grep家族

- grep：在文件中全局查找指定的正则表达式，并打印所有包含表达式的行
- egrep：扩展的egrep，支持更多的正则表达式元字符
- fgrep：固定grep（fixed grep），有时也被作为快速（fast grep),他按字面解释所有的字符

```shell
grep -q "root" /etc/passwd ;echo $?
#字符
\w
#非字符
\W
#词边界
\b
```

- 选项

  ```shell
  -i 忽略大小写
  -q 静默
  -v 反向
  -R 递归
  -o 只显示内容
  -A 后两行
  -B 前两行
  -C 上下文
  ```

  > useradd --help |grep '\-v' v是选项

## sed流编辑器

> 处理时，将当前处理的行存储到缓冲区，也叫“模式空间”，处理完在输出到终端

```shell
#sed命令格式
sed [options] 'command' file
sed [options] -f scriptfile file
#不管是否找到指定的模式，退出状态都是0
#支持正则表达式，放在双斜线当中
#定址
sed -r 'd' /etc/passwd
sed -r '3d' /etc/passwd
sed -r '1,3d' /etc/passwd
sed -r '2,5d' /etc/passwd
sed -r '/root/!d' /etc/passwd
sed -r '/root/,+5d' passwd
sed -r '/root/,5d' passwd
sed -r '1~2d' passwd
sed -r '0~2d' passwd
#命令
a 在当前行后加一行或者多行
c 永新文本修改当前行中的文本
d 删除行
i 在当前行之前插入文本
p 打印
n 读入下一输入行，并从下一条命令而不是第一条命令开始对其处理
q 结束或退出sed
! 对所选行外的所有行应用命令
s 替换标志
	g 全局
	i 忽略大小写
r 从文件中读
w 将行写入文件
y 将字符转换为另一个字符（不支持正则表达式）
h  模式空间覆盖暂存空间
H  模式空间追加暂存空间
g  暂存空间覆盖模式空间
G  暂存空间追加模式空间
x  暂存空间和模式空间替换
#选项
-e 允许多项编辑
-f 指定sed脚本文件名
-n 取消默认的输出
-i 就地编辑
-r 支持扩展元字符
sed -r '3,5s/.*/#&/' 	前面查找的内容
sed -r 's/^/#/'
sed -r '1h;$G' passwd
sed -r '1h;2,$g' passwd
sed -r '1,5s/^[ \t#]*/#/' passwd
sed -r  '1!G;h;$!d' 1.txt
```

> 无论执行是否成功返回值都为0

## awk

``` shell
awk语言
#格式
awk [options] 'commands' filename
#选项
-F
#命令
BEGIN{} 	{} 		END{}
行处理前	行处理		行处理后
#awk工作原理
1.awk使用一行作为输入，并将这一行赋给内部变量$0，每一行也可称为一个记录，一换行符结束
2.然后，行被：（默认为空格）分解成字段，每个字段存储在已编号的变量中，从$1,开始，最多一百个字段
3.awk如何知道用空格来分隔字段的 ，FS默认为空格
4.$1,$2，逗号映射为OFS
5.下一行
#awk内部变量
$0当前记录
NR输入记录编号总
FNR 当前行号
NF 字段数量
$NF 最后一个字段
FS字段分隔符
OFS输出字段分隔符
RS输入记录分隔符
ORS 输出记录分隔符


```



> awk文件分析
>
> > 模式和动作



```shell
正则表达式
匹配字段
~ !~
awk '/^alice/' /etc/passwd
关系运算
> <
awk '$1 == "alice"'
条件表达式
awk '{if($3>300) print $0}'
awk '{if($3>300){print $3} else{print $1}}'
算术运算"======+-*/%^========="
awk -F:'$3*10>500' /etc/passwd
awk -F: '{if($3*10>500){print $0}}' /etc/passwd
逻辑操作和复合模式"=====&& || !======="
awk -F: '$1~/root/ || $3 <=15'
awk -F: '$1 ~ /root/{print $3}' /etc/passwd
#awk脚本编程
awk -F: '{if($3==0){print $1 " is administrator"}}' /etc/passwd
awk -F: '{if($3>0 && $3<1000){i++}} END{print i}' /etc/passwd
awk -F: '/^root/{i=1;while(i<=7){print $i;i++}}' /etc/passwd
awk '{i=1;while(i<=NF){print $i;i++}}'
awk 'BEGIN{for(i=1;i<=5;i++){print i}}'
#数组
awk -F: '{username[i++]=$1} END {print username[0]}' /etc/passwd
#数组遍历
awk -F: '{username[x++]=$1} END{for(i=0;i<x;i++)print i,username[i]}' /etc/passwd
awk -F: '{user[x++]=$1} END{for(i in user){print i,user[i]}}' /etc/passwd
#shell统计
awk -F: '{shells[$NF]++} END{for(i in shells){print i,shells[i]}}' /etc/passwd
netstat -ant |grep ':80' |awk '{status[$NF]++} END{for(i in status) {print i,status[i]}}'
#函数
awk -F: '$1~/^....$/{count++;print $1} END{print "count is:" count}
awk -F: 'length($1)==4{count++;print $1} END{print "count is:" count}'  /etc/passwd
#外部变量

```

> $PS1 $PS2

## 实战-系统管理

脚本目的：分析系统资源性能瓶颈

脚本功能：

1. 查看CPU利用率与负载
2. 查看磁盘，Inode利用率与I/O负载
3. 查看内存利用率
4. 查看TCP连接状态
5. 查看CPU与内存占用最高的10个进程
6. 查看网络流量

```shell
#!/usr/bin/bash
#sys info 
#ycc ver 1.0
while :
do
        select input in cpu_load disk_load disk_use disk_inode
        do
        case $input in
        cpu_load)
                echo "--------------------------------"
                for i in {1..3}
                do
                        echo -e "\033[32m 参考值${i} \033[0m"
                        UTIL=$(vmstat |awk '{if(NR==3)print 100-$15"%"}')       
                        USER=$(vmstat |awk '{if(NR==3)print $13"%"}')
                        SYS=$(vmstat |awk '{if(NR==3)print $14"%"}')
                        IOWAIT=$(vmstat |awk '{if(NR==3)print $16"%"}')
                        echo "Util: $UTIL"
                        echo "User use:$USER"
                        echo "System use: $SYS"
                        echo "I/O wait: $IOWAIT"
			sleep 1
                done
		echo "-------------------------------"
		break
		;;
	disk_load)
			for i in {1..3}
			do
				 echo -e "\033[32m 参考值${i} \033[0m"
				 UTIL=$(iostat  -x -k|awk '/^vd|sd/{OFS=": ";print $1,$NF"%"}')
				 READ=$(iostat  -x -k|awk '/^vd|sd/{OFS=": ";print $1,$6"KB"}')
				 WRITE=$(iostat  -x -k|awk '/^vd|sd/{OFS=": ";print $1,$7"KB"}')
				 IOWAIT=$(vmstat |awk '{if(NR==3)print $16"%"}')
				 echo -e "Util:"
				 echo -e "${UTIL}"
				 echo -e "I/O Wait: $IOWAIT"
				 echo -e "Read/s :\n$READ"
				 echo -e "Write/s:\n$WRITE"
				 sleep 1
            done
		break
		;;
	disk_use)
		DISK_LOG=/tmp/disk_use.tmp
		DISK_TOTAL=$(fdisk -l |awk '/^Disk.*bytes/ && /\/dev/{printf $2" ";printf "%d",$3;if($0 ~ /swap/){print "MB"}else{ print "GB"}}')
		USE_RATE=$(df -Th |awk '/^\/dev/{print int($6)}')
		for i in $USE_RATE
		do
			if [ $i -gt 90 ];then
				PART=$(df -Th |awk '{if(int($6)=='''$i''')print $6}')
				echo "$PART = ${i}%" >>$DISK_LOG
			fi
		done 
		echo "----------------------------------------------"
		echo -e  "Disk total:\n$DISK_TOTAL"
		if [ -f $DISK_LOG ];then
		echo "---------------------------------------------"
		cat $DISK_LOG
		echo "-----------------------------------------------------"
		rm -rf $DISK_LOG
		else
		echo "-----------------------------------------------"
		echo "Disk use rate 90% "
		echo "-----------------------------------------------"
		fi
		break
		;;
	disk_inode)
                INODE_LOG=/tmp/inode_use.tmp
                INODE_USE=$(df -i |awk '/^\/dev/{print int($5)}')
                for i in $INODE_USE
                do
                        if [ $i -gt 90 ];then
                                PART=$(df -h |awk '{if(int($5)=='''$i''')print $6}')
                                echo "$PART=${i}%" >> $INODE_LOG
                        fi
                done
                if [ -f $INODE_LOG ];then
                echo "---------------------------------------------"
                cat $INODE_LOG
		rm -rf $INODE_LOG
                else
                echo "-----------------------------------------------"
                echo "Inode use rate 90"
                echo "-----------------------------------------------" i
                fi
                break
                ;;
	mem_use)
		echo "---------------------------------------------"
		MEM_TOTAL=$(free -m |awk '{if(NR==2){printf "%.1f",$2/1024;print"G"}}')
		USE=$(free -m |awk '{if(NR==2){printf "%.1f",$3/1024;print"G"}}')
		FREE=$(free -m |awk '{if(NR==2){printf "%.1f",$4/1024;print"G"}}')
		CACHE=$(free -m |awk '{if(NR==2){printf "%.1f",$6/1024;print"G"}}')
		echo -e "Total: $MEM_TOTAL"
		echo -e "Use: $USE"
		echo -e "Free: $FREE"
		echo -e "Cache: $CACHE"
		echo -e "------------------------------------------"
		break
		;;
	tcp_status)
		echo "------------------------------------------------"
		COUNT=$(ss -ant |awk '!/State/{status[$1]++}END{for(i in status)print i, status[i]}')
		echo -e "TCP connection status:\n$COUNT"
		echo "------------------------------------------------"
		break
		;;
	cpu_top10)
		echo "---------------------------------------------------"
		CPU_LOG=/tmp/cpu_top.tmp
		for i in {1..3}
		do
			ps aux|awk '{if($3>0.1){{printf "PID: "$2" CPU: "$3"% -->"}for(i=11;i<=NF;i++)if(i==NF)printf $i"\n";else printf $i}}'
		done
		break
		;;
	*)
		exit
        esac
        done
done

```

主机存活

```shell
#!/usr/bin/bash
ip_list="172.16.10.2 172.16.10.1 172.16.10.22"
for ip in "$IP_list"
do
	for count in {1..3}
	do
		ping -c1 -W1 $ip &>/dev/null
		if [ $? -eq 0 ];then
			echo "$ip ping is ok"
			break
		else
			echo "$ip ping is fail: $count"
			fail_count[$count]=$ip
    	fi
	done
	if [ ${#fail_count[@]}  -eq 3 ];then
		echo "${fail_count[1]} ping is fail"
		unset fail_count[*]
	fi
done
```

```shell

#!/usr/bin/bash
while read ip
do
        fail_count=0
        for i in {1..3}
        do
                ping -c1 -W1 $ip &>/dev/null
                if [ $? -eq 0 ];then
                        echo "$ip ping is ok"
                        break
                else
                        echo "$ip ping is fail: $i"
                        let fail_count++
                fi
        done
        if [ $fail_count  -eq 3 ];then
                echo "$ip ping is fail"
        fi
done <ip.txt
```

```shell
#!/usr/bin/bash
ping_success() {
        ping -c1 -W1 $ip &>/dev/null
        if [ $? -eq 0 ];then
                echo "$ip is ok"
                continue
        fi
}
while read ip 
do
        ping_success
        ping_success
        ping_success
        echo "$ip ping is fail"
done <ip.txt
```

多机mysql

```shell
#!/usr/bin/bash
while read ip
do
	{
		ssh root@$ip ""
	}&
done <ip.txt
wait
echo "all finish...."
```

nginx日志

```shell
cat /var/log/nginx/access.log |awk '{print $1}' |sort |uniq -c

```





































































































