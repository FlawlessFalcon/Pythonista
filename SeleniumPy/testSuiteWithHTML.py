__author__ = 'Donald'
import unittest
import HTMLTestRunner
import os
from buildFormsTestCase import BuildFormsTestCase
from popupWindows import PopupWindows

dir = os.getcwd()
tests1 = unittest.TestLoader().loadTestsFromTestCase(BuildFormsTestCase)
tests2 = unittest.TestLoader().loadTestsFromTestCase(PopupWindows)

all_tests = unittest.TestSuite([tests1,tests2])

outfile = open(dir+"\TestReport.html", "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,
                                       verbosity=1,
                                       title="Selenium Test Report",
                                       description="Testing Tomcat Web Project 1")
runner.run(all_tests)
#unittest.TextTestRunner(verbosity=2).run(all_tests)