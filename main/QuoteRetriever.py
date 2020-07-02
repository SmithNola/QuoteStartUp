from bs4 import BeautifulSoup
import requests

def retrieve_from_internet():
    res = requests.get("https://www.brainyquote.com/quote_of_the_day")
    html = BeautifulSoup(res.text, 'html.parser')
    aTag = html.select('.oncl_q')
    imgTag = BeautifulSoup(str(aTag), 'html.parser')
    quoteWithAuthor = imgTag.select("img")
    return quoteWithAuthor[0]['alt']


def retrieve_quote_and_author():
    list = retrieve_from_internet().split("-")
    quote = list[0]
    author = list[1]
    return quote, author