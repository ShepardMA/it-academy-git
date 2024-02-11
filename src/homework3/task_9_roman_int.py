# Римские цифры в целые

def roman_to_integer(s: str) -> int:
    roman_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    value_1 = 0
    for i in s[::-1]:
        value = roman_val[i]
        if value < value_1:
            total -= value
        else:
            total += value
        value_1 = value

    return total


print(roman_to_integer('MDCLXXVII'))
