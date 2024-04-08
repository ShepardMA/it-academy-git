def find_anagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = "".join(sorted(word.lower()))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return list(anagrams.values())


def group_anagrams(anagrams1):
    return [anagram for anagram in anagrams1 if len(anagram) > 1]



