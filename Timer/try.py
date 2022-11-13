import time 
num=  int(input('set your timer at sec :  '))
while num : 
    time.sleep(num)
    op=[]
    op.append(num)
    num-=1 
exit()
