
#ETHAN ISAACS

import re
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)
dictionary_words = []
file = open('../Notes/data/dictionary.txt', 'r')
for line in file:
    line = line.strip()
    dictionary_words.append(line)
def linear_search(key, dictionary):
    i = 0
    while i < len(dictionary) and dictionary[i] != key:
        i += 1
    if i < len(dictionary):
        return(False)
    else:
        return(True)
def binary_search(key, dictionary):
    lower_bound = 0
    upper_bound = len(dictionary) - 1
    found = False
    while lower_bound <= upper_bound and not found:
        middle_pos = (lower_bound + upper_bound) // 2
        if dictionary[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif dictionary[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True
    if found:
       return(False)
    else:
        return(True)
print("Binary Search YAY")
alice_linefun = []
alice_chapter1 = open('../Notes/data/AliceInWonderland200.txt', 'r')
for line in alice_chapter1:
    words = split_line(line.strip())
    alice_linefun.append(words)
for i in range(len(alice_linefun)):
    for word in alice_linefun[i]:
        found = binary_search(word.upper(), dictionary_words)
        if found:
            print("Line", i, "this word could be wrong bro!: ", word)
print("Linear Search YAY")
alice_fun = []
alice_chapter1 = open('../Notes/data/AliceInWonderland200.txt', 'r')
for line in alice_chapter1:
    words = split_line(line.strip())
    alice_fun.append(words)
for i in range (len(alice_fun)):
    for word in alice_fun[i]:
        found = linear_search(word.upper(), dictionary_words)
        if found:
            print("Line", i, "this word could be wrong bro!: ", word)

print("Lewis Carroll fix these please")

