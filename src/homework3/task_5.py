# Уникальные элементы в списке

def uniq():
    a = input('Введите элементы: ').split()
    b = {}
    for el in a:
        if el not in b:
            b[el] = 1
        else:
            b[el] += 1
    for el in b:
        if b[el] == 1:
            return el


print(uniq())
