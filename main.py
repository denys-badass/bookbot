import string 

def main():
    path_to_book = "books/frankenstein.txt"
    book_contents = read_file(path_to_book)
    letters_dict = count_letters(book_contents)
    letters_value = list(letters_dict.values())
    letters_value.sort(reverse=True)

    print(f"--- Begin report of {path_to_book} ---")
    print(f"{count_words(book_contents)} words found in the document\n")

    for value in letters_value:
        print(f"The {get_key_by_value(letters_dict, value)} character was found {value} times")

    print("--- End report ---")
        


def read_file(path):
    with open(path) as file:
        return file.read()

def count_words(text):
    return len(text.split())

def count_letters(text):
    lower_text = text.lower()
    letters = {}
    for key in string.ascii_lowercase:
        letters[key] = lower_text.count(key)

    return letters

def get_key_by_value(dict, value):
    return list(dict.keys())[list(dict.values()).index(value)]

main()