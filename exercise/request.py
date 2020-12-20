import requests
r=requests.get("http://www.baidu.com")
status_code=r.status_code
print(status_code)
r.encoding='utf-8'
print(r.text)