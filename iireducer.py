#!/usr/bin/python
import sys

#Initialize these 2 variables to keep track of unique words (previous) and business ids (bus_ids)
previous_key = None
bus_ids = []
# categories_set = {'categories'} 

# input = open("inverted-index.txt", 'w')
#Loop through the print value sent from umapper.py to analyze each line 
for line in sys.stdin:
    #Store each word as a key and the occurence as the value, this time by a tab
    key,value =  line.split( '\t' )
    #Remove unneccessary characters in value in hash map (new line)
    if ('\n' in value):
        value = value.strip('\n')
    #check if we are looking at a unique word or if the current word is the same as the previous seen word. If the word is different than previous, enter the loop. 
    #Once the condition is true and we are looking at a new word, write to the file the total number of occurences for the previous word followed by the previous word itself 
    if key != previous_key:
        if previous_key is not None:
            print(previous_key + " " + ", ".join(bus_ids) + "\n")
            #Reset the ids for business list and append the new business we are currently looking at to the same list
            bus_ids.clear()
            bus_ids.append(value)
        #Assign our current key to the previous_key variable
        previous_key = key
    
    #Edge case for adding business to bus_id list
    if (key == previous_key and value not in bus_ids):
        bus_ids.append(value)

# input.close()
