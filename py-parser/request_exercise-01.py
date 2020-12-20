import requests
url="http://item.jd.com/2967929.html"
try:
    r=requests.get(url)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text)
except:
    print("Misson failed!")

# print(r.text[:1000])
#返回的脚本是什么意思呢？