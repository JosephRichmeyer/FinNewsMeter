import urllib
import re
import requests
from bs4 import BeautifulSoup
import string
import scrapy
import datetime


#Declaring Variables
goodWord = ["rise","up","climb","boost","tax cut" "tax cuts"]
badWord = ["tax increase"]
goodCount = 0
badCount = 0
article = "The3333 White House has started work on a second round of tax cuts even as the budget deficit continues to grow, Treasury Secretary Steven Mnuchin said Thursday."
puncNum = '''!()-[]{};:'"\,<>./?@#$%^&*_~1234567890'''
d = datetime.datetime.today()

for x in article.lower():
    if x in puncNum:
        article = article.replace(x, "")
        
print(article)
def CNBC():
    cnbcDate = str(d.year) + "/" + str(d.strftime('%m')) + "/" + str(d.strftime('%d'))
    cnbcURLList = []
    cnbcFilter = []
    cnbcLink = []
    articleText = ""
    url = "https://www.cnbc.com/"
    page = requests.get(url)    
    data = page.text
    soup = BeautifulSoup(data,features="lxml")
    for link in soup.find_all('a'): 
        #print(link.get('href'))
        if link is not None:
            cnbcURLList.append(link.get('href'))
    cnbcFilter = list(filter(None, cnbcURLList))

    #checks to see if the article is from today and adds these to cnbcLink
    for link in cnbcFilter:
        if cnbcDate in link:
            cnbcLink.append(link)
            print (link)

    #extracts text from cnbcLink
    for link in cnbcLink:
        #articleText = articleText + str(soup.find_all(text=True))
        #scrapy code here
        
        res = requests.get(link)
        html_page = res.content
        soup = BeautifulSoup(html_page, 'html.parser')
        text = soup.find_all(text=True)
        print (text)
    #print (articleText)
    #TOMORROW, get article "content and headlines"


def BLOOMBERG():
    bloombergDate = str(d.year) + "-" + str(d.strftime('%m')) + "-" + str(d.strftime('%d'))
#def MARKETWATCH():


CNBC()
class cnbcSpider (scrapy.Spider):
    name = 'cnbc'
    cnbcURL = [ 'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',]

 #   def cnbc_request(self, response):
      #  for quote in response.css('div.quote') 