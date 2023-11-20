def upper_word(input_str):
    """Функция принимает на вход строку и возвращает ее со всеми заглавными буквами"""
    return input_str.upper()


def capitalize_words(input_str):
    """Функция делает заглавными первые буквы каждого слова в строке"""
    return ' '.join(word.capitalize() for word in input_str.split())

