from stats import count_words, char_count, sorted_chars
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exti(1)

    book_text = get_book_text(sys.argv[1])
    num_words = count_words(book_text)
    characters = char_count(book_text)
    sorted_list = sorted_chars(characters)
    #print(f"{num_words} words found in the document")
    print(f"""
============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
""")
    
    for i in sorted_list:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
    
    
main()