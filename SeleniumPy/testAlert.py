from selenium import webdriver
from selenium.webdriver.common.alert import Alert

driver = webdriver.Firefox()
driver.implicitly_wait(30)

driver.get("http://localhost:8080/Web_Project_1/seleniumTest.jsp")
driver.find_element_by_link_text("Popup Window Demos").click()
driver.find_element_by_css_selector("button").click()


alert = driver.switch_to.alert
alert.accept()
#alert.dismiss()

