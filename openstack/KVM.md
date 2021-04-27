# KVM

## 第一章：KVM概述

vim /etc/vimrc

 65 set nu
 66 set ts=4   tab
 67 set sw=4  自动缩进
 68 set si  自动缩进
 69 set ci

> 虚拟化产品，企业版和桌面版区别

app

guest os

虚拟化软件

操作系统 ------hypervisor

物理机

应用场景：

1. 机器配置比较高
2. 云平台
3. 虚拟机  迁移 快照 随意定义配置
4. 虚拟机管理器

服务

iaas  infrastructure as a service

pass platform as a service

saas software as a service

dsaas data storage as a service

caas container as a service

清缓存

```shell
[root@localhost ~]# echo 1 > /proc/sys/vm/drop_caches 
1  buff
2  cache
3  buff/cache
```

修改

- name
- mem
- cpu
- 硬盘
- 网卡

### 虚拟化概述

#### 什么是虚拟化

- 虚拟化的定义
  1. 在计算技术中，虚拟化意味着创建设备或资源的虚拟版本，如服务器，存储设备，网络或者操作系统等等
  2. 虚拟化技术
     - 系统虚拟化
       1. 这种虚拟化通常变现为在单一系统上运行多个操作系统
       2. 这些虚拟操作系统同时运行，每个操作系统又是相互独立
     - 存储虚拟化
     - 网络虚拟化
     - GPU虚拟化
     - 软件虚拟化
     - 硬件支持虚拟化

#### 虚拟化技术历史

#### 虚拟化实现方式

- 纯软件仿真
  1. 通过模拟完整的硬件环境来虚拟化来宾平台
  2. 模拟X86,ARM，PowerPC等多种CPU
  3. 效率比较低
  4. 产品或方案
     - QEMU,Bochs,PearPC
  
- 虚拟化层翻译
  1. 多数的虚拟化采用虚拟机管理程序Hypervisor
  2. Hypervisor是一个软件层或子系统
     - 也称为VMM虚拟机监控器
  3. 允许多种操作系统在相同的物理系统中运行
  4. 控制硬件并向来宾操作系统提供访问底层硬件的途经
  5. 向来宾操作系统提供虚拟化的硬件
  
- X86 CPU的保护环
  1. Ring0 操作系统
  2. Ring1 设备驱动程序
  3. Ring2 设备驱动程序
  4. Ring3 应用程序
  
- 无硬件辅助的全虚拟化
  1. Full Virtualization without Hardware Assist
  2. 基于二进制翻译的全虚拟化
  3. Hypervisor运行在Ring0
  4. Guest OS运行在Ring 1
  5. 机制：异常，捕获，翻译
  6. 实例：
     - VMware Workstation
     - QEMU
     - Virtual PC
  
- 半虚拟化 Para virtualization

  1. 也称为：超虚拟化，操作系统辅助虚拟化
  2. Hypervisor运行Ring0
  3. Guest OS不能直接运行在Ring0，需要对Kernel进行修改，将运行在Ring0上的，指令转调用Hypervisor
  4. 示例：Xen

- 硬件辅助的全虚拟化

  1. Full Virtualization with Hardware Assist
  2. Intel VT和AMD-V创建一个新的Ring -1单独给Hyperisor使用
  3. Guest OS可以直接使用Ring 0而无需修改
  4. 示例：
     - VMware ESXi
     - Microsoft
     - Xen3.0
     - KVM

- LXC和Docker

  1. 一种轻量级/操作系统虚拟化方式，有Linux内核支持

  2. 起源：chroot系统调用，对当前程序及其子进程改变根目录

  3. 优势：

     - 更快速的交付和部署

     - 更高效的虚拟化

     - 更轻松的迁移和扩展

     - 更简单的管理

       | 特性       | 容器               | 虚拟机     |
       | ---------- | ------------------ | ---------- |
       | 启动       | 秒级               | 分钟级     |
       | 硬盘使用   | 一般为MB           | 一般为GB   |
       | 性能       | 接近原生           | 弱于       |
       | 系统支持量 | 单机支持上千个容器 | 一般几十个 |

- Hypervisor的分类

  1. 裸金属虚拟化
  2. 寄居虚拟化---KVM

