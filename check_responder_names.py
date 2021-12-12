#! /usr/bin/env python3                                                            

import csv
import re

def clean(s):
    s = re.sub("\(.+\)","",s)
    s = re.sub("-.+$","",s)
    s = s.strip()
    s = s.lower()
    return s

names = {}

with open("data/Output_of_Response_Time_and_Type.txt") as csvfile:
    c = csv.reader(csvfile, delimiter='\t')
    for row in c:
        for n in row[12].split(","):
            names[clean(n)]=""


for n in sorted(names):
    print(n)
