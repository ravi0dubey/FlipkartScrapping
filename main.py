from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as urReq
import requests



flipkart_url= "https://www.flipkart.com/search?q="+"iphone11"
print(flipkart_url)
response_website=urReq(flipkart_url)
print(response_website)
flipkart_response=response_website.read()
beautifyed_html= bs(flipkart_response,"html.parser")
bigbox= beautifyed_html.find_all("div",{"class":"_1AtVbE col-12-12"})
product6="https://www.flipkart.com"+ bigbox[8].div.div.div.a['href']
product66 = requests.get(product6)
product66.encoding= 'utf-8'
product6_page = bs(product66.text,"html.parser")



price = product6_page.find_all('div',{'class' :"_30jeq3 _16Jk6d"})[0].text
product_name = product6_page.find_all('div',{'class' :"aMaAEs"})[0].h1.text
overall_product_rating = product6_page.find_all('div',{'class' :"_3LWZlK"})[0].text
total_rating = product6_page.find_all('span',{'class' :"_2_R_DZ"})[0].text.split('\xa0')[0]
total_reviews = product6_page.find_all('span',{'class' :"_2_R_DZ"})[0].text.split('\xa0')[2]


short_reviews = []
count_short_reviews = len(product6_page.find_all('div',{'class' :"_16PBlm"}))
for i in range(0,count_short_reviews-1):
    short_reviews.append(product6_page.find_all('div',{'class' :"_16PBlm"})[i].p.text)



long_reviews= []
count_long_reviews = len(product6_page.find_all('div',{'class' :"t-ZTKy"}))
for i in range(0,count_long_reviews-1):
    long_reviews.append(product6_page.find_all('div',{'class' :"t-ZTKy"})[i].text)


individual_ratings= []
count_individual_ratings = len(product6_page.find_all('div',{'class' :"_3LWZlK _1BLPMq"}))
for i in range(0,count_individual_ratings-1):
    individual_ratings.append(product6_page.find_all('div',{'class' :"_3LWZlK _1BLPMq"})[i].text)


users_list= []
count_users = len(product6_page.div.div.find_all('p',{'class' :"_2sc7ZR _2V5EHH"}))
count_users
for i in range(0,count_users-1):
    users_list.append(product6_page.div.div.find_all('p',{'class' :"_2sc7ZR _2V5EHH"})[i].text)


feedback_date_list= []
count_date_user_given = len(product6_page.div.div.find_all('p',{'class' :"_2sc7ZR"}))
count_date_user_given
for i in range(1,count_date_user_given-1,2):
    feedback_date_list.append(product6_page.div.div.find_all('p',{'class' :"_2sc7ZR"})[i].text)