### KVM概述

#### KVM历史

> lsmod模块 uname 内核版本

- 以色列的创业公司Qumranet创建了KVM
  1. 早期的主要开发者Avi Kivity
  2. 2006年10月，在完成基本功能，动态迁移，主要的性能优化后，正式宣布了KVM的诞生
  3. 2007年2月发布的内核2.6.20中，开始正式包括了KVM
- 2008年9月，Redhat1.7亿美元收购
  1. EHRL5.2，在集成Xen的基础上，又将KVM添加进来
  2. 2011年11月，RHEL6使用KVM彻底替换了Xen
- QEMU
  1. QEMU是一个通用的开源的硬件模拟器，可以模拟多种硬件
  2. QEMU-KVM从分支与主干合并，QEMU成立KVM在用户空间的管理工具

#### KVM体系结构

- KVM
  1. 初始化CPU硬件，打开虚拟化模式；以支持虚拟机的运行
  2. 负责CPU，内存，中断，控制器，时钟
- QEMU
  1. 模拟网卡，显卡，存储控制器和硬盘
- libvirt
  1. 他提供了统一API,守护进程libvirtd和一个默认命令行管理工具virsh

#### KVM集中管理与控制

- Ovirt 功能强大，是Redhat虚拟化管理平台RHEV的开源版本
- WebVirtMgr virt-manager的Web模式的代替品
- ConVirt 分开原版本和商业版本

Hypervisor /VMM的选择

- 电信/ISP公共云
  1. 单一hypervisor
  2. KVM
- 互联网公司
  1. 单一hypervisor
  2. KVM
- web托管和SAS细分市场
  1. 单一或多个hypervisor
  2. 容器（LXC,Parallels,Docker）
  3. KVM
- 企业
  1. 多种Hypervisor
  2. KVM和vCenter/ESXi

## 第二章：KVM安装

### 环境准备

- 生产环境硬件配置
  1. CPU必须支持虚拟化技术，在BIOS设置为启动
  2. 目前，多数服务器基础桌面计算机均处理启用状态
- 实验环境准备
  1. Test Bead，实验床，试验平台
  2. “嵌套”式试验环境
     - 在虚拟机中再做虚拟化
  3. VMware嵌套虚拟化
     - 产品：workstation,Player,ESXi
     - 支持：ESXi，Hyper-V，KVM，Xen
  4. KVM嵌套虚拟化
     - 支持：ESXi，Hyper-V，KVM，Xen

### KVM安装

- "模板"虚拟机的创建

- CentOS操作系统安装

- 启用网络连接

- 额外的软件包

  ```shell
  yum -y groups install base core virtualization-hypervison virtualization-platform virtualization-tools virtualization-client gnome-desktop
  ```

  > 安装tab ks=http://172.16.10.22/index.txt

- 修改虚拟化引擎的配置

- 复制第一台KVM虚拟机

### KVM远程管理

- SSH

- cockpit

- VNC

  ```shell
  #服务器端
  yum -y install *tigervnc*
  vncpasswd
  vncserver
  #客户端
  https://www.realvnc.com/en/connect/download/vnc/
  ```

- X-Windows

## 第三章：创建虚拟机

### 使用virt-manager创建虚拟机

- virt-manager基本使用

  - 实验环境准备

    1. 添加硬盘

       [root@localhost ~]# echo "- - -" > /sys/class/scsi_host/host0/scan
       [root@localhost ~]# echo "- - -" > /sys/class/scsi_host/host1/scan
       [root@localhost ~]# echo "- - -" > /sys/class/scsi_host/host2/scan

    2. 创建LV

    3. 创建文件系统及挂载点

  1. 启用virt-manager
  2. 虚拟机管理主窗口
  3. 硬件细节窗口
     - 配置虚拟机启动项
     - 附加USB设备给虚拟机
     - 准备工作
     - USB重定向
  4. 虚拟机图形控制台
  5. 添加远程连接
  6. 显示虚拟机细节
  7. 性能监视

### 使用virt-install创建虚拟机

