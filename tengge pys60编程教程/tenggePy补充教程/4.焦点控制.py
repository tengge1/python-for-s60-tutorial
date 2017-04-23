#焦点控制，可实现程序前后台不同动作。

import appuifw
def aa(fg):
    if fg:
        print "fg"
    else:
        print "bg"
appuifw.app.focus=aa

#当程序在前台时输出“fg”，后台时输出“bg”，我们可借用这一功能，实现在前后台让程序进行不同操作。例如游戏转入后台后，自动将游戏暂停。
