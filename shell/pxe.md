# PXE

原理：

1. 客户端启动系统，选择从网卡启动
2. 从dhcp服务器中获取到IP地址等信息(192.168.10.100)
3. 还获取到了tftp server(192.168.10.100)及网络引导程序pxelinux.0
4. 通过网卡读取到了tftp server(/var/lib/tftpboot)上的pxelinux.0，读取到内存中
5. 在内存中执行引导程序
6. 读取引导程序的配置文件
7. 个性化

## PXE实施

安装dhcpserver配置

```shell
[root@localhost ~]# yum -y install dhcp
[root@localhost ~]# vim /etc/dhcp/dhcpd.conf 
next-server 172.16.10.100;  #配置tftp的server
filename "pxelinux.0"; #引导程序
subnet 172.16.10.0 netmask 255.255.255.0 {
  range 172.16.10.150 172.16.10.200;
  option domain-name-servers 172.16.10.2;
  option domain-name "ycc.com";
  option routers 172.16.10.2;
  option broadcast-address 172.16.10.255;
  default-lease-time 600;
  max-lease-time 7200;
}
[root@localhost ~]# systemctl enable dhcpd --now
```

配置tftp

```shell
[root@localhost ~]# yum -y install tftp-server  xinetd
[root@localhost ~]# vim /etc/xinetd.d/tftp 
service tftp
{
        socket_type             = dgram
        protocol                = udp
        wait                    = yes
        user                    = root
        server                  = /usr/sbin/in.tftpd
        server_args             = -s /var/lib/tftpboot
        disable                 = no
        per_source              = 11
        cps                     = 100 2
        flags                   = IPv4
}
[root@localhost ~]# systemctl enable xinetd --now
```

配置syslinux

```shell
[root@localhost ~]# yum -y install syslinux
#配置引导文件
[root@localhost ~]# cp /usr/share/syslinux/pxelinux.0 /var/lib/tftpboot/
#新建配置文件目录
[root@localhost ~]# mkdir /var/lib/tftpboot/pxelinux.cfg
#复制配置文件
[root@localhost ~]# cp /media/isolinux/isolinux.cfg  /var/lib/tftpboot/pxelinux.cfg/default
#复制配置文件其他内容
[root@localhost ~]# cp /media/isolinux/* /var/lib/tftpboot/
#新建个性化系统，复制驱动程序
[root@localhost ~]# mkdir /var/lib/tftpboot/centos7
[root@localhost ~]# cp /media/images/pxeboot/{initrd.img,vmlinuz}  /var/lib/tftpboot/centos7/
```

配置iso文件路径

```shell
[root@localhost ~]# yum -y install httpd system-config-kickstart
#启动httpd
[root@localhost ~]# systemctl enable httpd --now
#配置软件包源
[development]
name=dvd
baseurl=http://172.16.10.100/pub
gpgchcek=0
#配置iso文件路径
[root@localhost ~]# mount -o ro,loop /dev/cdrom /var/www/html/pub/
#生成kickstart文件
[root@localhost ~]# system-config-kickstart 
#配置kickstart文件路径
[root@localhost ~]# cp ks.cfg /var/www/html/ks
#编辑default文件
label cenots
  menu label ^Install centos Linux 7.2
  menu default
  kernel /centos7/vmlinuz
  append initrd=/centos7/initrd.img ks=http://172.16.10.100/ks/ks.cfg
```

​	

# 密码破解

redhat6

1. 开机，进入GRUB启动菜单，按空格键
2. 按e进入编辑状态，选择root= 按e进入编辑
3. root=  按1 或者 single
4. 按b启动
5. passwd
6. exit

redhat7

1. e
2. linux  这行  rd.break   ctrl+x   删除后两个
3. mount -o rw,remount /sysroot
4. chroot /sysroot
5. passwd
6. touch /.autorelabel
7. exit
8. reboot

CNA

1. redhat
2. 3个  2个
3. chroot  /mnt/sysimage
4. /etc/passwd



# GRUB2加密

```shell
[root@localhost ~]# grub2-mkpasswd-pbkdf2 
[root@localhost ~]# vim /etc/grub.d/00_header 
cat <<-EOF
set superusers="root"
password_pbkdf2 root grub.pbkdf2.sha512.10000.221AEC7598580DE61D4138D6E7216E4B08CA85A636C176398EA5F68AF0CBFA4EC5608B60EFD8753B76BC17BD1F63562D8DC5AA33F05976169749EB7DAF919AF6.862D932AF26E71C38E260218D3B12A30FFECCA0901C95528036A76942E8F12588465E886C93D93E560E56E955200E3D4D86188E2A0C4A46056E66EEDBEB01B5B
EOF
[root@localhost ~]# grub2-mkconfig -o /boot/grub2/grub.cfg
[root@localhost ~]# reboot
```

