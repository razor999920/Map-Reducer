#!/usr/bin/python
import sys

#Initialize these 2 variables to keep track of unique words (previous) and sum for count of same words (sum)
previous = None
total = 0

#Open checkinsbyday.txt file to write all our unigrams and occurence count to. 
# output = open("checkinsbyday.txt", 'w')

#Loop through the print value sent from umapper.py to analyze each line which contains 1 word
for line in sys.stdin:
    #Store each word as a key and the occurence as the value, this time by a #
    key,value = line.split("#")
    
    #check if we are looking at a unique word or if the current word is the same as the previous seen word. If the word is different than previous, enter the loop. 
    #Once the condition is true and we are looking at a new word, write to the file the total number of occurences for the previous word followed by the previous word itself 
    if key != previous:
        if previous is not None:
            print( previous + '#' + str(total))
        #Reset these values to a new state where previous now equals the new word we are looking at and reset the sum to 0 to count the occurences of the new word we are looking at
        previous=key
        total = 0
    #If we are not looking at a new word, keep adding to the occurence count
    total = total + int(value)

#Lastly, write the last word and its occurences 
print(previous + '#' + str(total))
# output.close()

#End of checkinreducer.py