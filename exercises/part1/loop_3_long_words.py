words = ["api", "backend", "ui", "database", "test", "architecture"]


def get_long_words(words, min_length):
    long_words = []
    for word in words:
        if len(word) >= min_length:
            long_words.append(word)
    return long_words

print(get_long_words(words, 5))    # ["backend", "database", "architecture"]
print(get_long_words(words, 20))   # []
print(get_long_words([], 5))       # []
