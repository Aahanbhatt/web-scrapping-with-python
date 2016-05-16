import re
import urllib.request
import urllib.parse
import webbrowser

url="http://117.239.83.200:8102/it/index.php"
value={'view':'attendance4'}
data=urllib.parse.urlencode(value)
data=data.encode('utf-8')
req=urllib.request.Request(url,data)
resp=urllib.request.urlopen(req)

f=open("D:/AAHAN/aahan/py/crawler/attendance4.html",'w')
parsing=re.findall(r'<h4>(.*)</table>',str(resp.read()))
for p in parsing:
	f.write(p+"\n")
f.close()

fileurl="file://D:/AAHAN/aahan/py/crawler/attendance4.html"
webbrowser.open(fileurl)
