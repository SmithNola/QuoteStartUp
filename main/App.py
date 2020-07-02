from main.GUIscreen import GUI
from main.QuoteRetriever import *

def main():
    quote, author = retrieve_quote_and_author()
    gi = GUI(quote, author)
    gi.create_screen(quote, author)


main()
