def is_palindrome(word):
    cleaned_word = word.lower().replace(" ", "")
    return cleaned_word == cleaned_word[::-1]


