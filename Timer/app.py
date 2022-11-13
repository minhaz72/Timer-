import time 
def timer(time_sec): 
    while time_sec: 
        mins, secs= divmod(time_sec , 60 ) 
        timeformat='{:02d}:{:02d}'.format(mins, secs )
        print(timeformat, end='/')
        time_sec -=1 
        
        
        print("stop")
num= int(input('set your timer in sec :   '))
timer(num)