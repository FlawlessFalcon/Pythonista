'''
Created on May 27, 2016

@author: gaiyamperumal

Example script to run one test against the Chess Free app using Appium
The test will:
- launch the app
- click the 'PLAY!' button
- choose single player mode

'''
import unittest, time, os

from appium import webdriver

class ChessAndroidTests(unittest.TestCase):
    "Class to run tests against the chess free app "

    def setUp(self):
        "Setup for the test"
        # Using the apk link directly to launch the app
        #app = "http://file.appsapk.com/wp-content/uploads/apps-3/Chess%20Free.apk"
        app ="/Users/gaiyamperumal/Desktop/Terrific/MobileAutomation/apps/Chess Free.apk"
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4723/wd/hub',
            desired_capabilities={
                'platformName': 'Android',
                'deviceName': 'Android Emulator',
                'platformVersion': '6.0',
                'app': app,
                'name': 'Appium Python Android Test for Chess App',
                'appPackage': 'uk.co.aifactory.chessfree',
                'appActivity': '.ChessFreeActivity'
            })


    def tearDown(self):
        "Tear down the test"
        self.driver.quit()
        # uninstall app here

    def test_single_player_mode(self):
        "Test the Single Player mode launches correctly"
        element = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("uk.co.aifactory.chessfree:id/ButtonPlay").text("PLAY!")').click()
        time.sleep(5)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("uk.co.aifactory.chessfree:id/EasyButton").text("Single Player")').click()
        time.sleep(5)
        textfields = self.driver.find_elements_by_class_name("android.widget.TextView")
        print textfields
        self.assertEqual('MATCH SETTINGS', textfields[0].text)

    def test_two_player_mode(self):
        "Test the Two Player mode launches correctly"
        element = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("uk.co.aifactory.chessfree:id/ButtonPlay").text("PLAY!")').click()
        time.sleep(5)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("uk.co.aifactory.chessfree:id/MediumButton").text("Two Player")').click()
        time.sleep(5)
        textfields = self.driver.find_elements_by_class_name("android.widget.TextView")
        print textfields
        self.assertEqual('MATCH SETTINGS', textfields[0].text)

# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ChessAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)