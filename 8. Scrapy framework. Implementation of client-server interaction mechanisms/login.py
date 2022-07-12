import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Логин
service = Service('D:\Geek\Parser\HW_8\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://quotes.toscrape.com/login')
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'username')))

username = driver.find_element(by=By.ID, value='username')
password = driver.find_element(by=By.XPATH, value='//input[@name="password"]')

username.send_keys('admin')
password.send_keys('admin')

button = driver.find_element(by=By.XPATH, value='//input[@value="Login"]')
button.click()

# Скроллинг
driver.get('https://quotes.toscrape.com/scroll')
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'quote')))

pause_time = 0.5
start_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(pause_time)

    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == start_height:
        break
    start_height = new_height

# Парсинг
quotes = driver.find_elements(by=By.CLASS_NAME, value='quote')
for quote in quotes:
    all_tags = quote.find_elements(by=By.XPATH, value="//a[@class='tag']")
    quote_dict = {
        'text': quote.find_element(by=By.CLASS_NAME, value='text').text,
        'author': quote.find_element(by=By.CLASS_NAME, value='author').text,
        'tags': [tag.text for tag in all_tags]
    }

    with open('data.json', 'a', encoding='utf-8') as f:
        json.dump(quote_dict, f, ensure_ascii=False)

time.sleep(2)

driver.quit()
