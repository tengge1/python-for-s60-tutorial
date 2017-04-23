#作者：tengge

import re
#引入正则表达式模块
str="a&good!m_g&boy!&.am!&girl!"

p=re.compile("&[a-z]*!")
#这一句构建正则表达式。"&[a-z]*!"是一个正则表达式，意思是以“&”开头，以“!”结束，中间含任意多个小写字母
#构建表达式是最重要一步，请参照玉树临风教程

print p.findall(str)
#这个返回匹配的所有结果组成的列表，这是最重要的一个函数，其余从略

m=p.search(str)
#扫描字符串，若用“match”，则仅从开始匹配
print m.start()
#返回第一个匹配开始位置
print m.end()
#返回第一个匹配结束位置

