import requests

try:
    requests.get('http://wenshu.court.gov.cn/', proxies={'http': 'http://211.95.6.210:80'})
except:
    print 'connect failed'
else:
    print 'success'
