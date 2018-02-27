from selenium import webdriver as wb
import json
import time
import _thread
driver = wb.Chrome()
url = 'https://www.zhihu.com/topic/19607535/top-answers'

def jsfresh(threadname,delay):
	count = 0
	flag=1	
	while flag:
		count = count+1
		js="var q=document.documentElement.scrollTop=100000"  
		driver.execute_script(js)
		time.sleep(1)
		print ('QAQ页面君努力加载 %d 页' %count)
		if(count==30):
			break 


driver.maximize_window()
driver.get(url)

#_thread.start_new_thread(jsfresh,("fresh",5))
jsfresh("fresh",5)
asr_list = driver.find_elements_by_css_selector("[class='ContentItem AnswerItem']")


for asr in asr_list:
	uname = asr.find_element_by_css_selector("[class='UserLink AuthorInfo-name']").text
	title = asr.find_element_by_css_selector("[data-za-detail-view-element_name='Title']").text
	upvote = asr.find_element_by_css_selector("[class='Button VoteButton VoteButton--up']").text
	art = asr.find_element_by_css_selector("span.RichText.CopyrightRichText-richText").text
	print ("---------------------------------------------->\n")
	print ("uname: %s" %uname)
	print ("title: %s" %title)
	print ("upvote: %s" %upvote)
	print ("article: %s" %art)
	print ("<-----------------------------------------------\n")
driver.close()