- 命令参数参考

  ```shell
  -name 虚拟机名字
  -M 模拟的主机类型
  -m 内存大小
  -cpu cpu的模式
  -smp cpu核心数
  -numa 设置
  file 
  if=interface
  index
  media
  snapshot
  cache
  format
  -boot
  ```

  [root@localhost vm]# qemu-img create -f qcow2 centos7.0-4.qcow2 10G

  virt-install --name=centos7-4 --disk path=/kvm/vm/centos7.0-4.qcow2 --vcpus=1 --ram=1024 --cdrom=/kvm/iso/CentOS-7-x86_64-DVD-2003.iso --network network=default --graphics vnc,listen=0.0.0.0 --os-type=linux --os-variant=rhel7

  

  virt-install --name=oa --import

  --vcpus=1

  --ram=1024

  --disk path=/vm/oa-disk0.qcow2

  --network network=default

  --graphics vnc,listen=0.0.0.0

  

  

  

- 通过本地iso文件来进行安装

- Kickstart安装

  1. Kickstart是一种无人值守的安装方式

  2. 如果在安装过程中出现要填写参数的情况，安装程序首先会去查找Kickstart生成的文件，如果找到合适的参数，就采用所找到的参数；如果没有找到合适的参数，是需要安装着手工干预了

     ```shell
     virt-install --name=centos7-4 --disk path=/kvm/vm/centos7.0-4.qcow2 --vcpus=1 --ram=1024 --network network=default --graphics vnc,listen=0.0.0.0 --os-type=linux --os-variant=rhel7  --location /kvm/iso/CentOS-7-x86_64-DVD-2003.iso
     --extra-args="ks=http://172.16.10.22/anaconda-ks.cfg"
     ```

- 命令行模式安装

  1. 虚拟机的组成部分

     - 虚拟机配置文件

       ls  /etc/libvirt/qemu

     - 存储虚拟机的介质

       ls  /vat/lib/libvirt/images

  2. 根据配置文件创建虚拟机

     - 复制镜像文件

       

     - 需要配置文件

       

     - 修改配置文件内容

       name

       磁盘镜像

       mac

     - 创建虚拟机

       virsh 	

     - 重启一下

       systemctl restart libvirtd

     - 宿主机开启路由转发

     - 

- 网络安装

  安装文件介质文件位置网络上

- PXE安装

### 半虚拟化驱动virtio

- 半虚拟化驱动virtio原理概述
  1. 使用半虚拟化驱动virtio的目的
     - 为了提高内存，磁盘，网络的性能，需要支持半虚拟化
- 性能对比
- 半虚拟化设备统一接口
  1. 通过统一的接口virti以支持的多种硬件设备
     - 不同的虚拟设备和不同的虚拟机可以有不同的前端驱动
     - 不同的硬件设备可以有不同的后端驱动
     - 两者之间的交互遵循virtio标准
  2. 获得virtio驱动程序
     - 红帽RHEL4.8自动加载

### QEMU Guest Agent和SPICE Agent

- QEMU guest agent安装与配置

  1. 如果VM中安装了QEMU guest agent，Host就可以使用libvirt向VM发送命令，例如“冻结”，“释放”文件系统，虚拟CPU的热添加及移除等
  2. RHEL7 qemu-guest-agent
  3. windows需要手动安装

- 通过livirt来使用QEMU Guest agent

  virtsh shutdown

- SPICE agent安装与配置

  1. 图形优化，加密



## 第四章：管理虚拟机

### libvirt架构概述

- libvirtd守护进程

  > /etc/libvirt/qume

### 使用virt-manager管理虚拟机

- virt-manager主要功能
  1. 定义和创建虚拟机
  2. 硬件管理
  3. 性能监视
  4. 虚拟机的保存和恢复，暂停和继续，关闭和启动
  5. 控制台
  6. 在线和离线迁移
- 启用virt-manager
  1. virt-manager
  2. App>system tools>VMM
- USB重定向
- 远程管理

### 使用virsh来管理虚拟机

- virsh概述
  1. virsh使用libvirt management API构建的管理工具
  2. virsh的名称的含义是virtualization sgekk
     - 交互模式
     - 立即模式
- 常用virsh命令
  1. suspend 停止
  2. resume 回复
  3. shutdown 关机
  4. reboot
  5. autostart 
  6. undefine 删除配置文件

## 第五章：管理虚拟存储

