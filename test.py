import re
import cv2
##import numpy
import urllib2
import urllib
import cStringIO
import os



r = urllib2.Request('https://www.google.com')
f = urllib2.urlopen(r, data=None, timeout=3)
result =  f.read()
print result







##z='hi,ni\\ hao'
##print z.replace('\\','\\\\')
##print z

##w='absba123'
##a='zhsth_uy_zhshe'
##b = re.findall(r'.*_(?!sa).*_.*?',a)
##print b



##
##i=10
##l=['0','1','2']
##a=10/15.0
##a=round(a,2)
##print a




##im = cv2.imread('5p_14.jpg')
##h,w = im.shape[0:2]
##print h
##print w
####os.remove('1p_5.jpg')
