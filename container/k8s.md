# k8s

资源清单：

pod(最小单位):

pod控制器：

service服务发现：

存储：

调度器：

集群安全：

HELM(yum包管理工具):

运维：

## 组件

etcd:键值，可信赖的，分布式存储信息（持久化）

api-server：所有组件访问的统一入口

ControllerManager：维持副本期望数目

Scheduler： 调度器

kubelet: 直接更容器引擎交互实现容器的生命周期管理

kube-proxy： 负责写入规则，实现服务隐射访问的

CoreDNS: 集群中的svc创建域名记录

Dashboard：b/s结构的访问体系

Ingress Controller: 七层负载均衡

Federation :  跨集群的统一管理

Prometheus： 监控能力

ELK： 提供K8s集群日志统一分析介入平台

## pod

- 自主式pod
- 控制器管理的pod



RC & RS 集合式的selector& Dev(滚动更新)

















