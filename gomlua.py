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
s=0
os.system('clear')
print(red+"[VUI LÒNG NHẬP ĐẦY ĐỦ THÔNG TIN]")
cookie = input(reset+green+"Nhập Cookie Facebook : "+yellow)
token = input(reset+green+"Nhập Token App : "+yellow)
sleep(1)
os.system('clear')
url_job = "https://gomlua.com/cpi/listCampaignFacebook?os=web&type=like_post"
headgl = {
  'Host':'gomlua.com',
  'app_token':token,
  'Referer':'https://gomlua.com/',
}
headfb = {
  'Host':'mbasic.facebook.com', 
'upgrade-insecure-requests':'1',
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'navigate',
'sec-fetch-user':'?1',
'sec-fetch-dest':'document', 
'referer':'https://mbasic.facebook.com/',
'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
'Cookie':cookie,
}
print(reset+back_yellow+red+" TOOL GOM LÚA "+reset)
print(red+"Bảng Quyền : Minh Ngọc")
print(blue+"Telegram : t.me/minhngoc2003")
print(hong+"Group Telegram : t.me/sharetoolfree\n\n")
try:
  while True:
    #Check Cookie
    check_cookie = requests.get(url='https://mbasic.facebook.com/',headers=headfb)
    if "Đăng xuất" not in check_cookie.text:
      exit("Cookie Die                             ")
    #Load Job
    job = requests.get(url=url_job,headers=headgl)
    tim = job.json()['data']['list'][0]['campaign_url']
    link_id = job.json()['data']['list'][0]['link_id']
    loai = job.json()['data']['list'][0]['react_type']
    id_fb = job.json()['data']['list'][0]['campaign_id']
    #Check Job
    check = requests.get(url="https://gomlua.com/likeToken/checkLikeToken?os=web&link_id="+str(link_id),headers=headgl)
    error_check = check.json()['message']
    if error_check == "Thanh cong":
      sua_link = tim.replace("www","mbasic")
      wed = requests.get(url=sua_link,headers=headfb)
      soup = BeautifulSoup(wed.text,"html.parser")
      tim2 = soup.find_all("a",href=True)
      for i in tim2:
        link = i['href']
        if "/reactions/picker/?" in link:
          camxuc = requests.get("https://mbasic.facebook.com"+link, headers=headfb)
          soup2 = BeautifulSoup(camxuc.text, "html.parser")
          timcx = soup2.find_all("a", href=True)
          listcx = []
          for laycamxuc in timcx:
            tachcx = laycamxuc['href']
            listcx.append(tachcx)
          if loai == "LIKE":
            list_cx = listcx[1]
          if loai == "LOVE":
            list_cx = listcx[2]
          if loai == "CARE":
            list_cx = listcx[3]
          if loai == "HAHA":
            list_cx = listcx[4]
          if loai == "WOW":
            list_cx = listcx[5]
          if loai == "SAD":
            list_cx = listcx[6]
          if loai == "ANGRY":
            list_cx = listcx[7]
          requests.get("https://mbasic.facebook.com"+list_cx,headers=headfb)
          nhan_tien = requests.get(f"https://gomlua.com/likeToken/likeSuccess?os=web&link_id={link_id}&like_count=1",headers=headgl)
          message_nhan_tien = nhan_tien.json()['message']
          if "Chúc mừng bạn nhận được" in message_nhan_tien:
            vi = nhan_tien.json()['data']['current_paddy']
            s=s+1
            now = datetime.now()
            time_now =now.strftime("%X")
            print(reset+blue+"["+str(s)+"]"+reset+" • "+green+"【"+reset+time_now+green+"】"+reset+" • "+green+loai+reset+" • "+red2+str(link_id)+reset+" • "+green+"+35"+reset+" • "+yellow+str(vi)+reset+" • "+green+"[√]")
          else:
            s1=0
            while (s1<5):
              s1=s1+1
              nhan_tien = requests.get(f"https://gomlua.com/likeToken/likeSuccess?os=web&link_id={link_id}&like_count=1",headers=headgl)
              message_nhan_tien = nhan_tien.json()['message']
              sleep(1)
              if "Chúc mừng bạn nhận được" in message_nhan_tien:
                vi = nhan_tien.json()['data']['current_paddy']
                s=s+1
                now = datetime.now()
                time_now =now.strftime("%X")
                print(reset+blue+"["+str(s)+"]"+reset+" • "+green+"【"+reset+time_now+green+"】"+reset+" • "+green+loai+reset+" • "+red2+str(link_id)+reset+" • "+green+"+35"+reset+" • "+yellow+str(vi)+reset+" • "+green+"[√√]")
                break
    for i in range(5,-1,-1):
      print(reset+red+"Đang Tìm Job...",end=" \r"+reset)
      sleep(1)
except:
  exit(reset+red+'Die Token                  '+reset)