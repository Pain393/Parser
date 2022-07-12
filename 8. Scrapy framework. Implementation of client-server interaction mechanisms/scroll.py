import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service('D:\Geek\Parser\HW_8\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://quotes.toscrape.com/scroll')
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'quote')))

pause_time = 1
start_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(pause_time)
    
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == start_height:
        break
    start_height = new_height
    
quotes = driver.find_elements(by=By.CLASS_NAME, value='quote')
print(f'{len(quotes)} quotes')
time.sleep(3)

driver.quit()
