#!/usr/bin/python
import sys
import re
import csv

# input = open("tester_2.txt", 'w')

data = csv.reader(sys.stdin)
next(data)

for line in data:
    #Split the column into sections (which are split by commas in the data) to retrieve only the first column, which contains the context
    #Then look for words us import 're', a regular expression tool to help us label words. Store these words into variable 'words'
    line = line[0].split(",")[0]
    line = re.sub(r'^\W+|\W+$', '', line)
    words = re.split(r'\W+', line)

    next = None
    next_index = 1

    #Loop through the multiple words stored in variable 'words' and print each word seperately to the standard output. For consistency, convert all words to lowercase and with 1 next to it (for count).
    for index in range(len(words) - 1):
        # Next value
        next = words[next_index]

        # input.write( words[index].lower() + " " + next.lower() + "\t1" + "\n")
        print(words[index].lower() + " " + next.lower() + "\t1")
        # Increase index
        next_index += 1

# input.close()