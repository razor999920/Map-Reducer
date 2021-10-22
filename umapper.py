#!/usr/bin/python
import sys
import re
import csv

# input = open("tester_1.txt", 'w')

#Skip the first line (it is the title for the columns) which do not need analyzing
data = csv.reader(sys.stdin)
next(data)

#Loop through the file being sent via command line
for line in data:
    #Split the column into sections (which are split by commas in the data) to retrieve only the first column, which contains the context
    #Then look for words us import 're', a regular expression tool to help us label words. Store these words into variable 'words'
    line = line[0].split(",")[0]
    line = re.sub(r'^\W+|\W+$', '', line)
    words = re.split(r'\W+', line)

    #Loop through the multiple words stored in variable 'words' and print each word seperately to the standard output. For consistency, convert all words to lowercase and with 1 next to it (for count). 
    for word in words:
        # input.write( word.lower() + "\t1" + "\n")
        print(str(word.lower()) + "\t1")

# input.close()