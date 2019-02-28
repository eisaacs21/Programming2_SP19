# Searching (Chapter 15 on programarcadegames.com)

# open a file to read
file = open('Notes/data/vill.txt', 'r')  # default is 'r'

for line in file:
    print(line.strip())  # strip removes leading and trailing spaces, /n, /t.

file.close()  # make sure to close it

# to go through the file again, just reopen it
file = open('Notes/data/vill.txt', 'r')  # default is 'r'

for line in file:
    print("Hello", line.strip())

file.close()


# open a file to append to it.
file = open('Notes/data/vill.txt', 'a')  #  a for append

file.write("\nLee the Merciless")

file.close()

file = open('Notes/data/vill.txt')  # default is 'r'

for line in file:
    print("Hello", line.strip())

file.close()


# open and write to a file (THIS OVERWRITES YOUR FILE)

file = open('Notes/data/oscars.txt', 'w')  # if it doesn't exist, it creates one

file.write("Best Picture - Green Book\n")
file.write("Makeup - Black Panther\n")

file.close()

# easier way to open a file and read it
with open('Notes/data/vill.txt') as f:
    # we opened villains to read and assigned it a name f
    for line in f:
        print(line.strip(), end="!\n")


# To use the data, read it into a list
with open('Notes/data/vill.txt') as f:
    villain_list = [x.strip() for x in f]

print(villain_list)

# Linear Search
key = "THE DEADLY RAVEN"
i = 0

while i < len(villain_list) and key != villain_list[i]:
    i += 1
if i < len(villain_list):
    print("Found", key, "at position", i)
else:
    print("COULD NOT FIND")

print(villain_list)

#binary search
villain_list.sort()
print(villain_list)

key = "RENARD THE TORTURER"
lower_bound = 0
upper_bound = len(villain_list) - 1
found = False
loops = 0

# loop until we find it
while lower_bound <= upper_bound and not found:
    loops += 1
    middle_pos = (upper_bound + lower_bound) // 2 # chops off the decimal
    if villain_list[middle_pos] < key:
        lower_bound = middle_pos + 1
    if villain_list[middle_pos] > key:
        upper_bound = middle_pos - 1
    else:
        found = True
if found:
    print("found", key, "at position", middle_pos, "after", loops, "loops")
else:
    print("COULD NOT FIND", key)







