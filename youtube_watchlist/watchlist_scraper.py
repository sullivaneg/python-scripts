import csv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from secret.key import cipher
from bs4 import BeautifulSoup
import datetime
import pickle

cookie_file = 'secret/cookie.enc'

def encrypt_cookies(cookies, filename=cookie_file):
    serialized = pickle.dumps(cookies)
    encrypted = cipher.encrypt(serialized)
    with open(filename, 'wb') as f:
        f.write(encrypted)

def decrypt_cookies(cookies, filename=cookie_file):
    with open(filename, 'rb') as f:
        encrypted = f.read()
    decrypted = cipher.decrypt(encrypted)
    return pickle.loads(decrypted)

def save_cookies(driver, filename=cookie_file):
    cookies = driver.get_cookies()
    encrypt_cookies(cookies, filename)

def load_cookies(driver, filename=cookie_file):
    cookies = decrypt_cookies(filename)
    for cookie in cookies:
        cookie.pop('sameSite', None)
        driver.add_cookie(cookie)

def manual_login_and_save():
    options = Options()
    options.headless = False
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.youtube.com/')

    print('Logging in...')
    input()

    save_cookies(driver)
    driver.quit

def scrape_watchlist():
    # Create a headless Chrome browser
    # Learning point: Headless Chrome browsers are GUI-less browsers
    # often used for web scraping or development testing
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    try:
        # Open Youtube Watchlist URL
        driver.get('https://www.youtube.com/playlist?list=WL')

        # Wait for page to load content (WATCH TO SEE IF VPN SLOWS THIS)
        # Can adjust sleep time or firewall rules as needed
        # Wait until my span loads
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'style-scope'))
        )

        # Automate login -> Cookie Injection
        # Learning Point: Login manually -> Extract and save session cookies to file
        # Load and inject those cookies
        load_cookies(driver)
        driver.refresh()

        #Scraping Logic
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        span_tag = soup.find('span', class_='style-scope yt-formatted-string')

        if span_tag:
            count_text = span_tag.text.strip().replace(',', '')
            count_num = int(count_text)
        else:
            count_num = None

        # Store the number with a timestamp
        now = datetime.datetime.now().isoformat()
        print(f"{now} - Watchlist Count: {count_num}")

        with open('watchlist_log.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([now, count_num])

    finally:
        driver.quit()






