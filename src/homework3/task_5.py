# Уникальные элементы в списке

def uniq():
    a = input('Введите элементы разделенные пробелами: ').split()
    b = {}
    for el in a:
        if el not in b:
            b[el] = 1
        else:
            b[el] += 1
    uniq_el = [el for el in b if b[el] == 1]
    return uniq_el

print(uniq())
