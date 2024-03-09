def dict_from_string(s):
    d = {char: s.count(char) for char in s}
    return d


s = 'pythonist'
print(dict_from_string(s))
