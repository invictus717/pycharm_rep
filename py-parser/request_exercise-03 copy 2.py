import requests
url="http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
import os
root="D://IBIT//"
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.makedirs(root)
    if not os.path.exists(path):
        r=requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("Download Success!")
    else:
        print("It has existed!")
except:
    print("Mission failed!")