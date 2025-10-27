def get_book_text(filepath: str) -> str:
    """This function returns the text in a file as a string."""

    with open(filepath, 'r') as f:
        return f.read()

def count_book_words(file_text: str) -> int:
    """This functions returns the number of words in a string representing the text of a book"""

    return len(file_text.split())

if __name__ == "__main__":
    book_text: str = get_book_text("books/frankenstein.txt")
    book_word_count: int = count_book_words(book_text)
    print(f"Found {book_word_count} total words")
