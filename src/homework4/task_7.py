# The euclidean_algorithm

def euclidean_algorithm(a, b):
    x, y = a, b
    while y != 0:
        r = x % y
        x, y = y, r
    return x


number1 = 18
number2 = 48
result = euclidean_algorithm(number1, number2)
print(f"НОД чисел {number1} и {number2} равен {result}")
