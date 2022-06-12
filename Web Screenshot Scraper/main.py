from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv


with open('long_lats.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        DRIVER = 'chromedriver'
        driver = webdriver.Chrome(DRIVER)
        actions = ActionChains(driver)
        driver.set_window_size(1900, 1080)
        url = "https://earth.google.com/web/search/" + str(row[1]) + "%09" + str(row[2]) + "/@" + str(row[1]) + "," + str(row[2]) + ",300.68548482a,1250.12036026d,3y,0h,0t,0r"
        driver.get(url)
        time.sleep(12)
        driver.execute_script("document.body.style.zoom='85%'")
        time.sleep(1)

        screenshot = driver.save_screenshot(row[0] + ".png")
        driver.quit()

#left this commented part below because the format was hard to find online but this is the correct format
#element = driver.find_element(By.CSS_SELECTOR, 'icon-icon')
#element.click()
