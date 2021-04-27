# FusionStorage

## 分布式存储fusionstorage

### 认识Server  SAN

概念：有多个独立服务器自带的存储组成一个存储资源池，同时融合了计算和存储资源

特征：

1. 专有设备变通用设备
2. 计算与存储线性扩张
3. 简单管理，低TCO

### 传统SAN架构

孤立的存储资源：存储通过专用网络连接到有限数据的服务器

存储设备通过添加硬盘框增加容量，控制器性能成为瓶颈

### 分布式Server  SAN架构

共享式存储资源池

容量和性能线性增长

计算和存储融合部署

### 分布式块存储软件FusionStorage

将通用X86服务器的本地HDD,SSD等介质通过分布式技术组织成大规模存储资源池

对非虚拟化环境的上层应用和虚拟机提供工业界标准的SCSI和iSCSI接口

开放的API

### FusionStorage场景

云资源池

数据库及关键应用

## FusionStorage逻辑架构

FSM

管理模块，提供告警，监控，日志，配置操作维护功能，一般为主备节点部署

FSA 

代理进程，部署在各节点上，实现各节点与FSM通信。FSA包含MDC,VBS和OSD三种不同的进程。根据系统不同配置要求，分别在不同的节点上启用不同的进程组合来完成特定的功能

MDC(MetaData Controller)

元数据控制，实现对分布式集群的状态控制，以及控制数据分布式规则，数据重建规则。MDC部署3个节点，形成MDC集群。zk盘存放的是隐射关系

VBS(Virtual Block System)

虚拟块存储管理组件，负责卷元数据的管理，提供分布式集群接入点服务，使计算资源能够通过VBS访问分布式存储资源。每个节点上默认部署一个VBS进程，形成VBS集群。节点上也可以通过部署多个VBS来提升IO性能

OSD(Object Storage Device)

对象存储设备服务，执行具体的IO操作。在每个服务器上部署多个OSD进程，一块磁盘默认对应部署一个OSD进程。ssd1个400G

## FusionStorage部署方式

融合部署

指的是将VBS和OSD部署在同一台服务器中

虚拟化应用推荐采用融合部署的方式部署

分离部署

在不同服务器中

高性能数据库应用侧推荐采用分离部署的方式

## FusionStorage基本概念

DHT：Disrtibuted Hash  TableFusionStorage中指数据路由算法

Partition：代表了一块数据分区，DHT环上的固定Hash段代表的数据区

Key-Value：底层磁盘上的数据组成Kry-Value的形式，每个Value代表一个块存储空间，key是文件

资源池：存储池，一个存储池一个DHT环

Volume：逻辑存储单元，代表了应用看到的一个LBA连续编制，物理地址不连续

数据副本：多副本

## FusionStorage VBS模块及处理流程

VBS模块作为FusionStorage系统存储功能的接入侧，负责完成两大类业务：

- 卷和快照的管理功能
- IO的接入和处理
- VBM模块负责完成卷和快照的管理功能：创建卷，挂载卷，卸载卷，查询卷，删除卷，创建快照，删除快照，基于快照创建卷

IO在VBS进程中的需要三个模块的处理，分别为SCSI，VBP，CLIENT

- SCSI模块负责从内核中将IO引入VBS进程，SCSI模块接收到的IO是标准SCS协议格式的IO请求，通过SCSI四元组（host_id/channel_id/target_id/lun_id）和该IO在块设备上的Offset，读写的数据长度len唯一标识一个IO,SCSI模式将收到的IO信息交给VBP(Virtual Block Process)模块
- VBP内部将通过块格式的IO转换为FusionStorage内部Key-Value格式的IO下发给client，其中KEY的组成为：tree_id(48Byte)+block_no(48Byte)+branch_id(2Byte)+snap_id(2Byte),tree_id/branch_id/snap_id是FusionStorage内部对卷，快照的唯一标识；block_no是将卷按照1M的块划分，本次IO落在哪一个1M的块上的编号
- IO请求到达client模块后，client根据KEY中的tree_id/branch_id进行hash计算，确定本次IO发给哪一个OSD进程处理确定后将IO发给对应的OSD处理
- OSD并收取响应，然后逐层返回IO

### FusionStorage OSD模块处理

RSM: 就把A复制到sedcond OSD third OSD

SNAP：三个OSD一起把A写入到三个磁盘

cache：前提是有SSD的cache，服务器自带的缓存不提供写功能 如果没有SSD，SNAP直接写到HDD

AIO：负责把cache中的数据刷到HDD中

SMIO：

DSK：



## FusionStorage数据路由原理

VBS通过计算确定数据存放在哪个服务的那块硬盘上

OSD通过计算确定数据存放在硬盘的具体位置

## Cache写机制

