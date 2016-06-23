'''
Created on Jan 11, 2016

@author: gaiyamperumal

Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper 
case. Use the file words.txt to produce the output below. You can download the sample data at http://www.pythonlearn.com/code/words.txt
'''
fName = raw_input('Enter the file name:')
fHand = open(fName)
for line in fHand:
    line = line.rstrip()
    print line.upper()