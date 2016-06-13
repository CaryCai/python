import urllib
a=int(input('请输入你要下载的图片数量:'))

i=100
while i<=a:
    b='%d' %i
    i +=1
    path = r"d:/test/"+b+".jpg"
    u = r"http://www.boboporn.net/media/photos/"
    u=u+b+'.jpg'
    print '下载地址：',u,'保存位置：',path
    data = urllib.urlretrieve(u,path)
print('本程序属于 by:无敌，QQ:1239890175，大牛勿喷！')    

 
