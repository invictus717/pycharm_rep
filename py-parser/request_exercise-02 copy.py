import requests
url="https://www.amazon.cn/gp/product/B01M8L5Z3Y"
url_mooc="https://www.icourse163.org/"
url_bit="https://www.bit.edu.cn"
url_lexue="http://lexue.bit.edu.cn"
url_oschina="https://www.oschina.net/news/122922/cd-projekt-red-996"
url=url_oschina
# try:
#     r=requests.get(url_mooc)
#     r.raise_for_status()
#     r.encoding=r.apparent_encoding
#     print(r.text)
# except:
#     print("Misson failed!")

r=requests.get(url)
# print(r.status_code)
r.encoding=r.apparent_encoding
# print(r.text)

print(r.request.headers)
kv={'User-Agent':'Chrome/87.0'}
r=requests.get(url,headers=kv)
print(r.request.headers)
print(r.text[:1000])