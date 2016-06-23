'''
Created on Mar 15, 2016

@author: gaiyamperumal
'''
import re

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print y