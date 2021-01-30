#!/usr/bin/env python3

import os, re, random

filepath = "affirmations.txt"

#count the number of entries in filepath
with open(filepath) as lc:
    linecount = 0
    for cnt, line in enumerate(lc):
        linecount += 1

#randomize which line to select
random1 = random.randint(0,linecount-1)    

#select a random entry from the list
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        if cnt == random1:
            select = line

print(select)            