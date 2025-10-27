def count_book_words(file_text: str) -> int:
    """This functions returns the number of words in a string representing the text of a book"""

    return len(file_text.split())

def character_count(file_text: str) -> dict[str, int]:
    """
    This function returns a dictionary mapping characters to the number
    of times it they were found in a text.
    """
    
    char_counts: dict[str, int] = {}
    for c in file_text.lower():
        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1

    return char_counts
