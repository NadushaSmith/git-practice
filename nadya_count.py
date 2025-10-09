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

print('Rebase practice')

def find_longest_word(text):
    """Функция для поиска самого длинного слова"""
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)

