import requests
url="https://www.cnblogs.com/cjj-zyj/p/10033000.html"
import os
root="D://week_15_assign//"
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.makedirs(root)
    if not os.path.exists(path):
        kv={'User-Agent':'Chrome/87.0'}
        r=requests.get(url,headers=kv)
        r.encoding=r.apparent_encoding
        with open(path,'wb') as f:
            f.write(r.content)
            f.close
            print("Download Success!")
    else:
        print("It has existed!")
except:
    print("Mission failed!")