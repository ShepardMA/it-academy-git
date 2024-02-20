# The lists

def count_unique_elements(list1, list2):
    unique_elements = set(list1).symmetric_difference(set(list2))
    return print(len(unique_elements))


count_unique_elements([1, 2, 2, 2, 3, 4,], [2, 3, 5, 7])
