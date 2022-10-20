import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


os.environ['PATH'] += os.pathsep + r'C:\Soft\ForPython\chromedriver'

driver = webdriver.Chrome()

driver.get('http://www.google.com')

print(driver.title)

inputElement = driver.find_element(by=By.NAME, value='q')

inputElement.send_keys('cheese!')

inputElement.submit()

try:
    WebDriverWait(driver, 10).until(EC.title_contains('cheese!'))
    print(driver.title)
except TimeoutException:
    print('Timeout exception!')
finally:
    driver.quit()
