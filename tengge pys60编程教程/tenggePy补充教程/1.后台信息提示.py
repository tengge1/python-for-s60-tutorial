#后台提示信息
import appuifw

def aa(fg):
    if fg==0:
        appuifw.note(u"bg","info",1)

print "请将程序转入后台".decode("utf8")
appuifw.app.focus=aa
#要想在后台提示信息，只需在appuifw.note加入一个非零参数即可。
