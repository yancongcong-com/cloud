# Ansible

### Ansible的组成部分

- playbook 幂等，剧本，Ansible任务的配置文件，可以将多个任务定义在一个剧本中，由ansible自动执行，剧本执行执行支持多个任务，可以由控制主机运行多个任务，同时对多台远程主机进行管理
- Inventory，ansible管理的远程主机的清单，默认在：/etc/ansible/hosts
- modules,ansible的功能模块，多数为内置的核心模块，也可自定义
- Plugins,完成模块功能的补充，借助于插件完成记录日志，邮件等功能。
- API,供第三方程序调用的应用程序编程接口
- ANSIBLE,组合INVENTORY，API，MODULES，PLUGINS的框架，可以理解为ansible命令工具，其为核心执行功能。

> Ansible是一个IT自动化工具，它能配置系统，部署软件，编排更复杂的IT任务。

### ansible特性：

1. Agentless：不需要在被管理节点上安装客户端，只要有sshd即可
2. Serverless：在服务端不需要启动任何服务，只需要执行命令就行
3. Modules in any language：基于模块工作，可以使用任意语言开发ansbile
4. YAML：使用yaml语言定制playbook（paramiko,PyYMAL）
5. ssh：默认使用ssh控制节点

## Ansible安装

```shell
#安装epel源
[root@servera ~]# yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
[root@servera ~]# yum -y install ansible
```



## Ansible配置文件

### 配置文件优先级

1. 环境变量：ANSIBLE_CONFIG: 
2. ./ansible.cfg
3. ~/.ansible.cfg
4. /etc/ansible/ansible.cfg

### 配置文件参数

> 常见配置文件类型：xml,ini,json,yaml

```shell
[defaults]          #通用默认配置
inventory      = /etc/ansible/hosts     #被控制端IP或者DNS列表
library        = /usr/share/my_modules/     ##默认搜寻模块的位置
remote_tmp     = ~/.ansible/tmp            #远程执行临时文件
local_tmp      = ~/.ansible/tmp
plugin_filters_cfg = /etc/ansible/plugin_filters.yml
forks          = 5      ##并行线程数
poll_interval  = 15     ##回频率或轮询间隔时间
sudo_user      = root       ##sudo远程执行用户名
ask_sudo_pass = True        ##使用sudo，是否需要输入密码
ask_pass      = True        ##是否需要输入密码
transport      = smart      ##通信机制
remote_port    = 22         ##远程SSH端口
module_lang    = C          ##模块和系统之间通信的语言
module_set_locale = False
gathering = implicit        ##控制默认facts收集（远程系统变量）
gather_subset = all
gather_timeout = 10
roles_path    = /etc/ansible/roles      ##使用playbook搜索Ansible roles
host_key_checking = False       ##是否检查远程主机密钥
sudo_exe = sudo         ##sudo远程执行命令
sudo_flags = -H -S -n       ##传递sudo之外的参数
timeout = 10            ##SSH超时时间
remote_user = root      ##远程登录用户名
log_path = /var/log/ansible.log     ##日志文件存放路径
module_name = command       ##Ansible命令默认执行的模块
executable = /bin/sh        ##执行的shell环境，用户shell模块
hash_behaviour = replace    ##特定的优先级覆盖变量
jinja2_extensions = jinja2.ext.do,jinja2.ext.i18    ##允许开启jinja2扩展模块
private_key_file = /path/to/file    ##私钥文件存储位置
display_skipped_hosts = True        ##显示跳过任何任务的状态
system_warnings = True      ##禁用系统运行Ansible潜在问题警告
deprecation_warnings = True     ##PlayBook输出禁用“不建议使用”警告
command_warnings = False    ##command模块Ansible默认发出警告
nocolor = 1         ##输出带上颜色区别，0表示开启，1表示关闭
pipelining = False      ##开启pipe SSH通道优化
[privilege_escalation]                                           #对sudo用户提权的配置
#become=True                                                                    #是否sudo
#become_method=sudo                                                      #sudo方式
#become_user=root                                                               #sudo
#become_ask_pass=False   
[accelerate]        ##accelerate缓存加速
accelerate_port = 5099      ##加速连接端口5099
accelerate_timeout = 30     ##命令执行超过时间，单位为s
accelerate_connect_timeout = 5.0    ##上一个活动连接的时间，单位为min
accelerate_daemon_timeout = 30      ##允许多个私钥被加载到daemon
accelerate_multi_key = yes      ##任何客户端想要连接daemon都要开启这个选项
```

