# Iptables

> iptables：包过滤型的防火墙。

firewalld：防火墙，隔离工具；工作于主机或网络边缘，对于进出本主机或本网络的报文根据事先定义的检查规则做匹配检查，对于能够被规则到的报文作出相对应处理的组件

```shell
# 链
PREROUTING
INPUT
FORWARD
OUTPUT
POSTROUTING
# 功能
filter: 过滤，防火墙
nat: 用于修改原目地址
mange: 拆报文，修改，重新封装
raw: 关闭nat表上启用的连接追踪机制
# 功能 <-- 链
raw: PREROUTING,OUTPUT
mangle: PREROUTING,INPUT,FORWARD,OUTPUT,POSTROUING
nat: PREROUTING,INPUT,OUTPUT,POSTROUING
filter: INPUT,FORWARD,OUTPUT
```

iptables/netfilter

规则：

- 组成部分：根据规则匹配条件来尝试匹配报文，一旦匹配成功，就由规则定义的处理动作作出处理
  1. 匹配条件：
     - 基本匹配条件
     - 扩展匹配条件
  2. 处理动作：
     - 基本处理动作
     - 扩展处理动作
     - 自定义处理机制
- iptables的链：内置链和自定义链
  1. 内置链： 对应于hook function
  2. 自定义链：用于内置链的扩展和补充，可实现更灵活的规则管理机制

添加规则的考量点：

- 要实现哪种功能；判断添加在哪个表上；
- 报文流经的路径：判断添加到哪个链上。

链：链上的规则次序，即为检查的次序；因此，隐含一定的应用法则：

- 同类规则（访问同一应用），匹配范围小的放上面；
- 不同类的规则（访问不同应用），匹配到报文频率较大的放在上面；
- 将那些可由一条规则描述的多个规则合并起来；
- 设置默认策略
  - 建议在规则后面定义一条默认策略

## Iptables命令

```shell
iptables 
# 查看：
-L 列出指定链上的所有规则
-n 数字形式输出
-v 详细信息
-x 显示计算器结果的精确值
--line-numbers：显示规则序号
# 链管理
-N	自定义一个新的链条
-X	仅删除 用户自定义的 引用计数为0,空的链
-P	设置默认策略
-E	重命名
# 规则管理
-A	添加
-I 插入到指定的位置
-D 	删除指定位置或指定条件
-R	替换指定链上的指定规则
-F	清空指定的规则链
-Z	重新计数
# 匹配条件
# 基本匹配条件
-d	目标地址
-s	源地址
-p	协议类型
-i	input interface
-o	output	interface
# 扩展匹配条件
-m
# 处理动作
基本处理动作	ACCEPT DROP
扩展处理动作	REJECT	RETURN	LOG	REDIRECT
用户自定义

# 隐式扩展
 tcp
 udp
 icmp
# 显示扩展
-m 
--dport 目标端口
-j 动作 --- DROP ACCEPT REJECT
-m state --state=TIME_WAIT
   limit --limit 2000/s
   mac  
```

```shell
[root@serverA ~]# iptables -t nat -A POSTROUTING -o ens37 -s 172.16.10.0/24 -j SNAT --to 122.1.1.1
[root@serverA ~]# iptables -t nat -A POSTROUTING -o ens37 -s 172.16.10.0/24 -j MASQUERADE #自动隐射
```

squid

```shell
/etc/squid/squid.conf
[root@serverA ~]# iptables -t nat -A PREROUTING -i ens37 -s 192.168.10.0/24 -p tcp --dport 80 -j REDIRECT --to-ports 3128

```

http

```shell
[root@serverA ~]# iptables -A INPUT -s 0/0 -p tcp --dport 80 -j ACCEPT 
```



## 优先级

```shell
filter:
nat: 
mangle:
raw: 关闭nat表上的跟踪
```

ping

```shell
  iptables -A OUTPUT -s 172.16.10.22 -p icmp --icmp-type 8 -j ACCEPT 
  iptables -A INPUT -s 0/0 -p icmp --icmp-type 0 -j ACCEPT 

Chain INPUT (policy DROP)
target     prot opt source               destination         
ACCEPT     tcp  --  0.0.0.0/0            0.0.0.0/0            tcp dpt:22
ACCEPT     icmp --  0.0.0.0/0            0.0.0.0/0            icmptype 0

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination         
ACCEPT     icmp --  172.16.10.22         0.0.0.0/0            icmptype 8
```

