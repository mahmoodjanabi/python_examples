a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 5 ,5, 6, 7, 8, 9, 10, 11, 12, 13]
common_list = []

#Check for common elements in both lists
for a_element in a:
    for b_element in b:
        if a_element == b_element:
            common_list.append(str(a_element))

print(common_list)
common_list = list(set(common_list))
print(common_list)