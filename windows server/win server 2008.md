# 域

> 域是一个安全边界，域是一个负责单元

在windows server 2008中，域就是一个服务。

域的数据库，放在c盘，移动到e盘

2003 

restart f8 活动目录还原模式

NTDSUTIL

2008

1. Net stop NTDS
2. NTDSUTIL
3. net start NTDS

## DC

- 保证域架构的稳定

  1. 在DC上不要安装大型服务
  2. DC的计算机不允许公网直接访问
  3. 创建多个DC
  4. 定期多ADDB做备份（180）

- 域的命名

  1. baidu.com (推荐) 手动添加内网的公网IP	
  2. baidu.local 需要更改内网服务的域名

- NetBIOS名称

  1. 小名

- 林功能级别

  1. windows 2000 ---2000 2003 2008 2008 R2
  2. windows server 2003 ---2003以后
  3. windows server 2008 --- 2008以后
  4. windows server 2008 ---- 2008 R2

- sysvol

  1. 组策略高于本地策略

- 设置域还原密码

  1. ntdsutil
  2. set DSRM password

  3. 重置 DSRM 管理员密码: reset password on server DC.h3c.com
     请键入 DS 还原模式 Administrator 帐户的密码: ***********
     请确认新密码: ********

### 远程管理

- RDS(远程桌面)

### 安装备份的域服务

1. 在服务器上安装好域的服务
2. 把当前主DC的数据库复制到本地