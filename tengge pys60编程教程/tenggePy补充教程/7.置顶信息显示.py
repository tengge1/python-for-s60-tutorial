import appuifw
import e32
info=appuifw.InfoPopup()
info.show(u"hello",(20,20),2000,1000,appuifw.EHLeftVCenter)
#其中仅有第一个参数即可，u"hello"显示的文字，(20,20)控件显示位置，第三个参数是显示时间，第四个参数是弹出前等待时间，最后一个有以下几种
#appuifw.EHLeftVTop左对齐顶端对齐
#appuifw.EHLeftVCenter左对齐垂直方向居中
#appuifw.EHCenterVTop水平居中，垂直顶端
#等等
