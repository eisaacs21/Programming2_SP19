# Our Friend the list
import random

my_list = ["Bev", "Abe", "Cam", "Dan", "Eve", "Flo", "Gus"]
my_nums = [8, 4, 7, 5, 2, 19]

print(my_list[1]) # print abe
print(my_list[4:])
print(my_list[:3])
print(my_list[2:4])
print(my_list[-2])
# Make a copy
#my_list2 = my_list #don't do this
my_list2 = my_list[:] # do it like this
my_list2.append("Hal") #add hal
print(my_list2)
print(my_list)

# if in
if "Cam" in my_list:
    print("Cam is in there")

my_list2d = [["Bev", 8], ["Abe", 12], ["Cam", 4]]
print(my_list2d[1][0])




# some list functions
print(min(my_nums))
print(max(my_nums))
print(sum(my_nums))

# Some list methods
my_list.append("Hal")
print(my_list)
print(my_list.count("Abe")) #count the amount
my_list.append("Abe")
print(my_list.count("Abe"))
my_list.insert(3, "Deb")  # insert anywhere
print(my_list)

my_list.sort()
print(my_list)
my_list.append("erv")
print(my_list)
my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

# Important ones
name = my_list.pop() #returns the popped item
print(my_list)
my_list.pop(0) #take off something
print(my_list)

# deleting items
del my_list[4]
print(my_list)

print(my_list.index("Dan")) #gives index of first item found

#ITERATION

my_list = []
for i in range(10):
    my_list.append(i)

print(my_list)


for num in my_list:
    num += 1 #num is just a copy, does not change the list
    print(num)
print(my_list)


#add 10 to each item
for i in range(len(my_list)):
    my_list[i] += 10
print(my_list)


# make a 2d list that is 10 x 10 [[0,0]. [0,1], [0,2], [0,3]...
my_list = []
for i in range(10):
    for j in range(10):
        my_list.append([i, j])

print(my_list)

# print each pair
for pair in my_list:
    print(pair[0], pair[1])

# add 10 to every item

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        my_list[i] [j] += 10

print(my_list)

# list comprehension
# syntatic Sugar
# [returned_item for iterator in range/list filter]

# make a list from 0 to 100

my_list = [x for x in range(100)]
print(my_list)

# make a list of square from 0 to 100
my_list = [x ** 2 for x in range(100)]
print(my_list)

# make a list of squares from 0 to 100 only odd
my_list = [x ** 2 for x in range(100) if x ** 2 % 2 == 1]
print(my_list)

# make a list of 100 random number
#my_list = [random.randrange(1, 101) for x in range(100)]
#print(my_list)

#my_list2 = [x for x in my_list]


# roll two dice 100 time
my_list = [[random.randrange(1,7), random.randrange(1,7)] for x in range(100)]
print(my_list)

# roll 2 dice 100 times only roll 7
my_list = [x for x in [[random.randrange(1,7), random.randrange(1,7)] for x in range(100)] if x[0] + x[1] == 7]
print(my_list)


values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["H",  "D", "C", "S"]
deck = []
for value in values:
    for suit in suits:
        deck.append(value + suit)
print(deck)

# list concatenation

print(values + suits)