# 文件系统修复

```shell
[root@localhost ~]# dd if=/dev/zero of=/dev/sda3 bs=4k count=10
[root@localhost ~]# umount /dev/sda3
#ext
32768
[root@localhost ~]# dumpe2fs /dev/sda3
[root@localhost ~]# fsck -v -y /dev/sda3
[root@localhost ~]# e2fsck -b 98034 /dev/sda3
#xfs
[root@localhost ~]# xfs_repair 
```

# 引导修复

```shell
MBR一个扇区 512
MEBR=引导程序+分区表+55AA
		446+16*2+2=512
dd if /dev/zero of=/dev/sda bs=446 count=1
救援模式
chroot /mnt/sysimages
grub2-install /dev/sda
```





# 系统配置

```shell
#字符集
[root@localhost ~]# cat /etc/locale.conf 
LANG="en_US.UTF-8"
#迷你系统
[root@localhost ~]# ll /mnt/sysimages
#登录信息user
[root@localhost ~]# ll /etc/login.defs 
#gpasswd
[root@localhost ~]# gpasswd it
[root@localhost ~]# newgrp it
#永久的静态路由
[root@localhost ~]# cat /etc/sysconfig/network-scripts/route-eno16777736 
192.168.10.0/24 via 172.16.10.2
#网卡名称，内存日志
[root@localhost ~]# dmesg |grep -C 2  eth
[    1.613597] sd 2:0:0:0: [sda] Attached SCSI disk
[    1.728410] usb 2-1: new full-speed USB device number 2 using uhci_hcd
[    1.760316] e1000 0000:02:01.0 eth0: (PCI:66MHz:32-bit) 00:0c:29:07:1c:78
[    1.760321] e1000 0000:02:01.0 eth0: Intel(R) PRO/1000 Network Connection
[    1.760424] ahci 0000:02:05.0: version 3.0
[    1.760879] ahci 0000:02:05.0: irq 56 for MSI/MSI-X
#系统数据库
[root@localhost ~]# yum -y install aide
#ssh-agent bash 加载公私密钥
[root@localhost ~]# ssh-agent bash
#yum  list all加载软件包
[root@localhost ~]# rpm -ivh  文件名
[root@localhost ~]# rpm -e 软件名
[root@localhost ~]# rpm -aq  所有已经安装的包
[root@localhost ~]# rpm -ql  软件包的文件
[root@localhost ~]# rpm -qc  软件包的配置文件
[root@localhost ~]# rpm -qp 检查脚本
[root@localhost ~]# rpm -qf  文件属于哪个包
#开机内存日志
[root@localhost ~]# ll /run/log/journal/
[root@localhost ~]# vim /etc/systemd/journald.conf
Storage=persistent
#网络
en 以太网
s PCI插槽
p 编号
一个设备同时只能有两个连接
#自动连接
[root@localhost ~]# nmcli device connect ens33
#手动连接
[root@localhost ~]# nmcli connection add  type ethernet ifname ens33 con-name ens33
[root@localhost ~]# nmcli device status
#改连接名
[root@localhost ~]# nmcli connection modify ens33 con.id "new ens33"
#链路聚合
[root@localhost ~]# rpm -qa teamd
teamd-1.29-3.el7.x86_64
[root@localhost ~]# nmcli connection add type team ifname team0 con-name team0  config '{"runner":{"name":"activebackup"}}'
[root@localhost ~]# nmcli connection add type team-slave ifname ens33 con-name ens33 master team0 
修改配置文件
[root@localhost ~]# teamdctl team0 state
setup:
  runner: activebackup
ports:
  ens37
    link watches:
      link summary: up
      instance[link_watch_0]:
        name: ethtool
        link: up
        down count: 0
  ens38
    link watches:
      link summary: up
      instance[link_watch_0]:
        name: ethtool
        link: up
        down count: 0
runner:
  active port: ens37
#dnf应用流，模块化安装
[root@servera ~]# dnf  module list postgresql
#重设
[root@servera ~]# dnf  module reset postgresql
#启用需要版本
[root@servera ~]# dnf  module disable postgresql:10
[root@servera ~]# dnf  module enable -y postgresql:9.6
#安装
[root@servera ~]# dns module install -y posgresql
##################################
#删除临时文件
[root@servera ~]# cd /usr/lib/tmpfiles.d/
#添加自定义的临时文件和目录
[root@servera ~]# cat /usr/lib/tmpfiles.d/test2.conf 
d /var/test1 0770 root root -
f /var/testfile 0770 root root - 
[root@servera ~]# systemd-tmpfiles --create test2.conf
#开机自动删除文件
[root@servera ~]# cat /usr/lib/tmpfiles.d/test2.conf 
R /var/test1 
r /var/testfile
[root@servera ~]# systemd-tmpfiles --remove test2.conf
#######################################
#selinux
加强的安全的访问rwx
主体：用户
客体: 文件
安全上下文selinux
主体：进程
客体：文件
------->客体符合主体的上下文设置才能访问
https://www.cntcvc.com/ReadNews.html?id=6034&queryString=null
模式
enforcing
permissive
disabled
[root@servera ~]# ll  /etc/sysconfig/selinux /etc/selinux/config 
-rw-r--r--. 1 root root 548 Jan 25 09:46 /etc/selinux/config
lrwxrwxrwx. 1 root root  17 Jan 25 09:46 /etc/sysconfig/selinux -> ../selinux/config
#修改默认selinux值
[root@servera ~]# semanage fcontext -a -t "httpd_sys_content_t" /var/www/html/index.html
#还原默认
[root@servera ~]# restorecon -Rv /var/www/html/
#改变当前值
[root@servera ~]# chcon -t httpd_sys_content_t /var/www/html/index.html
[root@servera ~]# chcon --refernce /tmp/  /var/www/html/index.html
```

