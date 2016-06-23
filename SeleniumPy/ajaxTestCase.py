__author__ = 'Donald'

from selenium import webdriver # The driver for the Browser such as Firefox, etc.
from selenium.webdriver.common.by import By # Specifies the method of finding an element - by id, by name, etc.
from selenium.webdriver.support.ui import WebDriverWait # The function that implements the wait concept for a driver
from selenium.webdriver.support import expected_conditions as EC # specifies the type of wait condition

driver = webdriver.Firefox()
driver.get("http://perfdash-4602.phx01.dev.ebayc3.com:8080/Web_Project_1/ajaxTest.jsp")

driver.find_element_by_id("div1").click()

element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@id='div1']/div")))

ajaxDivText = driver.find_element_by_xpath("//div[@id='div1']/div").text
print("ajaxDivText is " + ajaxDivText)

driver.quit()
