# Docker

- Docker概述
- Docker安装
- Docker命令
- Docker镜像
- 容器数据卷
- DockerFile
- Docker网络原理
- Docker Compose
- Docker Swarm
- CI\CD jenkins

### 镜像仓库

- 镜像仓库用于存放docker镜像
- docker registry提供镜像仓库服务
- 一个docker  registry可以包含多个镜像仓库
- 仓库分为公共镜像仓库和私有镜像仓库
- Build（构建镜像）：镜像就像时集装箱包括文件以运行环境等资源
- Ship（运输镜像）：主机和仓库间运输吗，这里的仓库就像是超级码头一样
- Run（运行镜像）：运行的镜像就是一个容器，容器就是运行程序的地方

## Docker概述

> 容器就是将软件打包成标准化单元，以用于开发，交付和部署。

- 容器是一种轻量级，可移植，自包含的软件打包技术，使应用程序可以在几乎任何地方以相同的方法运行
- 开发人员在自己的电脑创建并测试好的容器，无需任何修改就能够在生产系统的虚拟机，物理服务器及公有云上运行
- 容器赋予了软件独立性，使其免受外在环境差异

- 核心：隔离
- 轻量级的容器
- Docker基于go开发
- hub.docker.com
- Docker是容器引擎，把linux的cgroup，namespace等容器底层技术进行封装抽象，为用户提供了创建和管理容器的便捷界面
- 虚拟化缺点：
  1. 资源占用十分多
  2. 冗余步骤多
  3. 启动很慢
- DevOps
  - 应用更快捷的交付和部署
  - 更快捷的升级和扩缩容
  - 更简单的系统运维
  - 更高效的计算资源利用
- 特点：
  1. 标准化
     - 保证一致的运行环境
     - 弹性伸缩，快速扩容
     - 方便迁移
     - 持续集成，持续交付与持续部署
  2. 高性能
     - 不需要进行硬件虚拟以及运行完整的操作系统
  3. 轻量级
     - 快速启动
  4. 隔离性
     - 进程隔离

| 特性       | 容器               | 虚拟机     |
| ---------- | ------------------ | ---------- |
| 启动       | 秒级               | 分钟级     |
| 磁盘使用   | 一般为MB           | 一般为GB   |
| 性能       | 接近原生           | 弱于       |
| 系统支持量 | 单机支持上千个容器 | 一般几十个 |

### docker镜像

- docker镜像是一个特殊的文件系统，除了提供容器运行时所需的程序，库，资源，配置等文件外，还包含了一些为运行时准备的一些配置参数。镜像不包含任何动态数据，其内容在构建之后也不会被改变

## Docker安装

```shell
#系统3.10
cat /etc/os-release
uname -r
# step 1: 安装必要的一些系统工具
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
# Step 2: 添加软件源信息
sudo yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
# Step 3: 更新并安装Docker-CE
sudo yum makecache fast
sudo yum -y install docker-ce docker-ce-cli containerd.io
# Step 4: 开启Docker服务
sudo systemctl enable docker --now
# Step 5：测试
docker version
docker run hello-world
# 查看镜像
docker images
# 资源目录
ll /var/lib/docker/
```

镜像加速

```shell
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://ehdrotrb.mirror.aliyuncs.com"]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker
```

## Docker的工作原理

docker run---->寻找镜像------有镜像  ----->运行

​												没有镜像----docker hub上下载

Docker是一个C/S架构的系统，Docker的守护进程运行在主机上。

通过docker-client控制

## Docker命令

```shell
docker  version
docker  info
docker --help
```

镜像命令

```shell
docker images
[root@localhost ~]# docker images 
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
hello-world   latest    bf756fb1ae65   11 months ago   13.3kB
#字段
REPOSITORY  镜像的仓库源
TAG			镜像的标签
IMAGE ID	镜像的ID
CREATE 		镜像的创建时间
SIZE		镜像的大小
#选项
-a 列出所有镜像
-q	只显示镜像的ID
#搜索
docker search
#下载
docker pull docker.io/library/tomcat:latest
#删除
docker rmi -f
```

容器命令

```shell
docker run - images ID
--name="name"
-d				后台运行
-it				使用交互方式运行，进入容器查看内容
-p				指定容器的端口
   - 主机：容器
   -容器端口
   -主机ip：容器
-P				随机指定端口
#运行的容器
docker  ps -a
-n最近创建的
-q显示容器编号
#退出
ctrl+p+q
#删除容器
docker  rm -f 容器ID
#启动
docker start 容器
docker  stop 容器
docker kill 容器
docker  restart 容器
#后台启动
docker run -d centos 停止了 没有提供服务
#查看日志
docker logs
#进程
docker top
#信息
[root@localhost ~]# docker inspect centos 
#进入开启的容器
docker exec -it 容器ID /bin/bash 新终端
 docker attach 4abf56e4a300			当前终端
```

## Docker 其他命令

```shell
#容器日志
docker logs -ft --tail 容器ID
 docker run -d centos /bin/bash -c "while true;do echo 111;sleep 1;done"
#进程
docker top suspicious_benz
#元数据
docker inspect 
#容器内到容器外
docker cp fd0ec2e7e927:/etc/nginx/nginx.conf ./
#启动nginx
docker run -d --name nginx4 -p 3344:80  nginx
#启动tomcat
docker run -it --rm tomcat:9.0
删除
#cpu
docker stats
#进入当前正在运行的容器
docker exec -it 828f1147d090 /bin/bash

```

## 可视化

```shell
docker
```

## Docker镜像讲解

### 镜像是什么

- 镜像是一种轻量级，可执行的独立软件包，用来打包软件运行环境和基于运行环境开发的软件，它包含运行某个软件所需的所有内容，包括代码，运行时，库，环境变量和配置文件

