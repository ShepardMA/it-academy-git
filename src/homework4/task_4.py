# The lists

def count_unique_elements(list1, list2):
    unique_elements = set(list1).symmetric_difference(set(list2))
    return len(unique_elements)


result = count_unique_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])
print(f"Количество уникальных чисел: {result}")
