# Tuple practice

list_1 = ['a', 'b', 'c']
tuple_1 = tuple(list_1)

tuple_2 = ('a', 'b', 'c')
list_2 = list(tuple_2)

a, b, c = 'a', 2, 'python'

tuple_3 = (1,)
l_tuple_3 = len(tuple_3)
tuple_3 += (2, 3)
for elements in tuple_3:
    print(f'Значение: {elements}')
print(f'Длина кортежа: {l_tuple_3}')
