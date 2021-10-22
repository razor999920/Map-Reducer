#!/usr/bin/python
import sys
import csv

# input = open("tester_2.txt", 'w')

#Store the data recieved from command line in the variable 'data'
#Skip the first line (it is the title for the columns) which do not need analyzing
data = csv.reader(sys.stdin)
next(data)

#Loop through the file being sent via command line
for line in data:  
    #Split the column into sections (which are split by commas in the data) to retrieve which contains the context
    bus_information = line[len(line)-1]
    categories_list = bus_information.split(';')

    #loop through categories stored in categories_list to determine which are included in the business being analyzed
    for  category in categories_list:
        #Remove unneccessary characters stored in the category data 
        if '\r\n' in category:
             category = category.rstrip('\r\n')
        
        #Print to command line the resulting data
        print(category + "\t" + line[0])
        # input.write(category + "\t" + bus_information[0] + "\n")

# input.close()
