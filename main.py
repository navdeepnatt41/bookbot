def get_book_text(filepath: str) -> str:
    with open(filepath, 'r') as f:
        return f.read()

if __name__ == "__main__":
    print(get_book_text("books/frankenstein.txt"))
