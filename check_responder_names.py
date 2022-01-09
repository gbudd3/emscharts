#! /usr/bin/env python3                                                            

import csv
import re
import database
import collections

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

def emscharts_dtg_to_iso(dtg):
    return re.sub(r"(\d\d)/(\d\d)/(\d\d\d\d) ",r"\3-\2-\1 ", dtg)


def main():
    database.setup_database()
    conn = database.get_database()
    cursor = conn.cursor()

    names = {}
    name_charts = collections.defaultdict(list)
    responder_id = {}
    responder_names_by_alias = setup_name_dictionary()
    chart_id = 1
    member_id = 1

    with open(0) as csvfile:
        c = csv.DictReader(csvfile, delimiter='\t')
        for row in c:
            cursor.execute("insert into charts values( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                chart_id,
                row['PRID'],
                row['Dispatch ID'],
                emscharts_dtg_to_iso(row["Date Dispatched"]),
                emscharts_dtg_to_iso(row["Date Enroute"]),
                emscharts_dtg_to_iso(row["Date Arrived"]),
                row['Disposition (Outcome)'],
                row['Unit'],
                row['Basesite'],
                row['Dispatched As'],
                row['Type of Service (IH/Scene)'],
                row['Age In Years (Calc)'],
                row['Gender'],
                row['Referring USNG']
            ))
            print(f"Insert {chart_id} with {row['PRID']}")

            for n in re.split("\s*[,;&]\s*",row['Crew - All']):
                if clean(n):
                    if clean(n) in responder_names_by_alias:
                        names[responder_names_by_alias[clean(n)]] = ""
                        name_charts[responder_names_by_alias[clean(n)]].append(chart_id)
                    else:
                        names[clean(n)]=row['Crew - All']
            chart_id += 1

    conn.commit()

    for n in sorted(names):
        print("'" + n + "'\t ===> " + names[n])
        cursor.execute("insert into members values( ?, ?)", (member_id, n))
        responder_id[n] = member_id

        member_id += 1

    conn.commit()

    for name in name_charts.keys():
        for i in name_charts[name]:
            cursor.execute("insert into member_charts values(?, ?)", (i, responder_id[name]))
            
    conn.commit()
    conn.close()


main()
