def biggest_dict(**kwargs):
    my_dict = {}
    for key, value in kwargs.items():
        my_dict[key] = value
    return my_dict


result = biggest_dict(first_one="we can do it")
print(result)