# ecoding = utf-8
from bs4 import BeautifulSoup
import requests
import time
from get_item import get_items


start_url = 'https://s.1688.com/company/company_search.htm?keywords=%B0%A2%C0%EF%B0%CD%B0%CD&earseDirect=false&button_click=top&n=y&pageSize=30&offset=0&beginPage='
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'cookie':'cna=eFeaEIaW9WwCAXTi2ZJozrXc; ali_beacon_id=101.45.157.218.1487765062630.564036.2; ali_apache_track="c_ms=1|c_mid=b2b-2035952963|c_lid=%E6%9C%80%E7%88%B1%E5%BD%93%E5%B9%B4%E8%8D%89%E8%8E%93"; JSESSIONID=8L78Tnon1-PI1XKWPpfqehQQls66-IXrJFCQ-AxEz; ali_apache_tracktmp="c_w_signed=Y"; _is_show_loginId_change_block_=b2b-2035952963_false; _show_force_unbind_div_=b2b-2035952963_false; _show_sys_unbind_div_=b2b-2035952963_false; _show_user_unbind_div_=b2b-2035952963_false; __cn_logon__=true; __cn_logon_id__=%E6%9C%80%E7%88%B1%E5%BD%93%E5%B9%B4%E8%8D%89%E8%8E%93; cn_tmp="Z28mC+GqtZ3AtvVX0XXyYHDRuQkf7/LB3K31woS+eMO0zpxEA/S3gvJbbCnRhbyy43Bqm7ltw+KSC0uKpcoypQj36I/cdykVj5m92Wb3Uc9T7tnu3dvcxadMpDbz3it7IgDEwRjkSp4eSago+ZZMZowgOak6gQ3Qzr/IUbWPxY9wWwtSQTi4CZ/LSmcWaUbVH9LgsfliNFAD6Tcffe7jmOiGAcfL+yIzGIaDR4ObDWkeNt8WZ1SuJok3ftxr8YEj"; _cn_slid_=8h83kntJUw; tbsnid=Znlkc5w29IHMI8fT6uOyG4eO1NA%2BtWxEEmxTeHBOEPg6sOlEpJKl9g%3D%3D; LoginUmid="Vx8PNph%2FVvxTnIEWMhLqch8uOPRPsiKa%2BJxUbqUREcsogBSl%2FbuCDg%3D%3D"; userID="MvcgkvrxS49H7XoKBMITnEMfCaBrcWWH23lPLFlxeNs6sOlEpJKl9g%3D%3D"; last_mid=b2b-2035952963; unb=2035952963; __last_loginid__="%E6%9C%80%E7%88%B1%E5%BD%93%E5%B9%B4%E8%8D%89%E8%8E%93"; login="kFeyVBJLQQI%3D"; _csrf_token=1488035835446; h_keys="%u963f%u91cc%u5df4%u5df4#%u5e7f%u5dde%u6069%u9edb%u670d%u9970%u6709%u9650%u516c%u53f8#%u5e7f%u5dde%u5e02%u767d%u4e91%u533a%u5b9d%u5c71%u5236%u8863%u5382#%u4e1c%u839e%u5e02%u6b27%u7eaf%u670d%u9970%u6709%u9650%u516c%u53f8#%u5434%u6c5f%u6da6%u8302%u7eba%u7ec7%u6709%u9650%u516c%u53f8#%u745e%u5b89%u5e02%u5146%u4e30%u670d%u88c5%u7ecf%u8425%u90e8"; ad_prefer="2017/02/25 23:49:12"; ali_ab=101.45.157.218.1487763743824.5; alicnweb=touch_tb_at%3D1488038171447%7Clastlogonid%3D%25E6%259C%2580%25E7%2588%25B1%25E5%25BD%2593%25E5%25B9%25B4%25E8%258D%2589%25E8%258E%2593%7Cshow_inter_tips%3Dfalse; _ITBU_IS_FIRST_VISITED_=n; userIDNum="jg5Oc530dpGtiK1OUFbbBg%3D%3D"; _nk_="0CoTItfKbkJRQF2ASkaf1g%3D%3D"; __rn_alert__=false; l=AnZ2kzy-qkGZ4EQvejdKeI2yRqZ4tLrR; isg=AtPTBtNPj0u4bUODDAVpqnoJYle5u2dK-xbBhoXwDPIpBPOmDFj3mjFWSMeW; _tmp_ck_0="HCGgddy%2F7BCpxElsrViZD2UzMOqC0RmZeCnnMjD1tpAyqryaUOoyRAv3rXR3u7eTKAq7T%2F5Ys1ERZs5DWkR8XADWgLJMvXhl%2BqEagyZ31aqQ09DqqImPfQNuxHq7B1KlIAgnXlcXEZZW7WMLHuGvmVHeM1BdWAk1H82TDw8J4QTtlIEQilcdy2xYpF2%2Fd%2BJPBhGyRqTjjUPwwcseTsyqyYeAaclXTJI2F5tkKo98%2BuCXMIIUmH6h3f%2FnOQUTutslxL%2BuctE98oM3hYHt7cjG4I4mJknQk1tgHhnV7aGL%2BO8R7RKx%2Bm3iW3S9mWuUPWZVz0JjxDowtinZHsfHuhaHykbUpzmw9NYtGqawDxHVdbnNvc3JFjCXd0BfVKDrItpQ7JbXTmuWcXaGmxikgnxToTn53fIQWSi4P14SL0viRP%2FX9s7NoNX4eN5oOI0Yk9YKrRj8mXkJhQiAHVsbQxiJG9E0zC9bxUbF1gbI0wYGbCgNjhH7gOMDRwC%2FJjInGt2Plt8gYTlZg7xUXboNlEYjGCAqBxFPaOkXE%2BiVnvwtTSY%3D"'}
def get_channel(start_url):

    for pages in range(1,6):
            channel_url = '{}{}'.format(start_url,str(pages))
           # requests.proxies = {'http': u'http://60.179.40.16:808'}
            web_data = requests.get(channel_url,headers =headers)
            time.sleep(1)
            soup = BeautifulSoup(web_data.text, 'html.parser')
            links = soup.select('a.list-item-title-text')
            for link in links:
                page_url = link.get('href')

                print page_url+'/page/contactinfo.htm'         # print links