## Docker镜像加载原理

> UnionFS（联合文件系统）

UnionFS（联合文件系统）：Union文件系统时一种分层，轻量级并且高性能的文件系统，他支持对文件系统的修改作为一次提交来一层层的叠加，同时可以将不同目录挂载到同一个文件系统，Union文件系统是Docker镜像的基础。镜像可以通过分层来进行继承，基于基础镜像，可以制作各种具体的应用镜像

特性：一次同时加载多个文件系统，但从外面看起来，只能到一个文件系统，联合加载会把各层文件系统叠加起来，这样最终的文件系统会包含所有分层的文件和目录。

镜像层无法改变。

Docker commit

```shell
docker commit -a="yancongcong" -m="add webapps app" 5657bf74f68d tomcat02:ycc
#-a 作者 -m 提交信息 容器ID 版本
[root@localhost ~]# docker images 
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
tomcat02      ycc       6d7c0be59d2d   6 seconds ago   654MB
mysql         5.7       a70d36bc331a   3 days ago      449MB
mysql         latest    c8562eaf9d81   3 days ago      546MB
tomcat        latest    040bdb29ab37   9 days ago      649MB
python        latest    da24d18bf4bf   9 days ago      885MB
nginx         latest    f6d0b4767a6c   10 days ago     133MB
centos        latest    300e315adb2f   6 weeks ago     209MB
hello-world   latest    bf756fb1ae65   12 months ago   13.3kB
```

## Docker数据卷

- 容器的持久化和同步操作！容器间也是可以数据共享的

```shell
docker run -it -v 主机目录：容器目录
docker run -it -v /home/test:/home centos /bin/bash
本地修改



docker run -d -p 3306:3306 -v /mysql/conf:/etc/my.cnf.d/ -v /mysql/data:/var/lib/mysql  -e MYSQL_ROOT_PASSWORD=1 --name=mysqlycc mysql:5.7
持久化



```

- 具名挂载和匿名挂载

```shell
匿名：-v 容器目录
docker run -d --name nginx01 -P -v /etc/nginx nginx
具名：-v  卷：容器目录：ro #只能宿主机改变
docker run -d --name nginx02 -P -v ycc:/etc/nginx nginx
[root@localhost ~]# docker volume inspect ycc
[
    {
        "CreatedAt": "2021-01-22T23:26:53+08:00",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/ycc/_data",
        "Name": "ycc",
        "Options": null,
        "Scope": "local"
    }
]
匿名挂载
具名挂载
指定路径挂载
```

- 数据卷容器---->备份

```shell
--volumes-from
数据卷同步
   99  docker run -it --name docker e01c333ac545 /bin/bash
  101  docker run -it --name docker01 --volumes-from docker  e01c333ac545 /bin/bash
  103  docker ps
  104  docker exec -it 70fae5705176 /bin/bash
  105  docker exec -it edbae0f644e0 /bin/bash
  106  history 

```

结论：

1. 容器之间配置信息的传递，数据卷容器的生命周期一直持续到没有容器使用为止
2. 但是一旦你持久化到了本地，这个时候，本地的数据是不会删除的 

## DockerFile

```shell
FROM centos
VOLUME ["volume01","volume02"]
CMD echo "-------end---------"
CMD /bin/bash
```



- 构建步骤

1. 编写一个dockerfile文件
2. docker build 构建成为一个镜像
3. docker run一个容器

- 基础知识

  1. 每个保留关键字都是大写
  2. 执行从上到下
  3. #注销
  4. 每一个指令都会创建提交一个新的镜像层

- 步骤

  DockerFile：构建文件，定义步骤，源代码

  DokcerImages：通过DockerFile构建生产的镜像，发布

  Docker容器：容器就是镜像运行起来提供服务器

### 文件参数

```shell
FROM 基础镜像
MAINTAINER 作者
RUN		镜像构建的时候运行的命令
ADD	    部署
WORKDIR		镜像的工作目录
VOLUME	卷的目录
EXPOSE	暴露端口
CMD		启动时运行的命令----最后一次
ENTRYPOINT	命令可追加
ONBUILD	可以追加命令
COPY	文件拷贝到镜像
ENV   环境变量
```

```shell
FROM centos
MAINTAINER kuangshen<2713816703qq.com>

ENV MYPATH /usr/local
WORKDIR $MYPATH

RUN yum -y install vim
RUN yum -y install net-tools

EXPOSE 80

CMD echo $MYPATH
CMD echo "------end------"
CMD /bin/bash

```

```shell
#CMD
[root@localhost mydoccker]# cat  cmdcentos
FROM centos
CMD ["ls","-a"]
[root@localhost mydoccker]# docker build -f cmdcentos -t centos:cmd .
[root@localhost mydoccker]# docker run  -it centos:cmd 
[root@localhost mydoccker]# docker run centos:cmd  ls -l
#ENTRYPOINT
[root@localhost mydoccker]# docker run centos:cmd  -l
```

## 提交

```shell
docker login -u -p
docker push 作者名/镜像名：版本号：1.0
```



## Docker网络

```shell
[root@localhost ~]# docker run -it --name tomcat02 tomcat ip add
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
18: eth0@if19: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:ac:11:00:08 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.17.0.8/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever

```



- 安装docker生成一个网卡
- 启动一个镜像，就生成一对
- --link

```shell
  156  docker run -d -P --name tomcat3 --link tomcat2 tomcat 
  157  docker exec -it tomcat3 ping tomcat2

```



### 自定义网络

- bridge：桥接docker - 不支持域名
- none：不配置网络
- host：和宿主机共享网络
- container：容器网络连通

[root@localhost mydoccker]# docker network create --driver bridge --subnet 192.168.1.0/24 --gateway 192.168.1.1 mynet

### 网络连通





























































































































