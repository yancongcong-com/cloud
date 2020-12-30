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

## Docker概述

- 核心：隔离
- 轻量级的容器
- Docker基于go开发
- hub.docker.com

- 虚拟化缺点：
  1. 资源占用十分多
  2. 冗余步骤多
  3. 启动很慢
- DevOps
  - 应用更快捷的交付和部署
  - 更快捷的升级和扩缩容
  - 更简单的系统运维
  - 更高效的计算资源利用

## Docker安装

```shell
# step 1: 安装必要的一些系统工具
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
# Step 2: 添加软件源信息
sudo yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
# Step 3: 更新并安装Docker-CE
sudo yum makecache fast
sudo yum -y install docker-ce
# Step 4: 开启Docker服务
sudo service docker start
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
docker pull
#删除
docker rmi -f
```

容器命令

```shell
docker run - images
--name="name"
-d				后台运行
-it				使用交互方式运行，进入容器查看内容
-p				指定容器的端口
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
#容器内到容器外
docker cp 容器  外面
#启动nginx
docker run -d --name nginx -p 3344:80 nginx
#启动tomcat
docker run -it --rm tomcat:9.0
#cpu
docker stats
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

## Docker数据卷

- 容器的持久化和同步操作！容器间也是可以数据共享的

```shell
docker run -it -v 主机目录：容器目录
```

- 具名挂载和匿名挂载

```shell
具名：-v  卷：容器目录：ro
```

- 数据卷容器

```shell
--volumes-from
```

## DockerFile

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
ENV
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

- 安装docker生成一个网卡
- 启动一个镜像，就生成一对
- --link

### 自定义网络

- bridge：桥接docker - 不支持域名
- none：不配置网络
- host：和宿主机共享网络
- container：容器网络连通

[root@localhost mydoccker]# docker network create --driver bridge --subnet 192.168.1.0/24 --gateway 192.168.1.1 mynet

### 网络连通





























































































