## Ansible主机清单

> 主机，主机组同名 主机优先

### 基于密码

``` shell
#方法一
[webservers]
10.1.1.1 ansible_ssh_port=22 ansible_ssh_user=root ansible_ssh_pass='123456'
10.1.1.2 ansible_ssh_port=22 ansible_ssh_user=root ansible_ssh_pass='123456'
#方法二
www[001:006].example.com
#方法三
[web]
web1 ansible_user=root ansible_pass=123456
web2 ansible_user=root ansible_pass=123456
[web:vars]
http_port=80
#方法四
[web]
ubuntu ansible_user=ubuntu ansible_pass=123456 ansible_host=192.168.5.1 ansible_port=22
centos ansible_user=root ansible_pass=123456 ansible_host=192.168.5.2 ansible_port=2022
#常见参数
ansible_connection,SSH的连接方式，可以指定为smart,ssh,paramiko
ansible_host,连接的主机地址，如果ansible中给主机起了一个不同的别名，需要用到这个参数
ansible_port,指定SSH端口，默认22
ansible_user,指定SSH时使用的用户名
ansible_ssh_pass,指定SSH时使用的密码，但是这里指定的是明文密码，不建议使用。而使用values对密码进行加密
ansible_ssh_private_key_file,指定SSH的私钥，使用无密钥登陆时使用
ansible_ssh_common_args,指定SFTP，SCP，SSH默认的额外参数
```

### 基于密钥

```shell
#root用户
#sudo方式
[privilege_escalation]                                          
become=True                                                                  
become_method=sudo                                                     
become_user=root                                                          
become_ask_pass=False 
[root@servera ~]# vim /etc/sudoers
#%wheel ALL=(ALL)       NOPASSWD: ALL
#su方式
[privilege_escalation]                                          
become=True                                                                   
become_method=su                                                      
become_user=root
become_ask_pass=False 
[root@servera ~]# cat /etc/pam.d/su |awk 'NR==4{print}'
#auth		sufficient	pam_wheel.so trust use_uid
```

### 动态主机清单



## Ansible模块

### 用户模块

1. group

```shell
name: somegroup
state: present
```

1. user

```shell
name: 用户名
state: 状态
remove: 删除家目录信息
group:
groups:
append: yes 追加组
```

### 文件模块

1. copy

```shell
src：源路径（控制主机）
dest：受管主机上的一个目标路径（必须）
content：文件内容（替代src参数）
mode：文件权限
owner：文件属主
group：文件属组
setype：指定文件安全上下文类型
backup：文件覆盖前是否生成备份
remote_src: yes从远程主机上复制
```

2. file

```shell
group:
mode:
owner:
path：受管主机文件路径
state: 表明这个文件或者目录属性
```

3. fatch模块：从受管主机上，拉取文件到控制节点

```shell
dest: 控制节点的保存路径
src: 受管节点要拉取文件的路径
flat: 直接保存到目标指定位置，而不是在受管主机名下的文件路径
```

4. lineinfile模块：增加或修改文件内容（以行为单位做流式处理）

```shell
backup: 若文件更新时创建备份文件
insertafter: 在指定位置的下一行插入
insertbefore: 在指定位置的上一行插入
line: 修改后的内容（按行写入）
regexp: 正则表达式（定位）
path: 远端的文件路径
state: 文件修改状态
```

5. synchronize模块：文件同步

```shell
src: 控制节点源路径
dest: 受管主机目标路径
delete: 如果同步完成之后源文件不存在，删除目标文件
```

6. blockinfile模块

```shell
blockinfile:
  path: /etc/ptah
  block: |
  		 this si 
  		 ad
```

7. stat模块

```shell
path: /etc/path
checksum_algorithm: md5
```

### 软件包模块

1. yum

```shell
name: '*'
state: latest
```

2. yum_repository 

```shell
name: epel
description: EPEL YUM repo
file: external_repos
baseurl: https://download.fedoraproject.org/pub/epel/$releasever/$basearch/
gpgcheck: no
```

### 服务模块

1. firewalld

