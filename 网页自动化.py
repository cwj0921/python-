from DrissionPage import ChromiumPage,ChromiumOptions
import time
import requests
import os

#查找图片，并将其下载
"""
作用：通过输入关键字，让代码自己打开Edge浏览器，并自动输入关键字，搜索，查询图片并下载到文件夹中
"""
"""
在编写代码时遇到了许多问题，比如因为浏览器的不同而导致需要导入不同的库，还有代码找不到浏览器路径需要手动更改的问题，也让我知道什么时候该使用哪个库，怎么快速找到路径
"""

name =input()  #输入图片名称
save_dir = 'Furina'   #保存图片的文件名目录
url = f'https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&lid=83183a280066d7a6&dyTabStr=MTIsMCwzLDEsMiwxMyw3LDYsNSw5&word={name}'  #搜索图片的url
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0'}

co = ChromiumOptions()      #创建浏览器对象
co.set_browser_path(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe')  #设置浏览器路径
page = ChromiumPage(addr_or_opts=co)    #创建页面对象
page.get(url)   #访问url,发送请求
time.sleep(2)   #等待2秒秒

Q = 3
for i in range(Q):   #这个是循环几次,Q为控制次数
    page.run_js('window.scrollTo(0,document.body.scrollHeight)')  #使网页自己滚动
    X = page.eles('css:.img_7rRSL')

    if not os.path.exists(save_dir):    #判断是否有保存图片的这个文件夹，如果没有就创建一个
        os.mkdir(save_dir)

    for index,element in enumerate(X):   #循环图片
        try:
           img_url = element.ele('css:img').attr('src')   #这个是获取图片的url
           C = requests.get(url=img_url,headers=headers,timeout=5)   #发出请求，下面那个是判断请求是否成功
           C.raise_for_status()
           W = str(time.time()) + f'_{i}' + '.jpg'       #给图片命名，时间戳加数字名
           J = os.path.join(save_dir,W)   #生成文件夹，用于存储图片

           with open(J,'wb') as F:                #保存图片
               F.write(C.content)
        except Exception as e:                    #这个是判断能否正常下载，是个提示
            print(f"下载失败：{e}")
            continue
page.quit()            #关闭页面