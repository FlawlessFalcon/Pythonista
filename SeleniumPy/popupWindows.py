# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class PopupWindows(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://perfdash-4602.phx01.dev.ebayc3.com:8080/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_popup_windows(self):
        driver = self.driver
        driver.get("http://perfdash-4602.phx01.dev.ebayc3.com:8080/Web_Project_1/seleniumTest.jsp")
        driver.find_element_by_link_text("Popup Window Demos").click()
        driver.find_element_by_css_selector("button").click()
        self.assertEqual("I am an alert box!", self.close_alert_and_get_its_text())
        driver.find_element_by_xpath("//button[@onclick='myFunction1()']").click()
        self.assertEqual("Press a button!", self.close_alert_and_get_its_text())
        driver.find_element_by_xpath("//button[@onclick='myFunction2()']").click()
        alert = driver.switch_to.alert
        alert.send_keys("Mickey")
        self.assertEqual("Please enter your name", self.close_alert_and_get_its_text())
        pageSource = self.driver.page_source
        self.assertTrue("Mickey" in pageSource)
        driver.find_element_by_xpath("//a[contains(@href, 'smallPopup.html')]").click()
        driver.switch_to.window("notes")
        driver.find_element_by_name("FirstName").clear()
        element = driver.find_element_by_name("FirstName")
        element.send_keys("Hermione")
        self.assertTrue("Hermione", element.text)

    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to.alert
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