```shell
source: 数据源
interface: 端口
service: 服务
zone: 关键区域
permanent: 永久生效
immediate: 立即生效
state: 防火墙规则状态
rich_rule: 富规则
```

3. selinux

```shell
state: disabled
```

4. service

```shell
name: httpd
state: restarted
enabled: yes
```

### 磁盘模块

1. mount

```shell
src:
path:
opts:
state:
- present将挂载信息写入/etc/fstab			  umounted 卸载，不清理/etc/fstab	
- mounted先挂载，在将挂载信息/etc/fstab  		absent 卸载，也清理/etc/fstab	
```

2. lvg

```shell
pesize: 物理区块的大小，必须是2的幂
pvs: 逗号分隔，物理卷
vg: 卷组名称
state: 创建或删除
```

2. lvol

```shell
lv: 逻辑卷
resizefs: 调整逻辑卷的文件系统大小
shrink: 启动逻辑卷收缩
size: 逻辑卷的大小
snapshot: 逻辑卷快照
state: 创建和删除
vg: 卷组
```

2. parted模块

```shell
align:  配置分区对齐
device: 块设备
flags: 分区的标识 
number: 分区编号
part_end: 指定的从磁盘开头的大小
state: 创建和删除
nuit: 分区信息的大小单位
```

2. feilsystem

```shell
dev: 设备
fstype: 文件系统类型
resizes: 大小
```

### 系统模块

1. cron

```shell
name: "check dirs"
hour: "5,2"
job: "ls -alh > /dev/null"
```

2. 压缩

```shell
copy：默认为yes，当copy=yes，那么拷贝的文件是从ansible主机复制到远程主机上的，如果设置为copy=no，那么会在远程主机上寻找src源文件

src：源路径，可以是ansible主机上的路径，也可以是远程主机上的路径，如果是远程主机上的路径，则需要设置copy=no

dest：远程主机上的目标路径

mode：设置解压缩后的文件权限
```

### 网络模块

1. get_url模块

```shell
url: 下载源地址
dest: 存放目标位置
mode: 权限
```

2. uri模块

```shell
url: 地址
method： 请求方法 如GET,POST,PUT,DELETE,HEAD.默认GET
timeout: 超时时间 默认30秒
status_code: 指定返回的状态码，如果匹配就成功，否则失败。默认200
return_content: 要不要返回网页的body
```

### 调试模块

1. debug

```yaml
debug:
  msg: 打印的自定义消息。如果省略，则打印一般消息。
  var: 要调试的变量名,不应该使用Jinja2分隔符
  verbosity: 调试变量
```

## Ansible Playbook剧本

> vim >>>>> 
>
> 65 set nu
>  66 set ts=2
>  67 set sw=2
>  68 set et
>  69 set si
>  70 set ci

YAML剧本语法格式

1. 缩进：用两个空格缩进
2. 列表：用-
3. 冒号：后有空格

Playbook输出的详细程度

1. -v：显示结果
2. -vv：任务结果和任务配置
3. -vvv：匹配关于与收管主机连接信息
4. -vvvv：增加显示

```yml
# 注释
- name: # 注释
# 字符串
"" ''
# 多行字符串
include_newlines: | #表示要保留字符串中的换行符
	EXample Company
	123 Main str
fold_newlines: > # 表示要将换行符转换为空格，并删除行中的前导空格。
	This is
	a very long
# 字典
name:
  var: ls
  date: lo
{ var: ls, date: lo }
# 列表
name:
  - httpd
  - nfs-utils
name: [ httpd, nfs-utils ]
# 注意 "{{}}"
```

执行空运行

1. 用户**-C**选项对playbook执行空运行。这会使Ansible报告在执行该playbook时将会发生什么更改，但不会对受管主机进行任何实际的更改

Playbook语法检查

1. [root@servera ansible]# ansible-playbook  useradd.yml    --syntax-check可对playbook语法检查

主机清单

```shell
通配符： *
列表：node,node1
与符号：&（and）
非符号：！（not）
```



## Ansible变量

> ansible变量简化维护

### 定义变量

> 语法----变量名:变量值。必须以字母开头，并且只能含有字母，数字和下划线。

- ansible playbook文件中进行定义
- inventory 主机清单中进行定义
- playbook文件使用时-e进行指定参数

