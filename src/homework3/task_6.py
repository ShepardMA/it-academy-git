# Упорядоченный список.

def move_numbers(arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        if arr[left] == 0:
            arr.pop(left)
            arr.append(0)
            right -= 1
        else:
            left += 1

    print(arr)


number_list = [1, 2, 3, 4, 5, 0, 0, 1, 0, 1, 0, 0, 8, 7, 6, 8]
move_numbers(number_list)
