# List practice
def list_1():
    list_2 = [f'{x}{y}' for x in ['a', 'b'] for y in ['b', 'c', 'd']][:: 2]
    return list_2


print(list_1())


def list_5():
    list_3 = [str(i) + 'a' for i in range(1, 5)]
    list_3 = [str(i) + 'a' for i in range(1, 5) if i != 2]
    list_4 = list_3.copy()
    list_4.append('2a')
    return list_3, list_4


print(list_5())
