#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
#Εβαλα 30 γιατι θεωρω οτι ειναι ενας φυσιολογικος αριθμος αυτοκινητων για αναμονη σε φαναρι! 
fan1 = random.randint(0, 30)
fan2 = random.randint(0, 30)
fan3 = random.randint(0, 30)
traf1 = ["the first traffic light turns green:" ,"the secondly traffic light turns green:" ]
traf2 = ["the first traffic light turns green:" , "the third traffic light turns green:"]
traf3 = ["the secondly traffic light turns green:" ,"the third traffic light turns green:" ]
print fan1,fan2,fan3
if (fan1>fan2 and fan1>fan3):
    print("the first traffic light turns green:")
    feug = random.randrange(5,10)
    print ("they came:" , feug)
    fan1 = fan1 - feug
    erx2 = random.randrange(0,5)
    print("they left from secondly traffic light:" , erx2)
    fan2 =fan2 + erx2
    erx3 = random.randrange(0,5)
    print("they left from third traffic light:" , erx3)
    fan3 =fan3 + erx3
    print ("the first traffic light has:" , fan1)
    print ("the secondly traffic light has:" , fan2)
    print ("the third traffic light has:" , fan3)
elif (fan2>fan1 and fan2>fan3):
    print("the secondly traffic light turns green:")
    feug = random.randrange(5,10)
    print ("they left:" , feug)
    fan2 = fan2 -feug
    erx1 = random.randrange(0,5)
    print("they came from first traffic light:" , erx1)
    fan1 =fan1 + erx1
    erx3 = random.randrange(0,5)
    print("they came from third traffic light:" , erx3)
    fan3 =fan3 + erx3
    print ("the first traffic light has:" , fan1)
    print ("the secondly traffic light has:" , fan2)
    print ("the third traffic light has:" , fan3)
elif (fan3>fan1 and fan3>fan2):
    print("the third traffic light turns green:")
    feug = random.randrange(5,10)
    print ("they left:" , feug)
    fan3 = fan3 -feug
    erx1 = random.randrange(0,5)
    print("they came from first traffic light:" , erx1)
    fan1 =fan1 + erx1
    erx2 = random.randrange(0,5)
    print("they came from secondly traffic light:" , erx2)
    fan2 =fan2 + erx2
    print ("the first traffic light has:" , fan1)
    print ("the secondly traffic light has:" , fan2)
    print ("the third traffic light has:" , fan3)
else:
    if (fan1==fan2):
        epil = random.choice(traf1)
        print epil
        if epil == traf1[1]:
            feug = random.randrange(5,10)
            print ("they came:" , feug)
            fan1 = fan1 - feug
            erx2 = random.randrange(0,5)
            print("they left from secondly traffic light:" , erx2)
            fan2 =fan2 + erx2
            erx3 = random.randrange(0,5)
            print("they left from third traffic light:" , erx3)
            fan3 =fan3 + erx3
            print ("the first traffic light has:" , fan1)
            print ("the secondly traffic light has:" , fan2)
            print ("the third traffic light has:" , fan3)
        else:
            feug = random.randrange(5,10)
            print ("they left:" , feug)
            fan2 = fan2 -feug
            erx1 = random.randrange(0,5)
            print("they came from first traffic light:" , erx1)
            fan1 =fan1 + erx1
            erx3 = random.randrange(0,5)
            print("they came from third traffic light:" , erx3)
            fan3 =fan3 + erx3
            print ("the first traffic light has:" , fan1)
            print ("the secondly traffic light has:" , fan2)
            print ("the third traffic light has:" , fan3) 
    if (fan1==fan3):
        epil = random.choice(traf2)
        print epil
        if (epil==traf2[1]):
            feug = random.randrange(5,10)
            print ("they came:" , feug)
            fan1 = fan1 - feug
            erx2 = random.randrange(0,5)
            print("they left from secondly traffic light:" , erx2)
            fan2 =fan2 + erx2
            erx3 = random.randrange(0,5)
            print("they left from third traffic light:" , erx3)
            fan3 =fan3 + erx3
            print ("the first traffic light has:" , fan1)
            print ("the secondly traffic light has:" , fan2)
            print ("the third traffic light has:" , fan3)
        else:
            feug = random.randrange(5,10)
            print ("they left:" , feug)
            fan3 = fan3 -feug
            erx1 = random.randrange(0,5)
            print("they came from first traffic light:" , erx1)
            fan1 =fan1 + erx1
            erx2 = random.randrange(0,5)
            print("they came from secondly traffic light:" , erx2)
            fan2 =fan2 + erx2
            print ("the first traffic light has:" , fan1)
            print ("the secondly traffic light has:" , fan2)
            print ("the third traffic light has:" , fan3)
    if (fan2==fan3):
        epil = random.choice(traf3)
        print epil
        if (epil==traf3[1]):
            feug = random.randrange(5,10)
            print ("they left:" , feug)
            fan2 = fan2 -feug
            erx1 = random.randrange(0,5)
            print("they came from first traffic light:" , erx1)
            fan1 =fan1 + erx1
            erx3 = random.randrange(0,5)
            print("they came from third traffic light:" , erx3)
            fan3 =fan3 + erx3
            print ("the first traffic light has:" , fan1)
            print ("the secondly traffic light has:" , fan2)
            print ("the third traffic light has:" , fan3)
        else:
            feug = random.randrange(5,10)
            print ("they left:" , feug)
            fan3 = fan3 -feug
            erx1 = random.randrange(0,5)
            print("they came from first traffic light:" , erx1)
            fan1 =fan1 + erx1
            erx2 = random.randrange(0,5)
            print("they came from secondly traffic light:" , erx2)
            fan2 =fan2 + erx2
            print ("the first traffic light has:" , fan1)
            print ("the secondly traffic light has:" , fan2)
            print ("the third traffic light has:" , fan3)
    

