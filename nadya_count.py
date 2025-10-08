def count_words(text):
    words = text.split()
    return len(words)
print('Rebase practice')

def find_longest_word(text):
    """Функция для поиска самого длинного слова"""
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)