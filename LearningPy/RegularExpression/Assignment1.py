'''
Created on Mar 15, 2016

@author: gaiyamperumal
regex_sum_42.txt
regex_sum_217341.txt

'''
import re 

hand = open('regex_sum_217341.txt')
data = list()
sum = 0
for line in hand:
    line = line.strip()
    datas = re.findall('[0-9]+', line)
    inp = list(datas)
    if datas == [] : continue
    for data in datas:
        sum = sum + int(data)
print sum