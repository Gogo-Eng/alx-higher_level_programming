#!/usr/bin/python3
list_division = __import__('4-list_division').list_division

my_l_1 = [10, 0, 4]
my_l_2 = [2, 4, 0]
result = list_division(my_l_1, my_l_2, 3)#max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H" , 2, 7]
result = list_division(my_l_1, my_l_2, 5)# max(len(my_l_1), len(my_l_2)))
print(result)

