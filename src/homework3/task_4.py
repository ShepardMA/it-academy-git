# Пары элементов
def count_pairs():
    numbers = input("Введите числа разделенный пробелами: ").split()
    dict_1 = {}
    for num in numbers:
        if num in dict_1:
            dict_1[num] += 1
        else:
            dict_1[num] = 1
    total_pairs = 0
    for count in dict_1.values():
        total_pairs += count * (count - 1) // 2
    return "Количество пар: ", total_pairs


print(count_pairs())