```shell
1. playbook中定义变量
#方法一
vars:
  - 变量名: 变量值
#方法二
vars_files:
  - 变量文件名
2. inventory主机清单中定义变量
#方法一
[组名:vars]
变量名: 变量值
#方法二
创建两个目录
host_vars/主机名
group_vars/组名
3. playbook执行中定义
```

### 变量优先级

1. 外置传参
2. playbook（vars_files）
3. playbook（vars）
4. inventoty(host_vars/host_name)
5. inventoty(group_vars/group_name)
6. inventoty(group_vars/all)

### 变量类型

常规变量：

```shell
变量名：变量值
```

数组：

```shell
变量名：
   - 变量值
   - 变量值
```

字典：

```shell
变量名:
  子变量名:
    子变量名:变量值
  子变量名:
    子变量名:变量值
```

### 变量引用

```shell
#常规变量
"{{ 变量名 }}"
#数组变量
"{{ 数组名[下标] }}"
#字典变量
"{{ 变量名['子变量名']['子变量名'] }}"
"{{ 变量名.子变量名.子变量名 }}"
```

### 变量注册register

> 可以将一个任务的输出结果定义到一个变量中，方便后续任务进行引用

```shell
---
- name: Configure httpd server
  hosts: all
  tasks:
    - name: Install httpd package
      yum:
        name: httpd
        state: present

    - name: Service httpd server
      service:
        name: httpd
        state: started
        enabled: yes

    - name: Ps httpd state
      shell: ps aux |grep httpd
      register: check_httpd

    - name: Debug httpd state
      debug:
        msg: "{{ check_httpd }}"
```

### Ansible Vault

```shell
作用：加密敏感的数据，密码等信息，通常情况下，都是定义在变量内。
1> 加密变量文件
2> 加密证书
#创建一个加密文件
[root@servera ~]# ansible-vault create sec.yml
New Vault password: 
Confirm New Vault password: 
#解密
[root@servera ~]# ansible-vault decrypt sec.yml
Vault password: 
Decryption successful
#加密一个已存在的文件
[root@servera ~]# ansible-vault encrypt sec.yml 
New Vault password: 
Confirm New Vault password: 
Encryption successful
#重置加密文件的密码
[root@servera ~]# ansible-vault rekey sec.yml 
Vault password: 
New Vault password: 
Confirm New Vault password: 
Rekey successful
#编辑已存在的加密文件
[root@servera ~]# ansible-vault edit sec.yml 
Vault password: 
#查看变量
[root@servera ~]# ansible-vault view sec.yml 
Vault password: 
```

### Facts变量-------事实

> 采集被控端的状态信息

```shell
#关闭facts变量,play中
gather_facts: no
#获取facts的值
[root@servera ansible]# ansible all -m setup
```

| **事实**                    | **变量**                                                     |
| --------------------------- | ------------------------------------------------------------ |
| **短主机名**                | **ansible_facts['hostname']**                                |
| **完全限定域名**            | **ansible_facts['fqdn']**                                    |
| **IPv4地址**                | **ansible_facts['default_ipv4']['address']**                 |
| **所有网络接口的名称列表**  | **ansible_facts['interfaces']**                              |
| **/dev/vda1磁盘分区的大小** | **ansible_facts['devices']['vda']['partitions']['vda1']['size']** |
| **DNS服务器列表**           | **ansible_facts['dns']['nameservers']**                      |
| **当前运行的内核版本**      | **ansible_facts['kernel']**                                  |

### 创建自定义事实

```shell
1️⃣：除了使用系统捕获的事实外，我们还可以自定义事实，并将其本地存储在每个受管主机上；

2️⃣：默认情况下，setup模块从各受管主机的/etc/ansible/facts.d目录下的文件和脚本中加载自定义事实

3️⃣：各个文件或脚本的名称必须以.fact结尾才能被使用；动态自定义事实脚本必须输出JSON格式的事实，而且必须是可执行文件
```

### 魔法变量（万能变量）

> 一些变量并事实或通过setup模块配置，但也由Ansible自动设置。这些魔法变量也可用于获取与特定受管主机相关的信息

```shell
#包含受管主机的变量；可以用于获取另一台受管主机的变量的值，如果还没有为受管主机收集事实，则它不会包含该主机的事实
hostvars
#列出当前受管主机所属的所有组
group_names
#列出清单中的所有组和主机
groups
#包含清单中配置的当前受管主机的主机名称。这可能因为各种原因而与事实报告的主机名称不同。
inventory_hostname
# 顶级不能加引号，取子必须加引号
```

