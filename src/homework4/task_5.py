# The languages

def language():
    n = int(input("Введите количество школьников: "))
    language_dict = {}
    for _ in range(n):
        languages = input("Введите языки, которые знает текущий школьник: ").split()
        for lang in languages:
            language_dict[lang] = language_dict.get(lang, 0) + 1
    all_known_languages = [lang for lang, count in language_dict.items() if count == n]
    any_known_languages = list(language_dict.keys())
    print(len(all_known_languages))
    print(*all_known_languages, sep='\n')
    print(len(any_known_languages))
    print(*any_known_languages, sep='\n')


language()