### 虚拟磁盘概述

- 虚拟化项目中存储的注意事项
  1. 存储的性能几乎总是虚拟换的瓶颈
     - 物理
       1. DAS(SCSI，SATA，SAS，N-SAS)
       2. SAN(Fibre Channel,FCoE,iSCSI,SAS)
       3. NAS(NFS,CIFS)
     - 虚拟适配器
       1. IDE
       2. VirtIO
       3. SCSI
     - 虚拟磁盘
       1. 固定
       2. 动态
       3. 差异
       4. 缓存
  2. 通过多个磁盘驱动以分布磁盘I/O来实现存储解决方案
  3. 驱动器的速度越快越好，考虑SSD与机械磁盘的混合使用
  4. 考虑部署集中化的SAN/DFS来实现高可用性和实时迁移
- KVM的存储模式
  1. 基于文件系统的存储
     - dir：Filesystem Directory
     - fs：Pre-Formatted Block Device
     - netfs：Network Exported Directory
  2. 基于设备的存储
     - Disk：Physical Disk Device
     - IScsi：iSCSI Target
     - logical：LVM Volume Group
  3. 通过存储池来简介存储的管理
- KVM的虚拟磁盘类型
  1. 固定 Fixed
     - 在配置时，指定磁盘大小
     - 不管在虚拟磁盘上实际存储多少数据，都将占用相同大小主机磁盘空间
  2. 动态 Dynamic
     - 增长到最大容量，但是只根据需求使用更多的空间
  3. 差异 Differencing
     - 因为创建的差异磁盘，所以只保存变更的数据
     - 列如，将操作系统安装在父盘，然后创建差异化磁盘来执行进一步配置
- KVM支持的虚拟磁盘类型
  1. raw
     - 这并非是一种真正的磁盘，而是代表虚拟机所使用的原始镜像
     - 他并不存储元数据，因此可以作为保证虚拟机兼容性的候选方案。然而，也正因为它不存储元数据，因此不支持某些高级特性，比如快照和压缩等
     - 格式简单，容易转换为其他的格式。需要文件系统的支持才能支持sparse file
- cow：copy-on-write格式，昙花一现
- qcow：QEMU早期的copy-on-write格式，过渡性方案
- qcow2
  1. 按需进行分配磁盘空间，不管文件系统是否支持
  2. 支持快照
  3. 支持zlib的磁盘压缩
  4. 支持AES的加密
- vmdk（Virtual Machine Disk）
  1. VMware虚拟当中默认使用的磁盘格式
- vhd\vhdx（Virtual hard Disk）
  1. 微软默认采用的文件格式
- vdi（VirtualBox）
- 通过qemu-img --help查看支持的格式

### 使用qemu-img管理虚拟磁盘

- qemu-img概述

  1. qemu-img是一个功能强制磁盘镜像管理工具
  2. qemu-img --help 包括以下功能
     - check	检查完整性
     - create    创建镜像
     - commit   提交更改
     - compare  比较
     - convert   转换
     - info    获得信息
     - map   映射
     - snapshot  快照管理
     - rebase 在已有的镜像的基础上创建新的镜像
     - resize 调整大小
     - amend 修订镜像格式选项
  3. qcow2格式选项
     - backing_file
       1. 于指定后端镜像文件
     - backing_file
       1. 设置后端镜像的镜像格式
     - cluster_size
       1. 设置镜像中的簇大小，取值在512到2M之间，默认值为64K
     - preallocation
       1. 设备镜像文件空间的预分配模式
     - encryption
       1. 用于设置加密

- 创建虚拟磁盘

  ```shell
  qemu-img create -f raw
  dd if=/dev/zero of=flat2.img bs=1024k count=0 seek=1024
  cp --sparse稀疏文件
  ```

- 检查虚拟磁盘

  ```shell
  qemu-img check flat2.img
  ```

- 预分配磁盘策略

  1. off
     - 缺省策略，即不使用预分配策略
  2. metadata
     - 分配元数据（metadata），预分配后的虚拟磁盘仍然属于稀疏映像类型
  3. full
     - 分配所有磁盘空间并置零，预分配后的虚拟磁盘属于非稀疏映像类型
  4. falloc
     - 分配文件的块并标示它们的状态为未初始化，相对full模式来说，创建虚拟磁盘的速度要快很多

  ```shell
  qemu-img create -f qcow2 test.qcow2 1g
  qemu-img info test.qcow2
  qemu-img create -f qcow2 test1.qcow2 1g -o preallocation=off  #关闭预分配，默认关闭
  qemu-img info test1.qcow2
  ```
  
