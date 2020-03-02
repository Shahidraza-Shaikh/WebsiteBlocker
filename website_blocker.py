from  datetime import datetime as  dt 
import time
website_list=['www.google.com','www.facebook.com','www.facebook.com','www.youtube.com','www.news.google.com/']
# host_temp=r'hosts'
start_clg_time =dt(dt.now().year ,dt.now().month,dt.now().day,8) # 8 is Hours 
end_clg_time= dt(dt.now().year ,dt.now().month,dt.now().day,19,11) # 19 is Hours and 11 minutes
host_window =r'C:\Windows\System32\drivers\etc\hosts' #for Linux -- r'etc/hosts'
redirect ='127.0.0.1'
while True :
    if (start_clg_time < dt.now() < end_clg_time):
        with open(host_window,'r+') as file :
            content =file.read()
            for website in website_list:
                if website in  content:
                    pass
                else:
                    file.write(redirect +"  "+ website+'\n')
    else:
        with open(host_window ,'r+') as file :
            content =file.readlines()
            file.seek(0)
            for line  in content:
                if not any( website in line for website in website_list):
                    file.write(line)
                file.truncate()
        break
    time.sleep(1)