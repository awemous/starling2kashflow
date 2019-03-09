#!/usr/bin/env python3

import csv
import sys
import os

def convertCSV(filename):
    with open(filename, "rt") as source, open("kash-" + os.path.basename(filename), "wt") as result:
        rdr = csv.reader(source)
        wtr = csv.writer(result, delimiter=',', )
        next(rdr)  # Skip CSV headers
        next(rdr)  # Skip "Opening balance."
        wtr.writerow(['MoneyIn', 'MoneyOut', 'Date', 'Description', 'Reference']) # write header
        for row in rdr:
        	test = 0
        	test = test + (float(row[4]))
        	if test < 0 : 
        		test = -test
        		wtr.writerow(['',round(test,2),row[0],row[1],row[2]])
        	else:
        		wtr.writerow([row[4],'',row[0],row[1],row[2]])

def main(argv):
    convertCSV(argv[0])

if __name__ == "__main__":
    main(sys.argv[1:])
