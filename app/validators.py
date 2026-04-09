bad_words = ["редиска", "бяка", "козявка"]


def no_forbidden_words(text: str):
    """Проверка на запрещенные слова в тексте"""
    for word in bad_words:
        if word[:-2] in text.lower():
            raise ValueError("Использование недопустимых слов")
    return text
