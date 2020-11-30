import os, sys
from time import sleep
from datetime import datetime
try:
    import requests
    from bs4 import BeautifulSoup
except:
  os.system("pip install requests")
  os.system("pip install bs4")
  import requests
  from bs4 import BeautifulSoup
#màu
red='\u001b[31;1m'
s=0
green='\u001b[32;1m'
blue='\u001b[34;1m'
yellow='\u001b[33;1m'
hong='\033[95m'
sky='\u001b[36m'
red2='\u001b[35m'
reset='\u001b[0m'

#Nền:
back_red='\u001b[41m'
back_green='\u001b[42m'
back_yellow='\u001b[43m'
back_blue='\u001b[44m'
os.system('clear')
print(reset+red+"[VUI LÒNG NHẬP ĐẦY ĐỦ THÔNG TIN]"+reset)
cookie = input(green+"Nhập Cookie Facebook : "+yellow)
authorization = input(green+"Nhập Authorization App : "+yellow)
delay = input(green+"Nhập Delay : "+yellow)

url_job = "https://tanglikefree.com/api/auth/Post/getpost"
head_job = {
  'Host':'tanglikefree.com',
  'X-Requested-With':'XMLHttpRequest',
  'Authorization':authorization,
  'Referer':'https://tanglikefree.com/makemoney',
}
head_fb = {
  'Host': 'mbasic.facebook.com',
  'upgrade-insecure-requests': '1',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'x-requested-with': 'com.android.browser',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-user': '?1',
  'sec-fetch-dest': 'document',
  'referer': 'https://mbasic.facebook.com/',
  'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
  'Cookie':cookie,
}
url_nhan = "https://tanglikefree.com/api/auth/creat_request"
url_login = "https://tanglikefree.com/api/auth/user"
url_request = "https://tanglikefree.com/api/auth/creat_request"
login = requests.get(url=url_login,headers=head_job)
messages = login.json()['messages']

