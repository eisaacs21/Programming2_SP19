'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''

#1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.
#IMPORT THE DICTIONARY
dictionary = open('../Notes/data/dictionary', 'r')


for line in dictionary:
    word = line.strip()
    dictionary_list = [x.strip() for x in dictionary]
    dictionary_len = [len(x) for x in dictionary_list]
print(dictionary_list[dictionary_len.index(max(dictionary_len))])




#2.  (8pts)  Write code which finds
# The total word count AND average word length
# in "AliceInWonderLand.txt"

# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

#3 (12pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?
file = open('../Notes/data/alice.txt')
number_chesh = 0
words = "Cheshire"

while number_chesh == 0:
    if words in file:
        number_chesh +=1
        print(number_chesh)












#### OR #####

#3  (12pts)Find the most frequently occurring
# seven letter word in "AliceInWonderLand.txt"
seven_letter_words = []
alice_stuff = []
from collections import Counter

for i in range(len(alice_stuff)):
    if len(alice_stuff[i]) == 7:
        seven_letter_words.append(alice_stuff[i])
c = Counter(seven_letter_words)
print("")
print (c.most_common(1))

# Challenge problem (for fun).  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".  Make a list.  You can substitute this for any of the above problems.



