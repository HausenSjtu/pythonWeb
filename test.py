import re

##z='hi,ni\\ hao'
##print z.replace('\\','\\\\')
##print z

w='absba123'
a='zhsth_uy_zhshe'
b = re.findall(r'.*_(?!sa).*_.*?',a)
print b
