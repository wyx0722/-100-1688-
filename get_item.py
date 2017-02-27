# ecoding = utf-8
import requests
from bs4 import BeautifulSoup
import string
import time
import random
def get_items(url):
     #经过ture.py验证过的可使用代理ip,做成ip池
     tab =  [{'http': 'http://210.75.3.50:8888'},
            {'http': 'http://210.242.179.103:8080'},
             {'http': 'http://210.176.52.109:80'},
             {'http': 'http://118.193.23.162:3128'},
             {'http': 'http://211.95.6.210:80'}]



     f = open(r'test.txt', 'r')
     cookies = {}
     for line in f.read().split(';'):
          name, value = line.strip().split('=', 1)
          cookies[name] = value

     proxie = random.choice(tab)

     headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
         'referer': 'https://login.1688.com/member/marketSigninJump.htm?Done=https%3A%2F%2Fwww.1688.com%2F'}
     requests_session = requests.session()

     req = requests_session.post('https://login.1688.com/member/signin.htm', headers=headers)

     req = requests_session.get(url, cookies=cookies,proxies = proxie)

     time .sleep(2)
     soup = BeautifulSoup(req.text,'html.parser')
     phoneNumber =  soup.select('div.contcat-desc > dl:nth-of-type(1) > dd')[0].text
     name = soup.select('#site_content h4')[0].text
    # mobile = soup.select('div.contcat-desc > dl:nth-of-type(2) > dd')[0].text


     print name,phoneNumber

#get_items('https://shop1422335449813.1688.com/page/contactinfo.htm')
