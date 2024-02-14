# List practice
def list_1():
    list_2 = [f'{x}{y}' for x in ['a', 'b'] for y in ['b', 'c', 'd']][:: 2]
    return list_2


print(list_1())


list_3 = [f"{i}a" for i in range(1, 5)]
removed_item = list_3.pop(1)
list_4 = list_3.copy()
list_4.append('2a')
print(f"Удаленный элемент: {removed_item}")
print(list_3)
print(list_4)
