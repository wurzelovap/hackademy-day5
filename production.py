def remove_duplicates(a_list):
    new_list = []
    for i in a_list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(remove_duplicates([1, 1, 2, 3, 2]))

list1 = [1,2, 3, 4, 5, 2, 6, 4, 3, 8, 9, 1, 1, 8, 3, 2, 1]
print(remove_duplicates(list1))
