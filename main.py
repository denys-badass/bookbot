def main():
    path_to_file = './books/frankenstein.txt'
    text = get_book_text(path_to_file)
    num_of_words = count_words(text)
    print(num_of_words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

main()
