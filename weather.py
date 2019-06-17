#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
driver = webdriver.Firefox(firefox_options=options)

user_input = raw_input("Where are you trying to find the weather in: ")
url = ("https://www.google.com/search?client=ubuntu&hs=epV&channel=fs&ei=fnsCXeO-Kc6t5wL5gYGYCw&q=tempature+" + user_input +"&oq=tempature+" + user_input +"&gs_l=psy-ab.3..0i22i30.1753.2426..2514...0.0..1.222.1395.5j4j2......0....1..gws-wiz.......0i71j0i10j0i13j0i8i13i30.V0uQp7ARvs0")

driver.get(url)

spans =[]	
count = 0
document = driver.find_elements_by_tag_name('span')
for i in document :
    if (i.get_attribute("innerHTML") != None) :
    	spans.append(i.get_attribute("innerHTML"))

for i in spans:
	print(str(count) + ". " + i)
	count += 1
	
ftemp = spans[12]
ctemp = ((int(ftemp) - 32) * 5/9)
Precip = spans[18]
Humid = spans[19]
wind = spans[21]
print(ftemp + "F / " + str(ctemp) + "C")
print("Precipitation: " + Precip )
print("Humidity: " + Humid)
print("Wind: " + wind)
