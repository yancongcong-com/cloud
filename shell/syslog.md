# Syslog

## 日志级别

none：不记录日志
debug：调试信息，系统进行调试时产生的日志，不属于错误日志，不需要过多关注。
info：一般的通知信息，用来反馈系统的当前状态给当前用户。
notice：提醒信息，需要检查一下程序了，不理会可能会出现错误。
warning：警告信息，当出现警告时，你的程序可能已经出现了问题，但不影响程序正常运行，尽快进行处理，以免导致服务宕掉。
error：错误信息，出现这一项时，已经挑明服务出现了问题，服务都无法确认是否能正常运行。
critical：比较严重的错误信息，服务已经宕了，可能已经无法修复。
alert：警报信息，需要立即采取行动，不仅是服务宕了，还会影响系统的正常启动。
emerg：紧急信息，系统可能已经不能使用了，如果不能解决，就重新装机吧。

## 子系统：factility，设施

### 动作：

### 服务：syslogd ,klogd