```shell
[root@serverA ~]# iptables -R INPUT 2 -s 0/0 -p tcp -m multiport --dports 22,3306,443,139,445 -j ACCEPT 
# 绑定多个端口
```

```shell
# iprange 
iptables -A OUTPUT 3 -s 172.16.10.22 -p tcp --dport 23 -m iprange --dst-range 172.16.10.1-172.16.10.254 -j ACCEPT 
iptables -A OUTPUT  -s 172.16.10.22 -p tcp --sport 23 -m iprange --dst-range 172.16.10.1-172.16.10.254 -j ACCEPT 
```

```shell
# time
[root@serverA ~]# iptables -A INPUT -d 172.16.10.22 -p tcp --dport 23 -m iprange --src-range 172.16.10.1-172.16.10.254 -m time --timestart 10:00:00 --timestop 16:00:00 --weekdays 1,2,3,4,5 --kerneltz -j ACCEPT 
[root@serverA ~]# iptables -A OUTPUT -s 172.16.10.22 -p tcp --sport 23 -m iprange --dst-range 172.16.10.1-172.16.10.254 -m time --timestart 10:00:00 --timestop 16:00:00 --weekdays 1,2,3,4,5 --kerneltz -j ACCEPT 
```

```shell
# string
[root@serverA ~]# iptables -A OUTPUT -s 172.16.10.22 -m string --algo kmp --string "gay" -j REJECT 
```

```shell
# connlimit
[root@serverA ~]# iptables -A INPUT -d 172.16.10.22 -s 172.16.10.0/16 -p tcp --dport 3306 -m connlimit --connlimit-upto 2 -j ACCEPT
```

```shell
# limit 令牌桶
[root@serverA ~]# iptables -A INPUT -d 172.16.10.22 -p icmp --icmp-type 8 -m limit --limit-burst 5 --limit 20/minute
```

```shell
# state
NEW: 新连接请求 入栈请求为NEW
ESTABLISHED: 已建立的连接
INVALID：无法设别的连接
RELATED：相关联的连接，当前连接是一个新的请求，但附属某个已存在的连接
UNTRACKED: 未追踪的连接
state扩展：
内核模块装载
nf_conntrack
nf_conntrack_ipv4
手动关联
nf_conntrack_ftp
# 跟踪到的连接
	/proc/net/nf_conntrack_max
# 调整可记录的连接数量最大值
	/proc/sys/net/nf_conntrack_max
# 超时时长
	/proc/sys/netfilter/*timeout*
[root@serverA ~]# iptables -A INPUT  -d 172.16.10.22  -p tcp -m  multiport --dport 22,23,80,3306 -m state --state NEW -j ACCEPT  
[root@serverA ~]# iptables -A INPUT  -d 172.16.10.22  -m state --state ESTABLISHED -j ACCEPT 
[root@serverA ~]# iptables -A OUTPUT -s 172.16.10.22 -m state --state ESTABLISHED -j ACCEPT 
```

```shell
# 处理动作
-j targetname
 简单target
   ACCEPT DROP
 扩展target
 	REJECT
 	LOG
 	[root@serverA role]# iptables -A INPUT -d 172.16.10.22 -p tcp --dport 23 -m state --state NEW -j LOG --log-prefix "access telnet"
 自定义链
```

## NAT

```shell
# SNAT
[root@serverA ~]# iptables -t nat -A POSTROUTING -s 172.16.10.0/24 -j SNAT --to-source 172.16.10.22
# DNAT
[root@serverA ~]# iptables -t nat -A PREROUTING -d 172.16.10.22 -p tcp --dport 80 -j DNAT --to-destination 172.16.10.1
# PAT
[root@serverA ~]# iptables -t nat -A PREROUTING -d 172.16.10.22 -p tcp --dport 8080 -j DNAT --to-destination 192.168.10.2:8080
# REDIRECT
```

