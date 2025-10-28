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

def sort_counted_character(char_counts: dict[str, int]) -> list[dict[str,int]]:
    """
    Takes a list of character count mappings for a text and returns them
    in order as a list.
    """

    sorted_counts: list[dict] = []
    for k, v in char_counts.items():
        sorted_counts.append(
                {
                    "char" : k,
                    "num" : v
                    }
            )
    sorted_counts.sort(reverse=True, key=lambda e: e["num"])
    return sorted_counts

