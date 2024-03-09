# The cache decorator

def cache(user_function):
    cache_dict = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache_dict:
            return cache_dict[key]
        result = user_function(*args, **kwargs)
        cache_dict[key] = result
        return result
    return wrapper
