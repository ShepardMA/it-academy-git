def are_anagrams(word1, word2):
    if len(word1) != len(word2):
        return False

    freq_dict = {}
    for char in word1:
        freq_dict[char] = freq_dict.get(char, 0) + 1

    for char in word2:
        if char not in freq_dict or freq_dict[char] == 0:
            return False
        freq_dict[char] -= 1

    return True

