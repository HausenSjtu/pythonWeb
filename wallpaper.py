import urllib2
import urllib
import re
import os
from PIL import Image
import cStringIO



path = os.getcwd()

for j in range (1,2):
       web = urllib2.urlopen('https://yande.re/post?page='+str(j)+'&tags=wallpaper')
       content = web.read()
       pics = re.findall(r'https://files.*?jpg',content)
       
       for i in range (1):#(len(pics)):
              pic = pics[i]
              file = urllib2.urlopen(pic)
              tmpIm = cStringIO.StringIO(file.read())
              print tmpIm
              im = Image.open(tmpIm)
              print im
              if pic.find('sample')==-1:
                     urllib.urlretrieve(pic, 'F:\\pics\\'+str(j)+'p_'+str(i)+'.jpg')


print 'complete~'

##f = file('wallpaper.html','w')
##f.write(content)
##f.close()