# VDO

## Striatis

- striatis原理：将文件系统构建在一个精简配置的共享池中。通过Stratis，便捷的使用精简配置，快照和基于池的管理和监控等高级存储功能
- 守护进程：stratisd.service
- 操作步骤

```shell
#安装安装包
[root@servera ~]# yum -y install stratis-cli stratisd
#启动服务
[root@servera ~]# systemctl enable stratisd --now
#创建池
[root@servera ~]# stratis pool create pool /dev/nvme0n1p3
#创建文件系统
[root@servera ~]# stratis filesystem create pool fs
#查看
[root@servera ~]# stratis filesystem list 
Pool Name  Name  Used     Created            Device            UUID                              
pool       fs    546 MiB  Feb 02 2021 21:04  /stratis/pool/fs  ff19f1c6fb484b9da9bb24049b076e01
#挂载
[root@servera ~]# vim /etc/fstab 
UUID="ff19f1c6-fb48-4b9d-a9bb-24049b076e01"  /mnt/testfs  xfs defaults,x-systemd.requires=stratisd.service 0 0
#pool信息
[root@servera ~]# stratis pool list 
Name    Total Physical Size  Total Physical Used
pool                 10 GiB              598 MiB 
#文件系统信息
[root@servera ~]# stratis filesystem list 
Pool Name  Name  Used     Created            Device            UUID                              
pool       fs    546 MiB  Feb 02 2021 21:04  /stratis/pool/fs  ff19f1c6fb484b9da9bb24049b076e01 
#设备信息
[root@servera ~]# stratis blockdev list 
Pool Name  Device Node       Physical Size   State  Tier
pool       /dev/nvme0n1p3           10 GiB  In-use  Data
#添加设备
[root@servera ~]# stratis pool add-data pool /dev/nvme0n5
```

## VDO

```shell
#压缩去重
#安装
[root@servera ~]# yum search vdo
[root@servera ~]# yum -y install vdo kmod-kvdo
#配置
[root@servera ~]# vdo create --name=vdotest --device=/dev/nvme0n1p4 --vdoLogicalSize=50G --force
#查看
[root@servera ~]# vdo list
vdotest
#vdo状态
[root@servera ~]# vdo status --name=vdotest |egrep -i "com|dedu|testvdo"
#格式化
[root@servera ~]# mkfs.xfs -K /dev/mapper/vdotest 
#挂载

#使用状态
[root@servera ~]# vdostats --human-readable
Device                    Size      Used Available Use% Space saving%
/dev/mapper/vdotest      20.0G      4.0G     16.0G  20%           99%
#测试去重
[root@servera ~]# dd if=/dev/zero of=/mnt/vdotest/file bs=1M count=10240
#传输镜像文件测试压缩和去重
```

# NFS

使用：

1. 客户端目录内容为空
2. 客户端要想存放文件成功必须服务端有把共享文件的权限打开
3. 客户端本地挂载的时候，也是有权限设置的

安装性方法

