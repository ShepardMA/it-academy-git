def create_dictionary(keys, values):
    if len(keys) != len(values):
        raise ValueError("Списки должны быть одной длины")
    my_dictionary = dict(zip(keys, values))
    return my_dictionary


keys_list = ["a", "b", "c"]
values_list = [1, 2, 3]
result_dictionary = create_dictionary(keys_list, values_list)
print(result_dictionary)
