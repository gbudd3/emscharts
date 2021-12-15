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

def setup_name_dictionary():
    d = {}
    with open("responder_names.csv") as r_names:
        for row in r_names:
            row = row.rstrip()
            na = row.split("|")
            if len(na) == 2 and na[1]:
                for a in na[1].split(","):
                    d[a] = na[0]
    return d


def main():
    names = {}
    responder_names_by_alias = setup_name_dictionary()

    with open(0) as csvfile:
        c = csv.reader(csvfile, delimiter='\t')
        for row in c:
            if row[0] == "PRID":
                continue

            for n in re.split("\s*[,;&]\s*",row[12]):
                if clean(n):
                    if clean(n) in responder_names_by_alias:
                        names[responder_names_by_alias[clean(n)]] = ""
                    else:
                        names[clean(n)]=row[12]


    for n in sorted(names):
        print("'" + n + "'\t ===> " + names[n])

main()
