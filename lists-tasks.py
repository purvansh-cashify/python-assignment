'''
Tasks given under lists section in the assignment
'''

# reverse a list
lst = [1, 2, 3, 4, 5]

rev_list = [i for i in reversed(lst)]

print(rev_list)

# concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

list3 = [i + j for i, j in zip(list1, list2)]

print(list3)

# Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

list3 = [i + j for i in list1 for j in list2]

print(list3)

# turning items of a list into their squares
sq_list = [i ** 2 for i in lst]

print(sq_list)

# iterate two lists simultaneously
lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]

for (i, j) in zip(lst1, lst2):
    print(i, j)

# remove empty strings from a list of strings
str_lst = ["abc", "", "hello", "purvansh", "", ""]

str_lst1 = [i for i in str_lst if len(i) != 0]

print(str_lst1)

# add new item to list at specified position
lst = [1, 2, 3, 5]

lst.insert(3, 4)

print(lst)

# Replace list’s item with new value if found
list1 = [5, 10, 15, 20, 25, 50, 20]

for i in range(0, len(list1)):
    if list1[i] == 20:
        list1[i] = 200
        break

print(list1)

# remove all occurrences of a specific item from a list
lst = [1, 1, 2, 2, 2, 3, 4, 2, 5, 2]

while 2 in lst:
    lst.remove(2)

print(lst)
