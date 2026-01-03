import requests
import re

#通过python在b站爬取音频和视频

url='https://www.bilibili.com/video/BV1nmsWexEfA/?spm_id_from=333.1387.favlist.content.click&vd_source=e31124669c1c708631bdcc9e7a3c2a02'
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0',
          'Cookie':"(在网页中找自己的Cookie)",
          'Referer':'https://www.bilibili.com/'
          }                                                     #获取b站的url和Cookie
L = requests.get(url=url,headers=headers).text          #将获取的请求打印(方便到时候利用正则寻找视频和音频的url)
print(L)

F = re.compile('"base_url":"(.*?)"',re.S)           #利用正则寻找视频和音频的url并将其打印
sourl_url = F.findall(L)
print(sourl_url)

video = sourl_url[0]                 #找到第一个视频，越靠前视频像素越高
audio = sourl_url[-2]                #第一个音频是整个url里面的倒数第二个，越靠前音质越好

video_name = 'video.mp4'             #为音频与视频命名
audio_name = 'audio.mp3'

video_data = requests.get(url=video, headers=headers)        #向获取的音频与视频单独发送请求
audio_data = requests.get(url=audio, headers=headers)

with open(video_name,'wb') as f:         #最后保存音频与视频
    f.write(video_data.content)
with open(audio_name,'wb') as f:
    f.write(audio_data.content)


