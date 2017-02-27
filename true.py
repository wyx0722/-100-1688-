import requests

try:
    将ip替换到进去，运行即可知道ip是否可用
    requests.get('http://wenshu.court.gov.cn/', proxies={'http': 'http://211.95.6.210:80'})
except:
    print 'connect failed'
else:
    print 'success'
