# Считает количество переданных аргументов, и возвращает их количество

def arguments_length(*args):
    return len(args)


print(arguments_length((1, 2, 3,), [1, 2, 3], 'tar', False))