```shell
 #inventory_hostname
  1 ---
  2 - name: Display gather_facts information
  3   hosts: all
  4   tasks:
  5     - name: Debug gather_facts
  6       debug:
  7         var: group_names
  8       when: 'inventory_hostname in groups.webserver'
  9		 #when: "'webserver' in group_names"
```

```shell
#hostvars
  1 ---
  2 - name: Display gather_facts information
  3   hosts: all
  4   tasks:
  5     - name: Debug gather_facts
  6       debug:
  7         var: hostvars['serverb']['ansible_facts']['fqdn']
  8       when: ansible_facts['fqdn'] == 'servera.example.com'
```

## Ansible任务控制

### Ansible判断

> 判断在ansible任务中的使用频率非常高，判断任务是否执行

| 操作                         | 示例                            |
| ---------------------------- | ------------------------------- |
| 等于（字符串）               | ansible_machine == "x86_64"     |
| 等于（数字）                 | max_memory == 512               |
| 小于                         | max_memory < 512                |
| 大于                         | max_memory > 512                |
| 小于等于                     | max_memory <= 512               |
| 大于等于                     | max_memory >= 512               |
| 不等于                       | max_memory != 512               |
| 变量存在                     | max_memory is defined           |
| 变量不存在                   | max_memory is not defined       |
| 布尔值存在为True             | memory_available                |
| 布尔值存在为False            | not memory_available            |
| 第一个变量存在在第二个变量中 | inventory_hostname in webserver |

```shell
#主机名像是
when: ( inventory_hostname is match ("ser*") )
```

```shell
  1 ---
  2 - name: Configure httpd server
  3   hosts: all
  4   tasks:
  5     - name: Install httpd package
  6       yum:
  7         name: httpd
  8         state: present
  9 
 10     - name: Service httpd server
 11       service:
 12         name: httpd
 13         state: started
 14         enabled: yes
 15 
 16     - name: Check http server
 17       command: systemctl is-active httpd
 18       ignore_errors: yes
 19       register: check_httpd
 20 
 21     - name: Http Restart
 22       service:
 23         name: httpd
 24         state: restarted
 25       when: check_httpd.rc == 0
```

### Ansible循环

```shell
#减少重复使用的模块
#方法一
with_items----item
- { name: 'www',groups: 'bin' }
- { name: 'test',groups: 'root' }
#方法二
pool----------item
#循环嵌套
mysql_user:
  name: "{{ item[0] }}"
  priv: "{{ item[1]}}.*:ALL"
  append_privs: yes
  password: redjat
with_nested:
  - [ 'joe','jane' ]
  - [ 'clientdb','employeedb' ]
  
#文件循环
  1 ---
  2 - name: copy file
  3   hosts: all
  4   tasks:
  5     - name: Copy file
  6       copy:
  7         src: "{{ item }}"
  8         dest: /tmp/
  9       with_fileglob:
 10         - /ls/*
```

### Ansible触发器

```shell
#实时更新
#监听---->触发
#notify-->handlers
```

### Ansible处理任务失败

```shell
#错误忽略
ignore_errors
#强制执行触发器
force_handlers
#定义错误
failed_when
#定义任务是否改变--->错误处理 关闭changed
changed_when: ( check_nginx.stdout.find('successful'))
changed_when: false
#块处理
block
rescue
always
block + when
```

### Ansible tag标签

```shell
#类型
1. 对一个tasks任务指定一个tags标签
2. 对一个tasks任务指定多个tags标签
3. 对多个tasks任务指定一个sags标签
tags: 标签名
ansible-playbook *.yml -t '标签名' #只执行标签任务
ansible-playbook *.yml --skip-tags '标签名' #不执行执行标签任务
```

### Ansible Include包含

```yaml
#Include特定的共有文件------>只有tasks文件
- name: Include
  include: http.yml
- name: Include
  include_tasks: http.yml
#多个playbook合并------->用于完整的playbook
- import_playbook: tasks.yml
- import_playbook: tasks1.yml
```

## Ansible Jinjia2

Ansible使用Jinjia2格式作为文件模板

Ansible，一般我们用Jinjia2模板来管理配置文件

它的每次使用都会被ansible标记为"changed"状态

