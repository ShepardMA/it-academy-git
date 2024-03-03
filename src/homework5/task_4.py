
original_dict = {1: "один",  2: "два",  3: "три", 4: "четыре"}
dict_items = original_dict.items()


def reverse_dict(original_dict):
    reversed_dict = {}
    for key, value in original_dict.items():
        reversed_dict[value] = key
    return reversed_dict


reversed_dict = reverse_dict(original_dict)
print(reversed_dict)
