from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from datetime import date
import time
import re
from bs4 import BeautifulSoup
# open chrome browser
driver = webdriver.Chrome(r'C:\Users\samuelmao\Desktop\DataScience\chromedriver.exe')
# go to the brands list page (A-Z)
#driver.get("https://www.sephora.com/brands-list")
driver.get('https://www.glassdoor.com/partner/jobListing.htm?pos=101&ao=420095&s=58&guid=1234567890abcdef1234567890abcdef&src=GD_JOB_AD&t=SR&extid=1&exst=OL&ist=&ast=OL&vt=w&slr=true&rtp=0&cs=1_daeb2d93&cb=1539316866516&jobListingId=2926478457')
# when login form pops up click cancel button
# driver.find_element_by_class_name('css-1n39fc0 ').click()
# # get a list of webelement that contains all the brands pages' webdrivers
# brand_pages = driver.find_elements_by_xpath("//a[@class='css-ezuahi ']")
# # create an empty list to find brands' URLs. brands has all brands URLs. ex: https://www.sephora.com/brand/acqua-di-parma
# brands = []
# for each in brand_pages:
#   each_page = each.get_attribute('href')
#   brands.append(each_page)
# # go to each brands URL
# for brand in brands[:3]:
#   driver.get(brand)
#   # go to each brand's all product page. ex: https://www.sephora.com/brand/acqua-di-parma/all
#   a=driver.find_element_by_partial_link_text('See All').get_attribute('href')
#   driver.get(a)
#   # create a list that contains all the products' urls
#   products=driver.find_elements_by_xpath("//div[@class='css-12egk0t']/a[@class='css-ix8km1']")
#   products=[x.get_attribute('href') for x in products]
#   print("---"*30)
#   # go to each product page
#   for p in products[:1]:
#     #Initialize an empty dictionary for each product
#     #product= {}
#     driver.get(p)
#     brand_name = driver.find_element_by_xpath("//h1/a/span[@class='css-15zphjk ']").text
#     print("got brand_name:", brand_name)
#     product_name = driver.find_element_by_xpath("//h1/span[@class='css-r4ddnb ']").text
#     print("got product name:", product_name)
#     num_reviews = driver.find_element_by_xpath("//button/span[@class='css-rok4hb ']").text
#     price = driver.find_element_by_xpath("//div/div[@data-comp='Price Box']").text
#     print("price is:",price)
#     details_info =driver.find_element_by_xpath("//div[@class='css-1pbcsc']/div").text
#     print("got details:", details_info)
#     #rating= driver.find_element_by_xpath("//div[@id='ratings-reviews']/div[@class='div.css-z1ro2e ']/div[@class='css-q074fe ']/div[@class='css-18r7c2g ']/div[@class='css-1cf1s0d ']/div[@class='css-14yihrc ']/div[@class='css-ffj77u ']").text
#     #rating= driver.find_element_by_xpath("//div[@data-comp='Grid Flex Box']/div[@data-comp='Box']").text
#     #rating=driver.find_element_by_xpath("//div[@class='css-14yihrc ']/div[@data-comp='Box']").text
#     #rating=driver.find_element_by_xpath("//div[@data-comp='LazyLoad RatingsAndReviews RatingsAndReviews RatingsAndReviews']/div[@data-comp='Box']").text
#     #this gives number of reviews and loves:
# 	#rating= driver.find_element_by_xpath("//div[@data-comp='GridCell Box']/div[@data-comp='Box']").text
#     #rating= driver.find_element_by_xpath("//div[@data-comp='GridCell Box']/div[@class='css-ffj77u ']").text
#     rating= driver.find_element_by_xpath("//div[@id='ratings-reviews']/div").text
#     print(rating)
#     #rating= int(driver.find_element_by_xpath("//div[@class='css-14yihrc ']/div[@class='css-ffj77u ']").text[1])
#     #scrapyshellcheck_response.xpath("//div[@data-comp='GridCell Box']/div[@class='css-ffj77u ']").extract_first
# #     try:
# #       driver.find_element_by_partial_link_text('About the Brand').click()
# #       brand_info = driver.find_element_by_xpath("//div[@id='tabpanel3']/p[@class='css-1loxqbt ']").text
# #     except NoSuchElementException:
# #       brand_info=""
# # ​
# #     try:
# #       rating= int(driver.find_element_by_xpath("//div[@class='css-14yihrc ']/div[@class='css-ffj77u ']").text[1])
# #     except NoSuchElementException:
# #       rating=""
