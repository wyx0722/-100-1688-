# -100-1688-
练手项目    {cookie的保质期是会变的，你需要经常使用浏览器获取最新的cookie；当然代理ip的寿命也有限，你也需要更换它。白天干测试，晚上学爬虫！}
change_ip.py：用来获取代理ip，针对爬取的ip限制问题
ture.py:用来验证获取的代理ip是否可用
channel_extract.py:获取所有需要具体分析的链接，并执行爬虫任务
get_item.py:用来解析最终链接上的内容，爬取联系方式
test.text:存放get_item.py所需的cookie
