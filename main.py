from stats import count_book_words, character_count

def get_book_text(filepath: str) -> str:
    """This function returns the text in a file as a string."""

    with open(filepath, 'r') as f:
        return f.read()

if __name__ == "__main__":
    book_text: str = get_book_text("books/frankenstein.txt")
    book_word_count: int = count_book_words(book_text)
    print(f"Found {book_word_count} total words")
    print(f"{character_count(book_text)}")
