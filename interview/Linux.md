## 网络基础

1. OSI七层模型的分 层与作用。

   应用层	APDU	为用户提供服务，一个操作界面

   表示层	PPDU	数据提供表示	加密和压缩

   会话层	SPDU	确定是否进行网络访问

   传输层	TPDU	对报文进行分组，组装； 提供传输协议的选择；端口封装；差错校验。TCP[传输控制协议](https://baike.baidu.com/item/传输控制协议/9727741)，

   UDP[用户数据报协议。](https://baike.baidu.com/item/用户数据报协议/8535496)

   网络层	报文	ip地址编址，路由选择

   数据链路层	帧	mac编址	mac寻址 差错校验

   物理层	比特	数据实际传输

   2. 三次握手
   
   TCP包头作用
   
   序号：Seq序号，占32位，用来标识从TCP源端口向目的端口发送的字节流
   
   确认号：Ack序号，占32位，只有ACK标志位为1时，确认号才有效，ack=seq+1
   
   标志位：
   
   - URG：紧急指针（urgent pointer）有效
   - ACK：确认序号有效
   - PSH：接收方应该尽快将这个报文交给应用层
   - RST：重置连接
   - SYN：发起一个新连接
   - FIN：释放一个连接
   
   client
   
   syn_sent  SYN=1 seq=j
   
   SYN=1,ACK=1,ack=j+1,seq=k
   
   ACK=1,ack=k+1
   
   