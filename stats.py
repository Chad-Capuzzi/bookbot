def count_words(book_text):
    return len(book_text.split())

def char_count(book_text):
    char_dict = {}
    for c in book_text:
        if c.lower() not in char_dict:
            char_dict[c.lower()] = 1
        else:
            char_dict[c.lower()] += 1
    return char_dict

def sorted_chars(char_dict):
    sorted_list = []
    for i in char_dict:
        sorted_list.append({"char": i, "num": char_dict[i]})
    sorted_list.sort(reverse=True, key=sort_on)

def sort_on(items):
    return items["num"]