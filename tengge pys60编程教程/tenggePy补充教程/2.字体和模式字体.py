import appuifw
import e32
lock=e32.Ao_lock()

appuifw.app.body=t=appuifw.Text()
t.add(unicode(appuifw.available_fonts())+"\n")
#appuifw.availablefonts()获得手机可用字体，返回一个列表，如[u'Sans MT 936_S60', u'Series 60 ZDigi']

t.font=appuifw.available_fonts()[0]
#设置为可用字体的第一个字体
t.add(u"hello"+"\n")
t.font="title"
#定义模式字体，可选title,legend,symbol,dense,normal,annotation
t.add(u"hello"+"\n")
appuifw.app.exit_key_handler=lock.signal
lock.wait()
