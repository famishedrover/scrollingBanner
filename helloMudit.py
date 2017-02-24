
import os

import time

#the width of the display
#width is say 79 units wide
WIDTH = 79

#the message
message = "hello! mudit".upper()

# 7-line display, stored as 7 strings
printedMessage = [ "","","","","","","" ]

#a dictionary mapping letters to their 7-line

#use from char import characters 
#or use dict from saved file 
from char import characters

 
#build up the banner
for row in range(7):
    for char in message:
        printedMessage[row] += (str(characters[char][row]) + "  ")


# for r in printedMessage :
#   print r


#the offset is how far to the right we want to print the message.
#initially, we want to print the message just off offset.
offset = WIDTH
while True:
    os.system("clear")
    #print each line of the message, including the offset.
    for row in range(7):
        print(" " * offset + printedMessage[row][max(0,offset*-1):WIDTH - offset])
    
    #move the message a little to the left.
    offset -= 1

    #start again from the right hand side.
    if offset <= ((len(message)+2)*6) * -1:
        offset = WIDTH
    
    #speed of banner scroll
    time.sleep(0.05)