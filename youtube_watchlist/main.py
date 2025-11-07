from os import WCONTINUED

from watchlist_scraper import *
import os

def main():
    file = "secret/cookie.enc"
    if not os.path.exists(file):
        manual_login_and_save()
    else:
        scrape_watchlist()

while True:
    main()