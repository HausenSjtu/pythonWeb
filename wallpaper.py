import urllib2
import urllib
import re
import os
import cv2
##from PIL import Image
##import cStringIO

startPage = 5
endPage = 5


path = os.getcwd()

for j in range (startPage,endPage+1):
       web = urllib2.urlopen('https://yande.re/post?page='+str(j)+'&tags=wallpaper')
       content = web.read()
       pics = re.findall(r'https://files.*?jpg',content)
       
       for i in range (len(pics)):
              pic = pics[i]
##              file = urllib2.urlopen(pic)
##              tmpIm = cStringIO.StringIO(file.read())
##              print tmpIm
##              im = Image.open(tmpIm)
##              print im
              if pic.find('sample')==-1:
                     fileName = path+'\\pics\\'+str(j)+'p_'+str(i)+'.jpg'
                     urllib.urlretrieve(pic, fileName)
                     img = cv2.imread(fileName)
                     h, w = img.shape[0:2]
                     if h > w:
                            os.remove(fileName)
                     pec = ((j-startPage)+min([i,20])/20.0)/(endPage-startPage+1)
                     pec *=100
                     pec = round(pec,0)
                     print 'mission completed\t'+str(pec)+'%'
                            
                     


print 'all ok~'

##f = file('wallpaper.html','w')
##f.write(content)
##f.close()
