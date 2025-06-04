from stats import get_book_text, number_of_words, number_of_chars, sort_chars_dict
import sys

def main(path_to_file):
    num_words = number_of_words(get_book_text(path_to_file))
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {path_to_file}...')
    print('----------- Word Count ----------')
    print(f"Found {num_words} total words")
    print('--------- Character Count -------')
    result = sort_chars_dict(number_of_chars(path_to_file))
    for char_dict in result:
        print(f'{char_dict['char']}: {char_dict['num']}')
    print('============= END ===============')

if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
main(sys.argv[1])