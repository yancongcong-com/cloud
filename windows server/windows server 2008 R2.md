# Windows Server 2008 R2

## 基本服务

### 计算机管理

- 计算机管理

  ```powershell
  compmgmt.msc
  ```

- 服务管理

  ```powershell
  msconfig
  ```

- 网络管理

  ```powershell
  # 网络发现 -----网上邻居
  # 文件共享 
  # 公用文件共享 ---- 公用文件夹的共享
  # 打印机共享
  # 密码保护的共享 ----- 不用密码，用Guest用户登录
  ```

- IE管理

  ```powershell
  # 关闭IE ESC
  # IE缓存
  # IE安全
  # IE高级
  ```

- 桌面体验

  ```powershell
  # 安装桌面体验功能
  # 启动Themes
  ```

- 文件夹选项

  ```powershell
  control
  ```

### 本地用户和组

- 本地用户和组

  ```powershell
  lusrmgr.msc
  ```

- 用户配置文件

  ```powershell
  # 用户配置文件：桌面上的文件，桌面背景，鼠标使用习惯，桌面图标，IE设置，数字证书，我的文档
  ```

- 只允许Guest用户访问

  ```powershell
  # 启用Guest用户
  # gpedit.msc
  # windows设置，安全设置，本地策略，安全选项，网络访问
  # 共享和存储管理
  ```

- 管理用户的密码

  ```powershell
  ctrl+alt+delete
  ```

- 网络凭据

  ```powershell
  # 镜像账号-----用户名，密码和远程主机的相同
  ```

- 网络凭据

  ```powershell
  # net use * /del
  ```

- 管理网络密码

  ```shell
  # 用户账户---> 管理凭据
  ```

- 组管理

  ```powershell
  # 
  ```

  