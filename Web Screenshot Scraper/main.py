from selenium import webdriver
import time

DRIVER = 'chromedriver'
driver = webdriver.Chrome(DRIVER)
driver.get('https://earth.google.com/web/search/701+ellicotts+street/@42.89777795,-78.8675311,194.02888237a,122.5392609d,35y,0h,0t,0r/data=Cn8aVRJPCiUweDg5ZDMxMjU5NDk1M2ZjNjc6MHhlMzgxNWI1NWY3MjI2ZTJjGfGjda_uckVAIdCg_Dh1t1PAKhQ3MDEgZWxsaWNvdHRzIHN0cmVldBgCIAEiJgokCUFuplNGc0VAEY0GMwiXckVAGX2j6_oKt1PAISOeDXfft1PA')
time.sleep(10)

element = driver.find_element('zoom-in')

element.click()

screenshot = driver.save_screenshot('my_screenshot.png')
driver.quit()