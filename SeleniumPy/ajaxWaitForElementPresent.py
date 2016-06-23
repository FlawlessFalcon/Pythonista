# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait # The function that implements the wait concept for a driver
from selenium.webdriver.support import expected_conditions as EC # specifies the type of wait condition

import unittest, time, re

class AjaxWaitForElementPresent(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8080/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ajax_wait_for_element_present(self):
        print("In test 1")
        driver = self.driver
        driver.get("http://localhost:8080/Web_Project_1/ajaxTest.jsp")
        driver.find_element_by_id("div1").click()
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "//div[@id='div1']/div"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        # ERROR: Caught exception [ERROR: Unsupported command [waitForCondition | var value = selenium.getText("//div[@id='div1']"); value != "Click Here for AJAX response"  | 30000]]
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*response from Servlet[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))

    def test_ajax_wait_for_element_present_1(self):
        print("In test 2")
        driver = self.driver
        driver.get("http://localhost:8080/Web_Project_1/ajaxTest.jsp")
        driver.find_element_by_id("div1").click()
        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@id='div1']/div")))
        # ERROR: Caught exception [ERROR: Unsupported command [waitForCondition | var value = selenium.getText("//div[@id='div1']"); value != "Click Here for AJAX response"  | 30000]]
        # Warning: verifyTextPresent may require manual changes
        try:
            self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*response from Servlet[\s\S]*$")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
    
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
