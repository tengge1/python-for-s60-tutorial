
import inbox

box=inbox.Inbox()

id=box.sms_messages()
#这个返回收件箱中所有短信地址（id号）组成的列表

box.set_unread(id[0],1)
#这个将收件箱中第一条短信设为未读，1为设为未读，0为设为已读

#其余请参照《tenggePy教程》合集2