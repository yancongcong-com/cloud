# VPN

## PPTP

- 比较基础和简单的VPN协议，支持TCP/IP网络
- 使用1723端口
- 加密是使用PPP内置MPPE加密协议（128加密）
- 适用于Client-to-Site和Site-to-Site的类型

## L2TP

- 是PPTP升级的一个协议，除了支持TCPI/IP网络，还支持Frame-Relay，x.25等网络
- 使用1701端口
- 使用IPSEC协议进行加密和身份验证，更加安全
- 适用于Site-to-Site的类型

## SSTP

- 是windows 2008 R2之前新支持的功能
- 使用443端口
- 加密使用SSL协议
- 适用于Client-to-Site的类型

