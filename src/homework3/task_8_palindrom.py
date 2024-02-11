# condition: Given an integer x, return true if x is a palindrome, and false otherwise.
# Could you solve it without converting the integer to a string?

def palindrome(x: int) -> bool:
    if x < 0:
        return False
    number_2 = x
    rev = 0
    while number_2 > 0:
        remainder = number_2 % 10
        rev = 10 * rev + remainder
        number_2 //= 10
    return rev == x


print(palindrome(1221))