- 后备差异虚拟磁盘

  1. 存储与基础镜像（父）磁盘的变化
     - 基础镜像（父）磁盘不会改变
     - 差异磁盘隔离变化
     - 多个差异磁盘可以使用相同的基础镜像（父）磁盘
  2. 优点：标准化基础镜像，节省空间
  3. 缺点：增加了开销，较差的性能

- 虚拟磁盘格式转换

  1. 语法格式

     convert

     ```shell
     qemu-img convert my-vmware.vmdk my-kvm.img
     qemu-img convert -O qcow2 rhel16u3.img rhel6u3-a.img
     ```

- 调整虚拟磁盘大小

  1. 语法格式

     resize filename [+|-] size

  2. 操作之前，一定做好数据备份

  3. 增加文件大小后，需要在客户机中使用fdisk，parted等分区工具进行相应的操作才能正真让客户机使用到增加后的镜像空间

  4. 缩小镜像之前，要在客户机中保证里面的文件系统空余空间，否则会数据丢失

  5. qcow2不支持缩小镜像的操作

  ```shell
  qemu-img resize  base-oa.qcow2 +10G
  ```

### 快照管理

- 磁盘快照
  1. 对磁盘数据进行快照
  2. 主要用于虚拟机备份等场合

- 内存快照
  1. 对虚拟机的内存/设备信息进行保存
  2. 该机制同时用于休眠恢复，迁移等场景
  3. 主要使用virsh save （qemu migrate to file）实现，只能对运行的虚拟机进行

- 检查点快照

  1. 同时保存虚拟机的磁盘快照和内存快照
  2. 用于将虚拟机恢复到某个时间点
  3. 可以保证数据的一致性

- 磁盘快照分类

  1. 按快照信息保存分为：
     - 内置快照：快照数据和base磁盘数据放在一个qcow2文件中
     - 外置快照：快照数据单独的qcow2文件存放
  2. 按虚拟机状态可以分为
     - 关机态快照：数据可以保证一致性
     - 运行态快照：数据无法保证一致性，类似与系统crash后的磁盘数据，使用时可能需要fsck等操作
  3. 按磁盘数量可以分为：
     - 单盘：单盘快照不涉及原子性
     - 多盘：涉及原子性。主要分两个方面：1.是所有盘快照点相同。2.所有盘要么都成功，要么都快照失败。主要依赖与qemu的transacton实现

- qemu-img的快照管理

  1. 语法格式

     ```shell
     qemu-img snapshot -l 磁盘
     qemu-img snapshot -c s1 磁盘
     virsh snapshot-list centos 虚拟机快照
     ```

### 存储池

- 基本概念

  1. Libvirt可以以存储池的形式对存储进行统一管理，简化操作
  2. 对于虚拟机操作来说，存储池和卷并不是必须的
  3. 支持一下存储池
     - dir: Filesystem Directory
     - disk: Physical Disk Device
     - fs: Pre-Formatted Block Device
     - gluster: Gluster FileSystem
     - iscsi: iSCSI Target
     - logical: LVM Volume Group
     - mpath: Multipath Device Enumerator
     - netfs: Network Export Directory
     - rbd: RADOS Block Device/Ceph
     - scsi: SCSI Host Adapter
     - sheepdog: Sheepdog Filesystem
  4. virsh中的存储池相关命令
     - find-storage-pool-sources-as 通过参数查找存储资源池find potential storage pool sources
     - find-storage-pool-sources 通过XML文档查找存储资源找到潜在存储资源
     - pool-autostart 自动启动某个池
     - pool-build 建立池
     - pool-create-as 从一组变量中创建一个池
     - pool-create 从一个XML文件中创建一个池
     - pool-define-as 在一组变量中定义
     - pool-define 在一个XML文件中定义一个池或修改已经有池
     - pool-delete 删除池
     - pool-destory 销毁池
     - pool-dumpxml 
     - pool-edit
     - pool-info
     - pool-list
     - pool-name
     - pool-refresh
     - pool-start
     - pool-undefine
     - pool-uuid