### 分隔符

1. {% %}

```shell
Jinjia2模板使用{%EXPR%}语法来包含表达式或逻辑，比如，循环，判断
```

1. {# #}

```shell
Jinjia2模板使用{%COMMENT%}语法来包含注释
```

3. {{}}

```shell
Jinjia2模板使用{%VARS%}语法来获取表达式或变量的值
```

### 循环

```yaml
{% for user in users %}
	{{ user }}
{{% endfor %}}
```

### 判断

```yaml
{% if finished %}
	{{ result }}
{% endif %}
```

### 变量过滤

Jinjia2支持改变输出格式，比如，输出为JSON或yaml格式。

to_json,表示输出为JSON格式。

to_yaml,表示输出为YAML格式

to_nice_json,表示输出近似JSON，人可读

to_nice_yaml,表示输出近似yaml，人可读

from_json,解析JSON字符串

## Ansible Role角色

> rloe主要用于代码重用和分享。

Ansible角色子目录

| 子目录    | 功能                                                         |
| --------- | ------------------------------------------------------------ |
| defaults  | 此目录中的main.yml文件包含角色变量的默认值，使用角色时可以覆盖这些默认值。这些变量的优先级较低，应该在play中更改和自定义。 |
| files     | 此目录包含由角色任务引用的静态文件。                         |
| handlers  | 此目录中的main.yml文件包含角色的处理程序定义。               |
| meta      | 此目录中的main.yml文件包含与角色相关的信息，如作者，许可证，平台和可选的角色依赖项。 |
| tasks     | 此目录中的main.yml文件包含角色的任务定义。                   |
| templates | 此目录包含由角色任务引用的的Jinjia2模板。                    |
| tests     | 此目录可以包含清单和test.ymlplaybook，可用于测试角色。       |
| vars      | 此目录中main.yml文件定义角色的变量值。这些变量常用于角色内部用途。这些变量的优先级较高，在playbook中使用时不应更改。 |

系统角色

| 名称                       | 状态     | 角色描述                                       |
| -------------------------- | -------- | ---------------------------------------------- |
| rhel-system-roles.kdump    | 全面支持 | 配置kdump服务恢复服务。                        |
| rhel-system-roles.network  | 全面支持 | 配置网络接口。                                 |
| rhel-system-roles.selinux  | 全面支持 | 配置和管理SElinux自定义，包括SElinux模式。     |
| rhel-system-roles.timesync | 全面支持 | 使用网络时间协议或精确时间协议配置时间同步。   |
| rhel-system-roles.postfix  | 技术预览 | 使用Postfile服务将每个主机配置为邮件传输代理。 |
| rhel-system-roles.firewall | 开发中   | 配置主机的防火墙。                             |
| rhel-system-roles.runed    | 开发中   | 配置tuned服务，以调优系统性能。                |

## Ansible Galaxy角色部署

```shell
#role搜索
[root@servera ansible]# ansible-galaxy search "install git" --platforms el
#role信息
[root@servera ansible]# ansible-galaxy info 
#下载role
[root@servera ansible]# ansible-galaxy install -p roles/
```

# 示例

```shell
[root@servera ansible]# cat http.yml 
---
- name: Configure httpd server
  hosts: serverb
  vars:
    servers:
      - { port: 80,name: web1,admin: web1@exqmple.com,document: /var/www/web1 }
      - { port: 8080,name: web2,admin: web2@exqmple.com,document: /var/www/web2 }
  tasks:
    - name: Install httpd package
      yum:
        name: httpd
        state: latest


    - name: Configure httpd server
      template:
        src: ./httpd.conf.j2
        dest: /etc/httpd/conf.d/www.conf

    - name: Service httpd server
      service:
        name: httpd
        state: started
        enabled: yes
[root@servera ansible]# cat httpd.conf.j2 
{% for index in servers %}
<VirtualHost {{ ansible_default_ipv4.address }}:{{ index.port }} >
  ServerName {{ index['name'] }}
  DocumentRoot {{ index.document }}
  {% if index.admin is defined %}
  ServerAdmin {{ index.admin }}
  {% endif  %}
  <Directory {{ index.document }} >
    AllowOverride None
    Options Indexes FllowSymLinks
    Require all granted
  </Directory>
</Virtualhost>
{% endfor %}
```











