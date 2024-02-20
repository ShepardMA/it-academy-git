# The lists

def count_common_numbers(list1, list2):
    common_numbers = set(list1) & set(list2)
    return print(len(common_numbers))


count_common_numbers([1, 2, 2, 2, 3, 4,], [2, 3, 5, 7])
