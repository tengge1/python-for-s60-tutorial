#本节除介绍了camera模块，还介绍一个重要函数blit的参数，很重要！

import e32, camera, appuifw, key_codes#camera是拍照摄像模块

def viewfinder(img):#将img绘在画布上
    canvas.blit(img)

def shoot():#拍照
    camera.stop_finder()#照相前要停止取景框
    photo = camera.take_photo(size = (640, 480))
    w, h = canvas.size#取得画布大小
    canvas.blit(photo, target = (0, 0, w, 0.75 * w),source=(0,0,640,480),mask=None,scale = 1)
    #photo图像，target在画布上画得位置，source截取原图像的位置，mask=None为无遮照，mask=1为黑色遮照，scale=0为截取，scale=1为缩放
    photo.save('c:\\photo.jpg')

def quit():
    camera.stop_finder()
    app_lock.signal()

appuifw.app.body = canvas = appuifw.Canvas()
appuifw.app.title = u"Camera"
appuifw.app.exit_key_handler = quit

camera.start_finder(viewfinder)
#启动取景器，并将取得的图片付给函数viewfinder
canvas.bind(key_codes.EKeySelect, shoot)
#将“照相”绑定在确定键上
app_lock = e32.Ao_lock()
app_lock.wait()

#其中，take_photo是可以具有很多参数的，如，photo = camera.take_photo(mode="RGB12",size = (640, 480),flash=None,zoom=0,exposure="auto",whitebalance="auto",position=0)
#参数一：图像模式，有“RGB16”“RGB12”“RGB”等
#参数二：照片像素
#参数三：None无闪光，"auto"自动闪光，"forced"强闪光
#参数四：设定变焦次数，如0,1,2
#参数五：曝光模式，"auto"自动曝光，"backlight"背光模式，"center"特写模式
#参数六：白平衡，"auto"自动，"daylight"日光，"cloudy"阴天，"fluorescent"荧光灯，"flash"闪光灯
#参数六：指定摄像头是哪一个
