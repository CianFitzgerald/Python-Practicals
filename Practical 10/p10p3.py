'''
assign cowls and capital vowels to a variable vowel
prompt the user to enter a word
initiate the count at zero
for letter in word:
    if letter is in the variable vowel i.e if any of the vowels are in the letter:
        increase the count by one 
print the number of total counts (the number of vowels in the word)
'''

vowel = ['a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"]
word = input("Enter a word: ")
count = 0
for letter in word:
    if letter in vowel:
        count += 1
print(word,"has",count,"vowels in it")