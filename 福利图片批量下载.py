import urllib
a=int(input('��������Ҫ���ص�ͼƬ����:'))

i=100
while i<=a:
    b='%d' %i
    i +=1
    path = r"d:/test/"+b+".jpg"
    u = r"http://www.boboporn.net/media/photos/"
    u=u+b+'.jpg'
    print '���ص�ַ��',u,'����λ�ã�',path
    data = urllib.urlretrieve(u,path)
print('���������� by:�޵У�QQ:1239890175����ţ���磡')    

 
