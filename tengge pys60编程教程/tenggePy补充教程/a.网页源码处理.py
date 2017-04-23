#作者：tengge

#请先将一个网页源码以utf8编码保存为“c:\\1.txt”，推荐用“tengge记事本”软件（在哇麦python论坛下载）

file=open("c:\\1.txt")
data=file.read().decode("utf8")
file.close()

import HTMLParser
parser=HTMLParser.HTMLParser()
result=[]#定义一个列表，用来存放处理结果

parser.handle_data=result.append
#将“handle_data”换为以下内容，result就得到以下结果：
#handle_data网页中文字列表(unicode编码)
#handle_decl网页头网址列表
#handle_endtag后标签内容列表
#handle_entityref网页格式控制标记列表
#handle_pi XML版本

parser.feed(data)#data是所要处理的数据
parser.close()
print result

#下面我们来看其他处理：
result1=[]
result2=[]
def handler(a,b):
    result1.append(a)
    result2.append(b)
parser.handle_starttag=handler
#将“handle_starttag”换为以下内容，result1,result2就得到以下结果：
#handle_starttag:result1是所有标签名列表，result2由许多子列表组成，子列表由许多元组组成，元组前者是标签名的属性，后者是对应属性的值，如：
#(u'href', u'http://waphi.baidu.com/')，href是超链接标记（a）的属性，其值为u'http://waphi.baidu.com/'

parser.feed(data)#data是所要处理的数据
parser.close()
print result1
print result2
