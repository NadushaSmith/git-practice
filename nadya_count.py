# Функция подсчета слов
def count_words(text):
    words = text.split()
    return len(words)
print(count_words)

# Функция для подсчета уникальных слов
def count_uniq_words(text):
    words = text.split(words)
    uniq_words = set(words)
    return len(uniq_words)
print(count_uniq_words)

# The and!
