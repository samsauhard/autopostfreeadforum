from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.keys import Keys 
from xlrd import open_workbook
from xlutils.copy import copy
import xlwt
import xlsxwriter
import re
from selenium.webdriver.support.ui import Select
option1 = 1
region = 782042
link = "http://www.thefreeadforum.com/postclassifieds/"
counter =1
driver = webdriver.Chrome('C:\chromedriver.exe')

driver.get(link)

driver.find_element_by_xpath('//*[@id="login_open"]').click()
driver.switch_to.window(driver.window_handles[-1])
el = driver.find_element_by_name('email')
el.send_keys("sauhard121@gmail.com")
driver.find_element_by_id('password').send_keys("Smart.sam1")
driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/form/div[3]/div[2]/button').click()
driver.find_element_by_xpath('//*[@id="header"]/div[3]/ul/li[2]/a').click()
driver.switch_to.window(driver.window_handles[-1])
ooption=[]
ooption1=[]
ooption2=[]
ww = driver.find_element_by_xpath('//*[@id="catId"]')
for options in ww.find_elements_by_tag_name('option')[2:]:
	ooption.append(options.get_attribute('value'))
	print(options.get_attribute('value'))
ww1 = driver.find_element_by_xpath('//*[@id="regionId"]')
try:	
	for options in ww1.find_elements_by_tag_name('option')[2:]:
		ooption1.append(options.get_attribute('value'))

		select112 = Select(driver.find_element_by_xpath('//*[@id="regionId"]'))
		select112.select_by_value(options.get_attribute('value'))
		#time.sleep(2)
		print(options.get_attribute('value'))
		
		ww2 = driver.find_element_by_xpath('//*[@id="cityId"]')
		try:
			for options2 in ww2.find_elements_by_tag_name('option')[1:]:
				ooption2.append(options2.get_attribute('value'))
				print(options2.get_attribute('value'))
		except:
			print('err')
except:
	print('err')

for option in ooption:
	for option1 in ooption1:
		for option2 in ooption2:	
			try:
				select = Select(driver.find_element_by_xpath('//*[@id="catId"]'))
				select.select_by_value(option)
				driver.find_element_by_xpath('//*[@id="titleen_US"]').send_keys("How to Earn a 6-Figure Side-Income Online")
				l = driver.find_element_by_xpath('//*[@id="descriptionen_US_ifr"]')
				l.click()
				time.sleep(1)
				select1 = Select(driver.find_element_by_xpath('//*[@id="regionId"]'))
				select1.select_by_value(option1)
				print("2")
				time.sleep(1)
				select2 = Select(driver.find_element_by_xpath('//*[@id="cityId"]'))
				select2.select_by_value(option2)
				print("3")
				driver.find_element_by_id('meta_website-link').send_keys("https://shopebuzz.com")
				time.sleep(2)
				
				iframe = driver.find_elements_by_tag_name('iframe')[0]
				driver.switch_to.frame(iframe)
				m = driver.find_element_by_xpath('//*[@id="tinymce"]')
				m.send_keys("Generate $1000's Per Day In 2020! In today's Free training I'm going to show you what is by far the BEST & EASIEST way to make money online in the comfort of your own home....and how you can tap into this proven system right now and start generating $1,000/Day (or more) and be on track for 6 figures in the next 30 days.And How It Can Change Your Life Forever! In fact, this training has helped over 2000+ people /from around the world in the last year make $1k/day and more!The best part is you don't need to have any experience to do this.Plus you don't need a lot of time as this only requires less than 1-2 hours a day to generate thousands.I'm going to show you exactly how to use Facebook to generate thousands of dollars per day without a product, email list or even a website.Don't worry about results...I'll show you how you can virtually GUARANTEE results for yourself on today's training.")
				print("1")
				driver.switch_to.default_content()

				time.sleep(3)
				driver.find_element_by_xpath('//*[@id="item-post"]/fieldset/div[10]/div/button').click()
				time.sleep(3)
				
				driver.get('http://www.thefreeadforum.com/postclassifieds/item/new')

			except Exception as e:
				print(e)
				
