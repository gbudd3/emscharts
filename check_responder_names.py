#! /usr/bin/env python3                                                            

import csv
import re

def clean(s):
    s = re.sub("\(.+?\)","",s)
    s = re.sub("\s*(\w)\.\s*",r"\1",s)
    s = re.sub("-.+$","",s)
    s = re.sub("\s+"," ",s)
    s = s.strip()
    s = s.lower()
    return s

names = {}

def main():
    with open("data/Output_of_Response_Time_and_Type.txt") as csvfile:
        c = csv.reader(csvfile, delimiter='\t')
        for row in c:
            if row[0] == "PRID":
                continue

            for n in re.split("\s*[,;&]\s*",row[12]):
                if clean(n):
                    names[clean(n)]=row[12]


    for n in sorted(names):
        print(n + "\t ===> " + names[n])

main()
