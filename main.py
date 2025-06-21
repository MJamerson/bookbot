from stats import get_word_count
from stats import get_char_count
from stats import sort_dict_by_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def generate_report(filepath, word_count, sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_dict:
        if str.isalpha(entry["char"]):
            print(f"{entry["char"]}: {entry["num"]}")


def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    word_count = get_word_count(book_text)
    char_count = get_char_count(book_text)
    sorted_dict = sort_dict_by_count(char_count)
    generate_report(filepath, word_count, sorted_dict)


if __name__ == "__main__":
    main()