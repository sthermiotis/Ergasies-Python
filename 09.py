#!/usr/bin/python
# -*- coding: utf-8 -*-

nmb = int(input("Please Enter any Number: "))
runn = True
while runn:
    nmb = nmb * 3 + 1
    nmb = sum(map(int, str(nmb)))
    print nmb
    if nmb <= 10:
        runn = False

                
