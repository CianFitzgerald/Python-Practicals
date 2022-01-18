"""
prompt the user to input a string 
assign the variable cat and dog with their respective strings
if the word count of cat is equal to the word count of dog:
    print that cat and dog appear the same number of times
else:
    print that they do not appear the same number of times
"""


word = str(input("enter a string here:"))
cat, dog  = "cat", "dog"
if word.count(cat) == word.count(dog):
    print("cat and dog appear the same number of times")
else:
    print("cat and dog do not appear the same number of times")
