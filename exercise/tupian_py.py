#图片爬取实例
import requests
path="D:/ABC.jpg"
url="http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
r=requests.get(url)
r.status_code
with open(path,'wb') as f:
	f.write(r.content)
f.close()
