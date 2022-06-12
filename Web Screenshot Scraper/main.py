from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


DRIVER = 'chromedriver'
driver = webdriver.Chrome(DRIVER)
actions = ActionChains(driver)
driver.set_window_size(1900, 1080)
driver.get('https://earth.google.com/web/search/701+ellicotts+street/@42.89777795,-78.8675311,194.02888237a,122.5392609d,35y,0h,0t,0r/data=Cn8aVRJPCiUweDg5ZDMxMjU5NDk1M2ZjNjc6MHhlMzgxNWI1NWY3MjI2ZTJjGfGjda_uckVAIdCg_Dh1t1PAKhQ3MDEgZWxsaWNvdHRzIHN0cmVldBgCIAEiJgokCUFuplNGc0VAEY0GMwiXckVAGX2j6_oKt1PAISOeDXfft1PA')
time.sleep(8)
"""
element = driver.find_element(By.CSS_SELECTOR, 'icon-icon')

element.click()
"""

driver.execute_script("document.body.style.zoom='85%'")
time.sleep(1)

screenshot = driver.save_screenshot('my_screenshot.png')
driver.quit()