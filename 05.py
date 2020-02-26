#!/usr/bin/python
# -*- coding: utf-8 -*-

f = open("write.txt","r")
words = []
for line in f:
        line = line.strip()
        words += line.split() 
print words
l = len(words)
i = 0

while i < l:
    if len(words[i]) > 3:
        wrd = words[i]
        pig = wrd[1:] + wrd[0] + "ay"
        print (pig)
        i = i + 1
    else:
        print (words[i])
        i = i + 1

    