if messages == "Success":
  os.system('clear')
  username = login.json()['data']['username']
  print(reset+back_yellow+red+" Tool Tanglikefree.com "+reset)
  print(red+"Bản Quyền : Minh Ngọc")
  print(blue+"Telegram : t.me/minhngoc2003")
  print(hong+"Group Telegram : t.me/sharetoolfree\n")
  print(reset+sky+"["+username+"]"+"\n\n"+reset)

  
  while True:
                #Check cookie
            check_cookie = requests.get(url='https://mbasic.facebook.com/',headers=head_fb)
            if "Đăng xuất" not in check_cookie.text:
              exit(reset+red+"Cookie Die                             "+reset)
              
            try:
              a = requests.get(url=url_nhan,headers=head_job)
              
              
              #Like Post
              request_id = a.json()['request_id']
              wed = requests.get(url=url_job,headers=head_job)
              id_fb = wed.json()[0]['idpost']
              wed_fb = requests.get("http://mbasic.facebook.com/"+str(id_fb), headers=head_fb)
              soup = BeautifulSoup(wed_fb.text,"html.parser")
              tìm = soup.find_all("meta",content=True)
              for i in tìm:
                link = i['content']
                if "https://www.facebook.com/story.php?" in link:
                  wed2 = requests.get(link, headers=head_fb)
                  soup2 = BeautifulSoup(wed2.text,"html.parser")
                  tìm2 = soup2.find_all("a",href=True)
                  for u in tìm2:
                    link2 = u['href']
                    if "/a/like.php?" in link2:
                      a=requests.get("https://mbasic.facebook.com/"+link2,headers=head_fb)
                elif "https://www.facebook.com/photo.php? " in link:
                  wed3 = requests.get(link, headers=head_fb)
                  soup3 = BeautifulSoup(wed3.text,"html.parser")
                  tìm3 = soup3.find_all("a",href=True)
                  for ui in tìm3:
                    link3 = ui['href']
                    if "/a/like.php?" in link3:
                      b=requests.get("https://mbasic.facebook.com/"+link3,headers=head_fb)
              data_nhan = {"idpost":id_fb,"request_id":request_id}
              wed_nhan = requests.post(url="https://tanglikefree.com/api/auth/Post/submitpost",headers=head_job,data=data_nhan)
              nhan = wed_nhan.json()['messages']
              vi = requests.get(url="https://tanglikefree.com/api/auth/user",headers=head_job)
              ví = vi.json()['data']['VND']
              
              
              if "Bạn Đã Nhận 40Đ Vào Tài Khoản" in nhan:
                s = s+1
                now = datetime.now()
                time_now =now.strftime("%X")
                print(reset+blue+"["+str(s)+"]"+reset+" • "+reset+sky+"["+time_now+"]"+reset+" • "+reset+green+"[LIKE]"+reset+" • "+reset+red2+id_fb+reset+" • "+reset+green+"+40Đ"+reset+" • "+reset+yellow+str(ví)+reset)
                sleep(1)
                for i in range(int(delay),-1,-1):
                  print(reset+red+"Vui Lòng Đợi",i,"Giây Delay!",end=" \r"+reset)
                  sleep(1)
                  
                  
              elif "Bạn Đã Nhận 41Đ Vào Tài Khoản" in nhan:
                s = s+1
                now = datetime.now()
                time_now =now.strftime("%X")
                print(reset+blue+"["+str(s)+"]"+reset+" • "+reset+sky+"["+time_now+"]"+reset+" • "+reset+green+"[LIKE]"+reset+" • "+reset+red2+id_fb+reset+" • "+reset+green+"+41Đ"+reset+" • "+reset+yellow+str(ví)+reset)
                sleep(1)
                for i in range(int(delay),-1,-1):
                  print(reset+red+"Vui Lòng Đợi",i,"Giây Delay!",end=" \r"+reset)
                  sleep(1)
                  
                  
              else:
                for i in range(int(delay),-1,-1):
                  print(reset+red+"Vui Lòng Đợi",i,"Giây Delay!",end=" \r"+reset)
                  sleep(1)
            except:
              pass
                
              #Like Page
            try:
              url_request_page = requests.get(url="https://tanglikefree.com/api/auth/creat_request",headers=head_job)
              request_id_page = url_request_page.json()['request_id']
              job_page = requests.get(url="https://tanglikefree.com/api/auth/Page/getpage",headers=head_job)
              idpage = job_page.json()[0]['idpage']
              wed_page = requests.get("https://mbasic.facebook.com/profile.php?id="+idpage,headers=head_fb)
              soup_page = BeautifulSoup(wed_page.text, "html.parser")
              tim_page = soup_page.find_all("a",href=True)
              for ipage in tim_page:
                page = ipage['href']
                if "/a/profile.php?" in page:
                  requests.get("https://mbasic.facebook.com"+page,headers=head_fb)
              data_page = {"idpage":idpage,"request_id":request_id_page}
                
                
              nhan_page = requests.post(url="https://tanglikefree.com/api/auth/Page/submitpage",headers=head_job,data=data_page)
              message_page = nhan_page.json()['messages']
              vi = requests.get(url="https://tanglikefree.com/api/auth/user",headers=head_job)
              ví = vi.json()['data']['VND']
                        
                        
              if "Bạn Đã Nhận 60Đ" in message_page:
                s = s+1
                now = datetime.now()
                
                time_now =now.strftime("%X")
                print(reset+blue+"["+str(s)+"]"+reset+" • "+reset+sky+"["+time_now+"]"+reset+" • "+reset+green+"[PAGE]"+reset+" • "+reset+red2+idpage+reset+" • "+reset+green+"+60Đ"+reset+" • "+reset+yellow+str(ví)+reset)
                sleep(1)
                  
                  
                for i in range(int(delay),-1,-1):
                  print(reset+red+"Vui Lòng Đợi",i,"Giây Delay!",end=" \r"+reset)
                  sleep(1)
              else:
                for i in range(int(delay),-1,-1):
                  print(reset+red+"Vui Lòng Đợi",i,"Giây Delay!",end=" \r"+reset)
                  sleep(1)
            except:
              pass
else:
  exit(reset+red+'Sai Thông Tin Xin Nhập Lại!'+reset)