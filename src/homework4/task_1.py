# Dict comprehensions

def create_cube_dict():
    my_dict = {x: x**3 for x in range(1, 21)}
    return my_dict


result = create_cube_dict()
print(result)