1. none：对文件进行匿名访问，nobody（65534）。对服务器的写入允许
2. sys：文件访问权限基于UID和GID值的标准linux文件权限。如果未指定
3. krb5：客户端必须使用kerberos证明身份
4. krb5i：添加加密性强的保证，确保每个请求中的数据未被篡改
5. keb5p：为客户端和服务器之间的所有请求添加加密，防止网络中的数据泄露

部署

```shell
#安装
[root@servera ~]# yum -y install nfs-utils
#启动
[root@servera ~]# systemctl start nfs-server.service 
[root@servera ~]# systemctl enable nfs-server.service 
#创建共享目录
[root@servera ~]# mkdir /mnt/nfsdir
#修改配置文件
[root@servera ~]# vim /etc/exports
/mnt/nfsdir 172.16.10.0/24(rw,sync)
>root_squash压缩为nobody 只读
#配置生效
[root@servera ~]# exportfs -rv
exporting 172.16.10.0/24:/mnt/nfsdir
#测试
[root@servera nfsdir]# showmount -e 172.16.10.22
Export list for 172.16.10.22:
/mnt/nfsdir 172.16.10.0/24
#防火墙
[root@servera nfsdir]# firewall-cmd --permanent --add-service=nfs
[root@servera nfsdir]# firewall-cmd --permanent --add-service=mountd
[root@servera nfsdir]# firewall-cmd --permanent --add-service=rpc-bind
[root@servera nfsdir]# firewall-cmd --reload 
#客户端挂载
#权限问题
#方法一：
[root@servera ~]# chmod -R o+w /mnt/nfsdir/
#方法二：
no_root_squash
```

# autofs

```shell
#原理：按需挂载，当访问目录，自动挂载，如果5分钟空闲，则会自动解除挂载
1. autofs服务会持续监听一个目录，比如这个目录是/mnt
2. 当我们使用到这个目录下的子目录的时候，/mnt/nfs
3. 会自动的根据规则文件，将远程服务的目录挂载过来。
#客户端
[root@servera ~]# yum -y install autofs
#启动
[root@servera ~]# systemctl start autofs.service  
[root@servera ~]# systemctl enable autofs.service 
#配置监听目录
[root@servera ~]# vim /etc/auto.master
/mnt    /etc/auto.mnt
#配置规则文件
[root@servera ~]# vim /etc/auto.mnt
nfs -fstype=nfs 172.16.10.22:/mnt/share
#######################挂载远程家目录
#client
[root@localhost ~]# useradd -u 2000 remote_user
[root@localhost ~]# rm -rf /home/remote_user/
#server
[root@servera ~]# useradd -u 2000 remote_user
[root@servera ~]# cat /etc/exports
/home/remote_user 172.16.10.0/24(rw,sync,no_all_squash,root_squash)
#client
[root@localhost ~]# cat /etc/auto.master |grep home
/home 	/etc/auto.home
[root@localhost ~]# cat /etc/auto.home 
remote_user -rw,sync 172.16.10.22:/home/remote_user
```

# 启动模式

```shell
#当前启动模式
[root@servera ~]# systemctl get-default
#设置启动模式

```



# 防火墙