- 显示池与卷的信息

  ```shell
  [root@localhost autostart]# ls -l
  total 0
  lrwxrwxrwx. 1 root root 32 Jan 16 17:58 default.xml -> /etc/libvirt/storage/default.xml
  lrwxrwxrwx. 1 root root 28 Jan 16 18:51 iso.xml -> /etc/libvirt/storage/iso.xml
  lrwxrwxrwx. 1 root root 27 Jan 16 18:52 vm.xml -> /etc/libvirt/storage/vm.xml
  开机自动启动
  ```

  

- 基于目录的存储池

- 基于磁盘的存储池

- 基于分区的存储池

- 基于LVM的存储池

- 构建实验用的集中存储环境

- 基于iSCSI的存储池

- 基于NFS的存储池

### 存储卷

### 虚拟磁盘离线访问工具

## 第六章：管理虚拟网络

### Linux网桥基本概念

- 数据链路的设备，基于MAC地址进行转发
- Redhat/CentOS配置网桥常用方法：
  1. 命令行
  2. nmtui:文本
  3. nmcli:命令行
  4. 图形界面管理工具

### QEMU-kvm支持的网络

- 虚拟机的网络模式
  1. 基于NAT
  2. 基于网桥
  3. 用户自定义的隔离
  4. 直接分配网络设备
- 虚拟机的网卡
  1. RTL8139，e1000
  2. virtio

### 像虚拟机添加网络连接

### 基于NAT的虚拟网络

![image-20210127164019879](D:\Users\Desktop\image-20210127164019879.png)

### 基于网桥的虚拟网络

### 用户自定义的隔离的虚拟网络

```shell
#配置网卡
cp ifcfg-eno16777736 ifcfg-br0
[root@localhost ~]# vim /etc/sysconfig/network-scripts/ifcfg-br0 
TYPE=Bridge
BOOTPROTO=none
NAME=br0
DEVICE=br0
DELAY=0
ONBOOT=yes
IPADDR=172.16.10.100
PREFIX=24
GATEWAY=172.16.10.2
DNS1=172.16.10.2
[root@localhost ~]# vim /etc/sysconfig/network-scripts/ifcfg-eno16777736 
TYPE=Ethernet
BOOTPROTO=none
NAME=eno16777736
UUID=da3cb1e4-f70d-4946-8638-40dcdcbcaf4c
DEVICE=eno16777736
ONBOOT=yes
BRIDGE=br0
brtcl  show 

```

添加nat网络

```shell
[root@localhost ~]# cp /etc/libvirt/qemu/networks/{default.xml,nat.xl}
<network>
  <name>swith</name>
  <uuid>15c29bba-6654-4ca7-b6a4-08f4dc91a244</uuid>
  <forward mode='nat'/>
  <bridge name='virbr1' stp='on' delay='0'/>
  <mac address='52:54:00:e7:1a:08'/>
  <ip address='192.168.100.1' netmask='255.255.255.0'>
    <dhcp>
      <range start='192.168.100.2' end='192.168.100.254'/>
    </dhcp>
  </ip> 
</network>

```

添加隔离网络

```shell
[root@localhost ~]# cp /etc/libvirt/qemu/networks/{default.xml,iso.xml}
<network>
  <name>isolated</name>
  <uuid>15c29b3a-6654-4ca7-b6a4-08f4dc91a244</uuid>
  <bridge name='virbr2' stp='on' delay='0'/>
  <mac address='52:54:00:e7:1a:09'/>
  <domain name='isolatel'/>
  <ip address='192.168.101.1' netmask='255.255.255.0'>
    <dhcp>
      <range start='192.168.101.2' end='192.168.101.254'/>
    </dhcp>
  </ip> 
</network>
[root@localhost ~]# virsh start swith
[root@localhost ~]# virsh net-autostart swith
#列出网络模式
[root@localhost ~]# virsh domiflist rhel7.1
#dhcp信息
[root@localhost ~]# ps aux |grep dnsmasq
```



# 网卡绑定

- 



























































































