#!/usr/bin/python
import sys
import re
import csv

data = csv.reader(sys.stdin)
next(data)

# input = open("tester_3.txt", 'w')

#Loop through the file being sent via command line
for line in data:
    #Split the column into sections (which are split by commas in the data) to retrieve only the first column, which contains the context
    #Then look for words us import 're', a regular expression tool to help us label words. Store these words into variable 'words'
    line = line[0].split(",")[0]
    line = re.sub(r'^\W+|\W+$', '', line)
    words = re.split(r'\W+', line)

    #These booleans will be used for holding second and third values of the trigram 
    #second and third indexes are also identified by 1 and 2, respectively 
    second_next = None
    third_next = None
    second_index = 1
    third_index = 2

    #Loop through the multiple words stored in variable 'words' and print each word seperately to the standard output. For consistency, convert all words to lowercase and with 1 next to it (for count). 
    for index in range(len(words) - 2):
        #Analyze the next values (second and third)
        second_next = words[second_index]
        third_next = words[third_index]

        # input.write(words[index].lower() + " " + second_next.lower() + " " + third_next.lower() + "\t1" + "\n")
        print(words[index].lower() + " " + second_next.lower() + " " + third_next.lower() + "\t1")
        # Increase index
        second_index += 1
        third_index += 1

# input.close()