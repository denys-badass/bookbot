def main():
    path_to_book = "books/frankenstein.txt"
    book_contents = read_file(path_to_book)
    words = book_contents.split()
    print(len(words))

def read_file(path):
    with open(path) as file:
        return file.read()

main()