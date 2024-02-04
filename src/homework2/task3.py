# Удаляем повторяющиеся символы и пробелы

s = input("Введите текст или цифры: ")
s_new = ''
for i in s:
    if i not in s_new and i != ' ':
        s_new += i
print(s_new)