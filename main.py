from sys import argv,exit
from stats import get_number_of_words, get_char_list,sort_dict
def get_book_test(filePath):
    file_contents = None
    with open(filePath) as f:
        file_contents = f.read()
    return file_contents

def main():
    try:
        file_path = argv[1]
        file_contents = get_book_test(file_path)
        num_of_words = get_number_of_words(file_contents.split())
        char_list = get_char_list(file_contents.split())
        word_list = sort_dict(char_list)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_of_words} total words")
        print("--------- Character Count -------")
        for item in word_list:
            for word,count in item.items():
                if not word.isalpha():
                    continue
                print(f"{word}: {count}")
        print("============= END ===============")
    except IndexError:
        print('Usage: python3 main.py <path_to_book>')
        exit(1)
main()