__author__ = 'Donald'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("http://www.google.com")


try:
    done = False
    inputTagList = []
    endIndex = 0
    count = 0
    while (not done):
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tsf")))
        pageSource = driver.page_source
        print("The type is " + type(pageSource).__name__)
        # print(pageSource)
        stringLength = len(pageSource)
        print("stringLength = " + str(stringLength))
        startIndex = pageSource.find("<input", endIndex, stringLength)
        endOfString = stringLength - startIndex - 1
        print("endOfString is " + str(endOfString))
        #print(pageSource[startIndex:stringLength - 1])
        endIndex = pageSource.find(">",startIndex, stringLength - 1)
        print("startIndex = " + str(startIndex))
        print("endIndex = " + str(endIndex))
        theInputTag = pageSource[startIndex:endIndex + 1]
        print(theInputTag)
        if (startIndex == -1):
            done = True
        else:
            print("count is " + str(count))
            inputTagList.append(theInputTag)
    for inputTag in inputTagList:
        print(inputTag)

finally:
    driver.quit()