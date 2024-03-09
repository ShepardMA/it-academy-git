# The words

def count_uniq_words(text):
    words = text.split()
    unique_words = set(words)
    return len(unique_words)


input_text = "Мама мыла раму, рама мыла маму"
print(f"Количество различных слов в тексте: {count_uniq_words(input_text)}")
