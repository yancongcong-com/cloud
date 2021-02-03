# Zabbix

- Zabbix优点：

1. 开源，五软件成本投入
2. server对设备性能要求低
3. 支持设备多，自带多种监控模板
4. 支持分布式集中管理，有自动发现功能，可以实现自动化监控
5. 开放式接口，扩展性强，插件编写容易
6. 当监控的item比较多服务器队列比较大时可以采用被动状态，被监控客户端主动从server下载需要监控的item然后取数据上传到server端。这种方式对服务器的负载比较小
7. Api的支持，方便与其他系统结合

- Zabbix的缺点

1. 需在被监控主机上安装agent，所有数据都存在在数据库里，产生的数据量大，瓶颈主要在数据库
2. 项目批量修改不方便
3. 社区虽然成熟，但中文资源少
4. 入门容易，能实现基础的监控，但是深层需求需要非常熟悉zabbix并大量的二次定制

## zabbix监控系统监控对象

- 数据库
- 应用软件
- 集群
- 虚拟化
- 操作系统
- 硬件
- 网络

zabbix模式

- 被动模式：

- 主动模式：

  > 对于agent

## zabbix架构

zabbix server

- zabbix server是angent程序报告系统可用性，系统完整性和统计数据的核心组件，是所有配置信息，统计信息和操作数据的核心存储器

zabbix数据库存储

- 所有配置信息和zabbix收集到的数据都被存储在数据库中

zabbix web界面

- 为了任何地方和zabbix服务器沟通

zabbix proxy代理服务器

- zabbix proxy可以替zabbix server收集性能和可用性数据。proxy代理服务器是zabbix软件可选择部署的一部分；当然，proxy代理服务器可以帮助单台zabbix server分担负载压力

zabbix agent监控代理

- zabbix agent监控代理部署在监控目标上，能够主动监控本地资源和应用程序，并将收集到的数据报告给zabbix server

## zabbix 数据流

- 监控方面，为了创建一个监控项用于采集数据，必须先创建一个主机
- 告警方面，在监控项里创建触发器，通过触发器来触发告警动作
  1. 为server创建一个host并关联一个用于对cpu进行监控的监控项
  2. 创建一个trigger，设置成为CPU负载过高时触发
  3. trigger被触发，发送告警邮件

## zabbix server安装

### 准备

```shell
#配置zabbix仓库
[root@localhost ~]# wget https://mirrors.aliyun.com/zabbix/zabbix/4.4/rhel/7/x86_64/zabbix-release-4.4-1.el7.noarch.rpm
[root@localhost ~]# rpm -ivh zabbix-release-4.4-1.el7.noarch.rpm 
#配置epel源
[root@localhost ~]# wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
#安装zabbix安装包
[root@localhost ~]#  yum -y install zabbix-agent zabbix-get zabbix-sender zabbix-server-mysql zabbix-web zabbix-web-mysql
#安装Mariadb
[root@localhost ~]# vim  /etc/yum.repos.d/MariaDB.repo
[mariadb]
name = MariaDB
baseurl = http://yum.mariadb.org/10.3/centos7-amd64
gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck=1
[root@localhost ~]# yum -y install MariaDB-client MariaDB-server
[root@localhost ~]# systemctl start mariadb
[root@localhost ~]# systemctl enable mariadb
[root@localhost ~]# mysql_secure_installation 
--为root用户设置密码
--删除匿名账号
--取消root用户远程登录
--删除test库和对test库的访问权限
--刷新授权表使修改生效
#配置mariadb
[root@localhost ~]# vim /etc/my.cnf.d/server.cnf 
[mariadb]
skip_name_resolve = ON
innodb_file_per_table = ON
innodb_buffer_pool_size = 256M
max_connections = 2000
log-bin = master-log
#启动mariadb
[root@localhost ~]# systemctl enable mariadb --now
#创建zabbix库，和用户
MariaDB [(none)]> create database zabbix character set utf8 collate utf8_bin;
MariaDB [(none)]> grant all on zabbix.* to zabbix@'192.168.10.%' identified  by  'zabbix';
#解压数据库文件
[root@localhost ~]# rpm -ql zabbix-server-mysql
/etc/logrotate.d/zabbix-server
/etc/zabbix/zabbix_server.conf
/usr/lib/systemd/system/zabbix-server.service
/usr/lib/tmpfiles.d/zabbix-server.conf
/usr/lib/zabbix/alertscripts
/usr/lib/zabbix/externalscripts
/usr/sbin/zabbix_server_mysql
/usr/share/doc/zabbix-server-mysql-4.4.10
/usr/share/doc/zabbix-server-mysql-4.4.10/AUTHORS
/usr/share/doc/zabbix-server-mysql-4.4.10/COPYING
/usr/share/doc/zabbix-server-mysql-4.4.10/ChangeLog
/usr/share/doc/zabbix-server-mysql-4.4.10/NEWS
/usr/share/doc/zabbix-server-mysql-4.4.10/README
/usr/share/doc/zabbix-server-mysql-4.4.10/create.sql.gz
/usr/share/man/man8/zabbix_server.8.gz
/var/log/zabbix
/var/run/zabbix
[root@localhost ~]# gzip -d /usr/share/doc/zabbix-server-mysql-4.4.10/create.sql.gz
[root@localhost ~]# vim create.sql
use zabbix
[root@localhost ~]# mysql -uroot -p''  <create.sql
```

### 配置zabbixserver

```shell
[root@localhost ~]# cp /etc/zabbix/zabbix_server.conf{,bak}
[root@localhost ~]# vim /etc/zabbix/zabbix_server.conf
ListenPort=10051
SourceIP=172.16.10.13
```

- Zabbix日志

  1. 默认用文件记录，也可以发送给我们的rsyslog日志记录系统，如果我们选择默认，则日志存放在LogFile=/var/log/zabbix/zabbix_server.log中，也可以自己设置

     ```shell
     LogFile=/var/log/zabbix/zabbix_server.log
     ```

- 日志的滚动

  1. 默认值为1，表示滚动。

     ```shell
     LogFileSize=0
     ```

- 日志的级别

- 数据库

  ```shell
  DBName=zabbix
  DBUser=zabbix
  DBPassword='zabbix'
  DBPort=3306
  DBHost=172.16.10.13
  ```

###  启动zabbix-server

```shell
[root@localhost ~]# systemctl enable zabbix-server.service --now
```



## 配置zabbix-web

配置

```shell
[root@localhost ~]# rpm -ql zabbix-web
[root@localhost ~]# vim /etc/httpd/conf.d/zabbix.conf 
php_value date.timezone Asia/Shanghai
[root@localhost ~]# vim /etc/php.ini
date.timezone = Asia/Shanghai
[root@localhost ~]# systemctl start httpd 
[root@localhost ~]# systemctl enable httpd 
```

## 安装zabbix-agent









































































































































