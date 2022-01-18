"""
if the path file exists print an appropriate message to notify user
open up the file
read the file and assign it to variable f
create a string which prints the count of each of the occurences and prints a
statement regarding the number of occurences 
write this to a file results.txt
if the new path file exists print an appropriate message to notify user
"""

import os
if os.path.isfile('HTML.rtf'):
    print("Does this file path exist: true")
else:
    print("Does this file path exist: False")
    
    
f=open('HTML.rtf', 'r')
f = f.read()
string = print("< appears:",f.count("<"), "times", "\n"+ 
               "> appears:",f.count(">"), "times", "\n"+
               "newline appears:",f.count("\n"), "times", "\n"+
               "e appears:",f.count("e"), "times",  "\n"+
               "<!-- appears:",f.count("<!--"), "times", "\n"+ 
               "--> appears:",f.count("-->"), "times", file = open("results.txt","a"))    

if os.path.isfile('results.txt'):
    print("Does this new file path exist: true")

else:
    print("Does this new file path exist: False")
    


 
    
    