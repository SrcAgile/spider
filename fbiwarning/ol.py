# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import os
import urllib
url = 'http://ffff75.com/p02/index.html'
baseurl = 'http://ffff75.com'
headers = {
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.167 Chrome/64.0.3282.167 Safari/537.36'
}

response = requests.get(url=url,headers=headers)
content = response.content.decode()

soup = BeautifulSoup(content,'html.parser')

def resolve(combineurl):
	response = requests.get(url=combineurl,headers=headers)
	content = response.content.decode()
	soup = BeautifulSoup(content,'html.parser')
	titlelist = soup.select('font')
	title=0
	for t in titlelist:
		title=str(t.get_text())
	wrapimg = soup.select('.wrap  img')
	floder = 'img/'+title
	if not os.path.isdir(floder):
		os.makedirs(floder)
	for img in wrapimg:
		imgurl = img.attrs['src']
		#imgurl = urllib.parse.quote(imgurl,safe='/:?=')
		print ('[reqs] %s' %imgurl[-6:])
		if(imgurl[-3:]=='gif'):
			continue
		try:
			response = requests.get(url=imgurl,headers=headers)
			content = response.content
			jpg = floder+'/%sjpg'
			try:
				with open(jpg  %imgurl[-6:-3],'wb') as f:
					f.write(content)
			except Exception as e:
				print (e)
		except :
			print ('may be url err')
	print ('[save] %s file' %title)

img_list = soup.select('.typelist a')
print (len(img_list))
for i in img_list:
	curl = baseurl + str(i.attrs['href'])
	resolve(curl)
