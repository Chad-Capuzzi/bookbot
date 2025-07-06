def count_words(book_text):
    return len(book_text.split())

def char_count(book_text):
    char_dict = {}
    for c in book_text:
        if c.lower() not in char_dict:
            char_dict[c.lower()] = 0
    return char_dict