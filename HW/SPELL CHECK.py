def split_line(line):
    split = re.findall('[A-Za-z]+(?:\'\"[A-Za-z]+)?', line)
    return split


# Opens the dictionary text file and adds each line to an array, then closes the file
dictionary = open("Notes\data\dictionary.txt")
dict_array = []
for item in dictionary:
    dict_array.append(split_line(item))
print(dict_array)
dictionary.close()

print("---Linear Search---")

# Opens the text for the first chapter of Alice in Wonderland
chapter_1 = open("Notes\data\AliceInWonderland200.txt")

# Breaks down the text by line
for each_line in chapter_1:
    # Breaks down each line to a single word
    words = split_line(each_line)
    # Checks each word against the dictionary array
    for each_word in words:
        i = 0
        # Continues as long as there are more words in the dictionary and no match
        while i < len(dict_array) and each_word.upper() != dict_array[i]:
            i += 1
        # if no match was found print the word being checked
        if not i <= len(dict_array):
            print(each_word)

# Closes the first chapter file
chapter_1.close()