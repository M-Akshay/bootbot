import sys 
from stats import get_num_words, get_count_characters, chars_to_sorted_list

# Check if the correct number of arguments were provided
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Get the book path from command line arguments
path = sys.argv[1]

# Now you can use book_path instead of hardcoding "books/frankenstein.txt"


def main():
    num = get_num_words(path)
    char_count = get_count_characters(path)
    sorted_chars = chars_to_sorted_list(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")

main()