from selenium import webdriver
from bs4 import BeautifulSoup

# bookName = 'react'
# 링크 받기
link = input('교보문고 링크 입력 : ')
driver = webdriver.Chrome('/Users/jack/Downloads/chromedriver')
driver.implicitly_wait(3)
driver.get(link)
# key = driver.find_element_by_id('searchKeyword').send_keys(bookName)
# driver.find_element_by_xpath("//input[@type='submit']").click()
# driver.find_element_by_css_selector('#container > div:nth-child(21) > form > table > tbody > tr:nth-child(2) > td.detail > div.title > a').click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
# 제목, 출판사, ISBN, 쪽수, 금액(판매가), 정가
title = soup.select("#container > div:nth-child(4) > form > div.box_detail_point > h1")
print('책제목',title[0].text.replace("\n", "").strip())
sellPrice = soup.select("#container > div:nth-child(4) > form > div.box_detail_order > div.box_detail_price > ul > li:nth-child(1) > span.sell_price")
print('판매가',sellPrice[0].text)
orgPrice = soup.select("#container > div:nth-child(4) > form > div.box_detail_order > div.box_detail_price > ul > li:nth-child(1) > span.org_price")
print('정가',orgPrice[0].text.replace("\n", "").strip())
seller = soup.select('#container > div:nth-child(4) > form > div.box_detail_point > div.author > span:nth-child(3) > a')
print('출판사',seller[0].text)
ISBN = soup.select("#container > div:nth-child(7) > div.content_left > div:nth-child(5) > table > tbody > tr:nth-child(1) > td")
print('ISBN',ISBN[0].text)
pageNum = soup.select("#container > div:nth-child(7) > div.content_left > div:nth-child(5) > table > tbody > tr:nth-child(2) > td")
print('쪽수',pageNum[0].text)
