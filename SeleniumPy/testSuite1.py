__author__ = 'Donald'
import unittest
from buildFormsTestCase import BuildFormsTestCase
from popupWindows import PopupWindows

tests1 = unittest.TestLoader().loadTestsFromTestCase(BuildFormsTestCase)
tests2 = unittest.TestLoader().loadTestsFromTestCase(PopupWindows)

all_tests = unittest.TestSuite([tests1,tests2])

unittest.TextTestRunner(verbosity=2).run(all_tests)