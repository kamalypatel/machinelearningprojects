from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv

DRIVER = 'chromedriver'
driver = webdriver.Chrome(DRIVER)
actions = ActionChains(driver)
driver.set_window_size(1900, 1080)
url = "https://www.ahridirectory.org/NewSearch?programId=5&searchTypeId=1&productTypeId=1732"
driver.get(url)

element = driver.find_element(By.XPATH, '//*[@id="btnSearch"]')

element.click()
time.sleep(10)

element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div[3]/div[4]/span/a[2]')

element.click()
time.sleep(10)

element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div[3]/div[4]/span/a[3]')

element.click()
time.sleep(10)

element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div[3]/div[4]/span/a[4]')

element.click()
time.sleep(10)
