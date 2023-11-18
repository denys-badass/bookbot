import string 

def main():
    path_to_book = "books/frankenstein.txt"
    book_contents = read_file(path_to_book)
    words = count_words(book_contents)
    letters = count_letters(book_contents)

    print(words)
    print(letters)

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

    

main()