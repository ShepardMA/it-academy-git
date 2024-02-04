# Считаем общую цену

a = int(input("Введите цену в рублях: "))
b = int(input("Введите цену в копейках: "))
c = int(input("Введите количество товаров: "))
price = c * (100 * a + b)
rub = price //100
cent = price % 100
e = "руб"
f = "коп"
print(rub, e, cent, f)