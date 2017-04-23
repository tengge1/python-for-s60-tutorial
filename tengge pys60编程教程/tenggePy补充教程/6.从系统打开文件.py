import appuifw
handler=appuifw.Content_handler()
#生成Content_handler实例
handler.open("z:\\data\\startup_tone.aac")
handler.open_standalone(u"z:\\data\\startup_tone.aac")
#从系统以独立进程打开文件
