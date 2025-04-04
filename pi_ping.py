import os
import datetime
import subprocess
import time
def check_status():
   ip = "172.23.38.83"
   #response = os.system(f"ping -c 10 {ip}")
   response = subprocess.call(['ping','-c','10',ip])
   print('++++++++++++++++')
   print(response)
    
   if response == 0:
       print("pi@" ,ip, ": Online")
       return True
   else:
       print("pi@" ,ip, ": Offline")
       return False


def create_token(status):
   filename='/Users/nahumyonas/pi_ping.py/status_log.txt'#one file to log all data
   if status==True:
       statustr='1'
   else:
       statustr='0'


   with open(filename, 'a+') as f:
       timestr=str(datetime.datetime.now())
       message=timestr+' '+statustr+'\n'
       f.write(message)
  
  
t_result=check_status()
create_token(t_result)

while True:
    check_status()
    time.sleep(2700)


