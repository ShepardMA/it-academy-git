# Ищем самое длинное слово

all_string = input('Введите предложение: ')
very_long_word = ''
for word in all_string.split():
    if len(word) > len(very_long_word):
        very_long_word = word
print(very_long_word)