#下面是用上面的代码获取到的所有链接，你可以通过增加pages数，增加链接个数
links_list ='''
https://shop1447778988193.1688.com/page/contactinfo.htm
https://ziyipretty.1688.com/page/contactinfo.htm
https://shop1433609610819.1688.com/page/contactinfo.htm
https://shop1435078475325.1688.com/page/contactinfo.htm
https://3gsmartwatch.1688.com/page/contactinfo.htm
https://nishabeidi.1688.com/page/contactinfo.htm
https://youpsunny.1688.com/page/contactinfo.htm
https://fantiow.1688.com/page/contactinfo.htm
https://mflanz.1688.com/page/contactinfo.htm
https://chenyanshizhuang.1688.com/page/contactinfo.htm
https://hoyugo.1688.com/page/contactinfo.htm
https://shop1431104701726.1688.com/page/contactinfo.htm
https://yueyuexinfs.1688.com/page/contactinfo.htm
https://gegetuxia.1688.com/page/contactinfo.htm
https://shop1448384033655.1688.com/page/contactinfo.htm
https://shop1456419548895.1688.com/page/contactinfo.htm
https://ssyr168.1688.com/page/contactinfo.htm
https://wang186866.1688.com/page/contactinfo.htm
https://shop1395124396220.1688.com/page/contactinfo.htm
https://tree1688.1688.com/page/contactinfo.htm
https://youvsunny.1688.com/page/contactinfo.htm
https://chanmoc.1688.com/page/contactinfo.htm
https://pengzhuli85.1688.com/page/contactinfo.htm
https://shop1393935148664.1688.com/page/contactinfo.htm
https://zhenshuaifushi.1688.com/page/contactinfo.htm
https://neatkids.1688.com/page/contactinfo.htm
https://shop1481215923560.1688.com/page/contactinfo.htm
https://jinran86.1688.com/page/contactinfo.htm
https://shop1430732291659.1688.com/page/contactinfo.htm
https://oulie88.1688.com/page/contactinfo.htm
https://shop1400691569631.1688.com/page/contactinfo.htm
https://2016fz.1688.com/page/contactinfo.htm
https://kimi201406.1688.com/page/contactinfo.htm
https://xcone.1688.com/page/contactinfo.htm
https://unigood.1688.com/page/contactinfo.htm
https://taotee.1688.com/page/contactinfo.htm
https://znfs188.1688.com/page/contactinfo.htm
https://shop1455712883813.1688.com/page/contactinfo.htm
https://mdask1906.1688.com/page/contactinfo.htm
https://dgxili.1688.com/page/contactinfo.htm
https://lanyiyu.1688.com/page/contactinfo.htm
https://dianlanfengbiao.1688.com/page/contactinfo.htm
https://shop1437670158376.1688.com/page/contactinfo.htm
https://hsstore.1688.com/page/contactinfo.htm
https://lemafushi.1688.com/page/contactinfo.htm
https://shop1442073273245.1688.com/page/contactinfo.htm
https://hanguoyiguansy.1688.com/page/contactinfo.htm
https://ssay1992.1688.com/page/contactinfo.htm
https://shop1433438178740.1688.com/page/contactinfo.htm
https://shop1456159907399.1688.com/page/contactinfo.htm
https://shop1450198615800.1688.com/page/contactinfo.htm
https://shop1468601410566.1688.com/page/contactinfo.htm
https://haoting1.1688.com/page/contactinfo.htm
https://shop1459357710455.1688.com/page/contactinfo.htm
https://shop1431708927498.1688.com/page/contactinfo.htm
https://pokwai.1688.com/page/contactinfo.htm
https://mygzpffs.1688.com/page/contactinfo.htm
https://rihanjia.1688.com/page/contactinfo.htm
https://shop1467306350212.1688.com/page/contactinfo.htm
https://honghongfushi.1688.com/page/contactinfo.htm
https://shop1429109913114.1688.com/page/contactinfo.htm
https://deo1688.1688.com/page/contactinfo.htm
https://ivy1688.1688.com/page/contactinfo.htm
https://womensvip.1688.com/page/contactinfo.htm
https://xingmy.1688.com/page/contactinfo.htm
https://shop1411058732611.1688.com/page/contactinfo.htm
https://yimeilida.1688.com/page/contactinfo.htm
https://shop1439830178914.1688.com/page/contactinfo.htm
https://shop1418280681251.1688.com/page/contactinfo.htm
https://shop1389804812948.1688.com/page/contactinfo.htm
https://0757baolifactory.1688.com/page/contactinfo.htm
https://shop1445014654439.1688.com/page/contactinfo.htm
https://yushuangmiao.1688.com/page/contactinfo.htm
https://shop1466010510506.1688.com/page/contactinfo.htm
https://shop1435682996106.1688.com/page/contactinfo.htm
https://gzhf520.1688.com/page/contactinfo.htm
https://shop1427364158207.1688.com/page/contactinfo.htm
https://gzbtfs.1688.com/page/contactinfo.htm
https://baixinfs.1688.com/page/contactinfo.htm
https://shop1460393816167.1688.com/page/contactinfo.htm
https://shop1442249317651.1688.com/page/contactinfo.htm
https://lostangles.1688.com/page/contactinfo.htm
https://shop1436806615558.1688.com/page/contactinfo.htm
https://158105957.1688.com/page/contactinfo.htm
https://ai1688vip.1688.com/page/contactinfo.htm
https://shop1395162008250.1688.com/page/contactinfo.htm
https://shop1434545582555.1688.com/page/contactinfo.htm
https://szsrsfz.1688.com/page/contactinfo.htm
https://szhkfz.1688.com/page/contactinfo.htm
https://shop1422335449813.1688.com/page/contactinfo.htm'''

links = links_list.split()
#print links

for link in links :
    #可能会爬取到无效网址或者个别网址select的位置不对，我们设置一个异常让程序继续进行
    try:
        get_items(link)
    except IndexError as e:
            print 'wo need keep going'
            continue
