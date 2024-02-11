# задача на таргет

def find_index(numbers, target):
    dict_index_numbers = {}
    for i, num in enumerate(numbers):
        num_2 = target - num
        if num_2 in dict_index_numbers:
            return [dict_index_numbers[num_2], i]
        else:
            dict_index_numbers[num] = i


print(find_index([2, 3, 145, 14, 15, 154],  299))