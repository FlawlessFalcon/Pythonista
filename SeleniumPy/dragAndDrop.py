__author__ = 'Donald'

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get("http://www.w3schools.com/html/html5_draganddrop.asp")


element = driver.find_element_by_id("drag1")
target = driver.find_element_by_id("div2")

action_chains = ActionChains(driver)
time.sleep(15)
action_chains.drag_and_drop(element, target).perform()
time.sleep(15)
driver.close()
