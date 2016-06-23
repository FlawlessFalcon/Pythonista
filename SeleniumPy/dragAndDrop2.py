__author__ = 'Donald'

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

firefox = webdriver.Firefox()

firefox.get('http://localhost:8080/Web_Project_1/testDragAndDrop2.jsp')
#draggable = firefox.find_element_by_class_name("draggable")
draggable = firefox.find_element_by_xpath("//div[@id='boxA']")
droppable = firefox.find_element_by_xpath("//div[@id='boxB']")
dragdrop = ActionChains(firefox).drag_and_drop(draggable, droppable)

dragdrop.perform()
firefox.quit()