import requests
r=requests.get("http://www.baidu.com")
print(r.status_code)
r.encoding=r.apparent_encoding
print(r.encoding)
print(r.text)