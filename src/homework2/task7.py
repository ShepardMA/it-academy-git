# Определяем даны ли нам стороны треугольника, и если это треугольник находим площадь

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    s = pow((p * (p - a) * (p - b) * (p - c)), 1 / 2)
    print('Это треугольник с площадью: ', s)
else:
    print('Это не треугольник')