- OSD在收到VBS发送的写IO操作时，会将写IO缓存在SSD cache后完成本节点写操作
- OSD会周期将缓存在SSD cache中的写IO数据批量写入到磁盘，写Cache有一个水位值，未到刷盘周期超过设定水位值也会将Cache中数据写入到硬盘中
- FusionStorage支持大块直通，按缺省配置大于256k的块直接落盘不写Cache。这个配置可以修改

## Cache读机制

- FusionStorage的读缓存采用分层机制，第一层为内存cache，内存cache采用LRU机制缓存数据
- 第二层为SSD cache,SSD cache采用热点读机制，系统会统计每个读取的数据，并统计热点访问因子，当达到阈值时，系统会自动缓存数据到SSD中，同时会将长时间未被访问的数据移出SSD
- FusionStorage预读机制，统计读数据的相关性，读取某块数据时自动将相关性高的块读出并缓存到SSD中

## 分布式Cache

- FusionStorage集群内各服务器节点的缓存和带宽都均匀分布到各个服务器节点上，不存在独立存储系统中大量磁盘共享计算设备和存储设备之间有限带宽的问题
- FusionStorage支持将服务器部分内存用作读缓存，NVDIMM和SSD用作写缓存，数据缓存均匀分布到各个节点上，所有服务器的缓存总容量远大于采用外置独立存储的方案，即使采用大容量低成本的SATA硬盘，FusionStorage仍然可以发挥很高的IO性能，整体性能提升1~3倍
- FusionStorage支持SSD用作数据缓存，除具备通常的写缓存外，增量热点数据统计和缓存功能，加上其大容量的优势，进一步提升了系统的性能

## 存储网络

- 10GE组网
  1. 物理服务器网卡要求配置网卡聚合（Bond）
  2. GE组网时，硬件至少为4*1Gb组网，其中至少3*1Gb用于存储平面
  3. 10GE组网时，硬件至少为2*10Gb组网，其中至少2*6GE用于存储平面

- ·IB高速组网
  1. FusionStorage内部通信支持低时延，高带宽的Infiniband网络，存储交换无瓶颈
  2. 单口56Gbps带宽，完美配合极速SSD存储吞吐

## VBS模块以及处理流程

- 卷和快照的管理功能
- IO的接 入和处理

## OSD模块以及处理流程

- 磁盘的管理
- IO的复制 
- IO数据的Cache的处理

## FusionStorage  MDC模块功能

### MDC是一个高可靠集群，通过HA机制保证整个系统的高可用性和高可靠性

### ZK分布式服务框架主要用来解决分布式应用中的问题

## 块存储功能

### FusionStorage通过VBS以SCSI或iSCSI方式提供块接口

- SCSI

  安装VBS的物理部署，FusionStorage或KVM等采用SCSI方式 

- ISCSI

  安装VBS以外的虚拟机或主机提供存储访问，VMware,MS SQL Server集群采用iSCSI模式

## 精简配置功能

- 相比传统方式分配物理存储资源，精简配置可显著提高存储空间利用率
-  FusionStorage天然支持自动精简配置，和传统SAN相比不会带来性能下降

## 快照功能

- FusionStorage快照机制，将用户卷数据在某个时间的状态保存下来，可用作导出数据，恢复数据之用

- FusionStorage快照数据在存储是采用ROW机制，快照不会引起原卷性能下降

- 无限次快照

  快照元数据分布式存储，水平扩展，无集中式瓶颈，理论上可支持无限次快照

- 卷恢复速度快

  无需数据搬迁，从快照恢复卷1s完成（传统SAN在几小时级别）

## 故障容忍

- 数据可靠是第一位的，FusionStorage建议3副本配置部署
- 如果两副本故障，认可保障数据不丢失
- 故障容忍根据环境规模可以支持
  1. 跨服务器故障
  2. 跨机柜故障
  3. 跨机房故障

## 快速数据重建

- FusionStorage中的每个硬盘都保存了多个DHT（分布式哈希表）分区（Partition），这些分区的副本按照策略分散在系统中的其他节点。当FusionStorage检测到硬盘或者节点硬件发生故障时，自动在后台启动数据修复
- 由于分区的副本被分散到多个不同的存储节点上，数据修复时，将会在不同的节点上同时启动数据重建，每个节点上只需重建一小部分数据，多个节点并行工作，有效避免单个节点重建大量数据所产生的性能瓶颈，对上层业务的影响做到最小化

## 弹性扩展

- FusionStorage扩容后，容量，性能。带宽，缓存等整体提升

## 跨资源池的卷冷迁移

### 场景一

资源池之间的容量平衡，容量满的池迁移到一个空闲的池

### 场景二

卷在不同性能的资源池池之间的迁移，从低性能的池向高性能的池迁移

## 与FusionSphere联合安装部署

1. FC----FS 必须要有VBS,协议是SCSI协议 ，VBS坏了，访问中断
2. SCSI挂载卷方式，必须要有VBS，协议是SCSI
3. iSCSI卷隐射，使用者可以没有VBS，但是可以通过别人的VBS来访问FS存储，协议是ISCSI