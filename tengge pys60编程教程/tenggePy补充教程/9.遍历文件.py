#遍历文件就是找出某一目录下所有文件。在做音乐播放器找出所有mp3文件时很有效。
import os

def walk(a,d,f):
    print a,d,f
os.path.walk("e:\\Images\\",walk,None)

#说明：None是每执行一次os.path.walk所调用的函数，这里我们让它什么也不调用。
#"e:\\Images"这是要遍历的目录，建议测试代码时找一个较小的目录
#walk这是os.path.walk获得的信息所调用的函数，它需要有三个参数
#下面我们对walk的三个参数进行说明：
#a：这个返回os.path.walk第二个函数执行结果。
#d：这个返回"e:\\Images"的某子目录（及所在的文件夹）
#f:这个返回文件夹中所有文件组成的列表
#用遍历文件，再配合endswith等就可以找出某一路径下某一类型文件！
