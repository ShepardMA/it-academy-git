# The lists

def count_common_numbers(list1, list2):
    common_numbers = set(list1) & set(list2)
    return len(common_numbers)


result = count_common_numbers([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])
print(f"Количество общих чисел: {result}")
