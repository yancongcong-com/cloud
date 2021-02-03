# Ansible

## Ansible的组成部分

- playbook 幂等，剧本，Ansible任务的配置文件，可以将多个任务定义在一个剧本中，由ansible自动执行，剧本执行执行支持多个任务，可以由控制主机运行多个任务，同时对多台远程主机进行管理
- Inventory，ansible管理的远程主机的清单，默认在：/etc/ansible/hosts
- modules,ansible的功能模块，多数为内置的核心模块，也可自定义



Ansible是一个IT自动化工具，它能配置系统，部署软件，编排更复杂的IT任务。

ansible特性：

1. Agentless：不需要在被管理节点上安装客户端，只要有sshd即可
2. Serverless：在服务端不需要启动任何服务，只需要执行命令就行
3. Modules in any language：基于模块工作，可以使用任意语言开发ansbile
4. YAML：使用yaml语言定制playbook
5. ssh：默认使用ssh控制节点

## ansible配置文件

- 优先级
  1. 环境变量：ANSIBLE_CONFIG: 
  2. ./ansible.cfg
  3. ~/.ansible.cfg
  4. /etc/ansible/ansible.cfg

