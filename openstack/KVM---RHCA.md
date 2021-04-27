KVM硬件打开

内核模块加载

[root@serverb ~]# lscpu |egrep 'vmx|svm'
Flags:                 fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon nopl xtopology tsc_reliable nonstop_tsc eagerfpu pni pclmulqdq vmx ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch invpcid_single ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow vnmi ept vpid fsgsbase tsc_adjust bmi1 avx2 smep bmi2 invpcid rdseed adx smap clflushopt xsaveopt xsavec xgetbv1 arat md_clear spec_ctrl intel_stibp flush_l1d arch_capabilities

#内核模块加载

[root@serverb ~]# modprobe  kvm

[root@serverb ~]# lsmod |grep kvm
kvm_intel             188740  3 
kvm                   637289  11 kvm_intel
irqbypass              13503  3 kvm

#查看

[root@serverb ~]# ls /dev/kvm

#开启嵌套虚拟化

[root@serverb ~]# cat /sys/module/kvm_intel/parameters/nested 
N #等于Y

#永久生效

[root@serverb ~]# cat /etc/modprobe.d/training.conf 
options kvm-intel nested=Y
options kvm-amd nested=1

#卸载模块

[root@serverb ~]# modprobe -r kvm_intel

#加载模块

[root@serverb ~]# modprobe -a kvm_intel

#开启cpu虚拟化

## 创建网络

[root@serverb ~]# yum -y install bridge-utils

[root@serverb ~]# brctl show

#创建网桥

[root@serverb ~]# brctl addbr br2
[root@serverb ~]# brctl addif br2 ens34

# 创建存储

[root@serverb ~]# qemu-img create  -o size=20G -f qcow2 centos.qcow2

[root@serverb ~]# yum -y install qemu-img

## 格式转换

[root@serverb ~]# qemu-img convert -f vmdk -O qcow2 vm02.vmdk vm02.qcow2

调整大小 

[root@serverb ~]# qemu-img resize vm01.qcow2 12G









快照----->后端镜像

[root@serverb ~]# qemu-img create -f qcow2 -b vm01.qcow2 vm02.qcow2

[root@serverb vm]# qemu-img create -f qcow2 -b /kvm/vm/centos01.qcow2 node2.qcow2

#重新 -u不做一致性检查

[root@serverb vm]# qemu-img rebase -u -b /kvm/vm/centos01.qcow2 node2.qcow2

# 删除个性化

[root@serverb qemu]# virt-sysprep -a /kvm/vm/node3.qcow2 

# 创建虚拟机

#远程vnc

# console

虚拟机

- echo "ttyS0" >> /etc/securetty
- vim /etc/grub2.conf
- console=ttyS0

[root@serverb ~]# virsh console centos7.0

## 远程连接

[root@serverb ~]# virsh -c qemu:///system

[root@serverb ~]# virsh -c qemu+ssh://root@172.16.10.13/system

## 快照



# 虚拟机关闭的情况下修改虚拟机文件

[root@serverb qemu]# yum -y install libguestfs-tools

[root@serverb qemu]# guestfish -w -a /kvm/vm/centos02.qcow2 



# kVM缺点

1. 物理机宕机，虚拟机宕机



# 解决方案

manger/controler

第三方身份验证

数据库

hypervisor

存储

