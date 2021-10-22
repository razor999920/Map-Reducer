#!/usr/bin/python
import sys
import csv

#yelp_business, day, #checkins
data = csv.reader(sys.stdin.readlines()[1:])
next(data)

for checkins in data:
    #Because we split every column by a , we can now remove the unwanted second/last column
    checkins.remove(checkins[2])

    #Now that second word is removed, we have less data filter through, saving time
    #Print what we want out for reference and reducer use
    print(checkins[0] + ", " + checkins[1] + ", #" + checkins[2])