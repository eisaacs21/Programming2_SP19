import random
rando_list = [random.randrange(1, 100) for x in range(100)]
print(rando_list)

def selection_sort(my_list):
    for cur_pos in range (len(my_list)):
        min_pos = cur_pos
        for scan_pos in range(cur_pos + 1, len(my_list)):
            if my_list[scan_pos] < my_list[min_pos]:
                min_pos = scan_pos
        my_list[cur_pos], my_list[min_pos] = my_list[min_pos], my_list[cur_pos]

selection_sort(rando_list)
print(rando_list)