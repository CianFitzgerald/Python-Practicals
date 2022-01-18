"""
check if the file path exists and print the relevant statemnt if it does or doesn't
open the file and assign it to the variable f
read the file 
if the count of the number of each of the brackets is equal:
    print the amount of each of the brackets and print that the file has balanced brackets
    
else:
    print the amount of each of the brackets and print that the file does not have balanced brackets
"""


import os
if os.path.isfile('HTML.rtf'):
    print("Does this file path exist: True")
else:
    print("Does this file path exist: False")
    
f=open('HTML.rtf', 'r')
f = f.read()

if f.count("<") == f.count(">") and f.count("(") == f.count(")") and f.count("{") == f.count("}"):
    print("there are", f.count("<"),"< brackets and", f.count(">"),"> brackets.")
    print("there are", f.count("("),"( brackets and", f.count(")"),") brackets.")
    print("there are", f.count("{"),"{ brackets and", f.count("}"),"} brackets.")
    print("Therefore the file has balanced brackets")

else:
    print("there are", f.count("<"),"< brackets and", f.count(">"),"> brackets.")
    print("there are", f.count("("),"( brackets and", f.count(")"),") brackets.")
    print("there are", f.count("{"),"{ brackets and", f.count("}"),"} brackets.")
    print("Therefore the file does not have balanced brackets")

