from stats import count_words, char_count, sorted_chars

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    characters = char_count(book_text)
    sorted_list = sorted_chars(characters)
    #print(f"{num_words} words found in the document")
    print(f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
""")
    
    for i in sorted_list:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
    
    
main()