import appuifw
import e32
sleep=e32.ao_sleep
lock=e32.Ao_lock()
appuifw.app.body=t=appuifw.Text()
t.add(u"hello,i am tengge.")
t.set_pos(t.get_pos()-1)
#get_pos()获取光标位置，set_pos，设置光标位置
sleep(1)#暂停1秒，以便看清效果
t.delete(t.len()-6)
#len()获取文本长度，delete(n)，从光标处删除长度为n的文字
sleep(1)
t.add(u"a good boy")
sleep(1)
def r():
    t.add("\n")
#此处定义了一个像回车那样的函数。即在光标处添一个换行附。
t.bind(63557,r)#将函数绑定在确定键上
r()
t.add(t.get(6,11))
#t.get(6,11)即获取第6个到十一个字符。
sleep(1)
t.clear()
t.add(u"cabbagecabbage")
pos=0
while pos!=-1:
    pos=t.get().find(u"a",pos+1)
    t.set_pos(pos)
    sleep(1)
#find(u"a",pos+1)的意思是找的pos以后的第一个u"a"的位置。
#如u"calculate".find(u"a",2)返回的是第二个a的位置6

appuifw.app.exit_key_handler=lock.signal
lock.wait()
