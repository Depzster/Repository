def process_lists(list1, list2):
    combined_list = list1 + list2
    unique_list = list(set(combined_list))
    powered_list = [item ** 3 for item in unique_list]
    return powered_list


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
result = process_lists(list1, list2)
print(result)
