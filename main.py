def main():
    path_to_book = "books/frankenstein.txt"
    book_contents = read_file(path_to_book)
    words = count_words(book_contents)
    print(len(words))

def read_file(path):
    with open(path) as file:
        return file.read()

def count_words(text):
    return len(text.split())

main()