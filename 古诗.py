# -*- coding:utf-8 -*-
import time
A=time.time()
f=open('gushi.txt','w+')
f.write('床前明月光\n疑是地上霜\n举头望明月\n低头思故乡')
f.close()
f=open('gushi.txt','r')
content=f.read()
f.close()
print(content)
def copy():
    f=open('copy.txt',"w+")
    f.write(content)
    f.close()
copy()
print('复制完成')
B=time.time()
print('用时为:'+str(B-A)+'秒')