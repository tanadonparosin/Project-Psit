
# import the time module
import time 
  
# define the countdown func. 
def countdown(t): 
    big = 0
    t += 1
    while t != big:
        hours = big//3600
        left = big%3600
        mins, secs = divmod(left, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs) 
        print(timer, end="\r")
        time.sleep(1) 
        big += 1
        
      
    print('Time Out!') 
  
  
# input time in seconds 
t = input("Enter the time to stop in seconds:")
  
# function call 
countdown(int(t))


