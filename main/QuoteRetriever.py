from bs4 import BeautifulSoup
import requests

def retrieve_quote():
    res = requests.get("https://www.brainyquote.com/quote_of_the_day")
    html = BeautifulSoup(res.text, 'html.parser')
    aTag = html.select('.oncl_q')
    imgTag = BeautifulSoup(str(aTag), 'html.parser')
    quoteWithAuthor = imgTag.select("img")
    return quoteWithAuthor[0]['alt']

def seperate_quote(quoteWithAuthor):
    list = quoteWithAuthor.split("-")
    quote = list[0]
    author = list[1]
    print(quote + author)
    return quote, author

seperate_quote(retrieve_quote())

