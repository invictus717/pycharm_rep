#这里是网页爬取的通用框架；
import requests
def gethtmltext(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "Error Happened"
if __name__=='__main__':
    url="http://www.baidu.com"
    print(gethtmltext(url))

# 以下是相关资源性修改的方式,其实呢是一个建议的json的信息标记
# payload={'key1':'value1','key2':'value2'}
# r=requests.post('http://httpbin.org/post',data=payload)
# print(r.text)
# r=requests.post(url=,data=,json=,**kwargs=)