```shell
#列出所有支持的区域
[root@servera ~]# firewall-cmd --get-zones
block dmz drop external home internal libvirt public trusted work
#列出默认区域
[root@servera ~]# firewall-cmd --get-default-zone 
public
#列出预定义服务
[root@servera ~]# firewall-cmd --list-all --zone=public 
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: br0
  sources: 
  services: cockpit dhcpv6-client http ssh
  ports: 8081/tcp
  protocols: 
  masquerade: no
  forward-ports: 
  source-ports: 
  icmp-blocks: 
  rich rules: 
#列出所有支持的服务
[root@servera ~]# firewall-cmd --get-services 
RH-Satellite-6 amanda-client amanda-k5-client amqp amqps apcupsd audit bacula bacula-client bgp bitcoin bitcoin-rpc bitcoin-testnet bitcoin-testnet-rpc ceph ceph-mon cfengine cockpit condor-collector ctdb dhcp dhcpv6 dhcpv6-client distcc dns docker-registry docker-swarm dropbox-lansync elasticsearch etcd-client etcd-server finger freeipa-ldap freeipa-ldaps freeipa-replication freeipa-trust ftp ganglia-client ganglia-master git gre high-availability http https imap imaps ipp ipp-client ipsec irc ircs iscsi-target isns jenkins kadmin kerberos kibana klogin kpasswd kprop kshell ldap ldaps libvirt libvirt-tls lightning-network llmnr managesieve matrix mdns minidlna mongodb mosh mountd mqtt mqtt-tls ms-wbt mssql murmur mysql nfs nfs3 nmea-0183 nrpe ntp nut openvpn ovirt-imageio ovirt-storageconsole ovirt-vmconsole plex pmcd pmproxy pmwebapi pmwebapis pop3 pop3s postgresql privoxy proxy-dhcp ptp pulseaudio puppetmaster quassel radius redis rpc-bind rsh rsyncd rtsp salt-master samba samba-client samba-dc sane sip sips slp smtp smtp-submission smtps snmp snmptrap spideroak-lansync squid ssh steam-streaming svdrp svn syncthing syncthing-gui synergy syslog syslog-tls telnet tftp tftp-client tinc tor-socks transmission-client upnp-client vdsm vnc-server wbem-http wbem-https wsman wsmans xdmcp xmpp-bosh xmpp-client xmpp-local xmpp-server zabbix-agent zabbix-server
#列出预定义文件
[root@servera ~]# ll /usr/lib/firewalld/services/
#service的好处
1. 通过服务名称来管理规则更加人性化
2. 高效
#设置--->凡是172.16.10.0/24去home区配
[root@servera ~]# firewall-cmd --permanent --add-source=172.16.10.0/24 --zone=home
[root@servera ~]# firewall-cmd --reload 
[root@servera ~]# firewall-cmd --list-all --zone=home 
#####################
#列出一个区域关联过哪些数据源
[root@servera ~]# firewall-cmd --list-sources --zone=home 
172.16.10.0/24
#查询一个数据源是否在一个区域内
[root@servera ~]# firewall-cmd --query-source=172.16.10.0/24 --zone=home
yes
#更改数据源到另一个区域中
[root@servera ~]# firewall-cmd  --permanent --change-source=172.16.10.0/24 --zone=public 
##################网卡
[root@servera ~]# firewall-cmd  --list-all
#对于网络接口的操作
[root@servera ~]# firewall-cmd --permanent --change-interface=ens160 --zone=trusted 
[root@servera ~]# firewall-cmd --reload 
#恢复默认
[root@servera ~]# firewall-cmd --permanent --remove-interface=ens160 --zone=trusted 
[root@servera ~]# firewall-cmd --reload 
#添加
[root@servera ~]# firewall-cmd --permanent --add-interface=ens160 --zone=trusted 
[root@servera ~]# firewall-cmd --reload 
###################小结####################
1. 正常情况下，网卡在默认区域内，把规则设置在public
2. 如果分开设置，可以通过设置数据源或网卡分配到对应的区域内
###########定义防火墙规则#################
1. 基于网卡
2. 基于服务
3. 基于端口
4. 富规则
语法：
rule
[source]
[destination]
service|port|protocol|icmp-block|masquerade|forwaed-port
[log]
[audit]
[accept|reject|drop]
#富规则的排序
#一旦向某个区域中添加了多个规则，规则的顺序便会在很大程度上影响防火墙的行为
1. 为该区域设置的任何端口转发和伪装规则
2. 为该区域设置的任何记录规则
3. 为该区域设置的任何允许规则
4. 为该区域设置的任何拒绝规则
#使用富规则
[root@servera ~]# firewall-cmd --permanent --add-rich-rule='rule family=ipv4 source address=172.16.10.2/32 service name=ssh reject' 
[root@servera ~]# firewall-cmd --permanent --add-rich-rule='rule family=ipv4 source address=172.16.10.2/32 port port=8080 protocol=tcp accept' 
success允许访问本地8080
####小结
rule family=ipv4/ipv6
source address = 来源IP
destination adderss= 目的IP
service name = 服务名
port port = 端口号 protocol = 协议名（tcp/udp）
动作 （accept|reject|drop）
#################伪装
#是否允许伪装IP
[root@servera ~]# firewall-cmd --query-masquerade 
no
#允许
[root@servera ~]# firewall-cmd --add-masquerade 
success
#禁止
[root@servera ~]# firewall-cmd --remove-masquerade 
success
######
[root@servera ~]# firewall-cmd --permanent --add-rich-rule='rule family=ipv4 source address=172.16.10.2/32 masquerade' 
success
################端口转发
#5868 到80
[root@servera ~]# firewall-cmd --permanent --add-rich-rule='rule family=ipv4 source address=172.16.10.0/24 forward-port port=5868 protocol=tcp to-port=80'
###########端口上下文
[root@servera ~]# semanage port  -l |grep http
```

# su

```shell
[root@servera ~]# vim /etc/pam.d/su
```































































































































































































































































































































































































