from stats import count_book_words, character_count, sort_counted_character

def get_book_text(filepath: str) -> str:
    """This function returns the text in a file as a string."""

    with open(filepath, 'r') as f:
        return f.read()

if __name__ == "__main__":
    book_text: str = get_book_text("books/frankenstein.txt")
    book_word_count: int = count_book_words(book_text)
    sorted_char_counts: list[dict] = sort_counted_character(character_count(book_text))    
    char_key: str = "char"
    num_key: str = "num" 

    print("============ BOOKBOT ============")
    print("analyzing book found at books/frankenstein.txt")
    print("----------- Word Count -----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")
    for elem in sorted_char_counts:
        if elem["char"].isalpha():
            print( f"{elem[char_key]}: {elem[num_key]}" )
    print("============= END ===============")
