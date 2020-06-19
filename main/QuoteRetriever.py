from bs4 import BeautifulSoup
import requests
res = requests.get("https://www.brainyquote.com/quote_of_the_day")
html = BeautifulSoup(res.text, 'html.parser')
aTag = html.select('.oncl_q')
imgTag = BeautifulSoup(str(aTag), 'html.parser')
quoteWithAuthor = imgTag.select("img")
print(quoteWithAuthor[0]['alt'])

