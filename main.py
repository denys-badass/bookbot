ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():
    path_to_file = 'books/frankenstein.txt'
    text = get_book_text(path_to_file)
    num_of_words = count_words(text)
    chars = count_chars(text)

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{num_of_words} words found in the document")
    print_report(sort_chars(chars))
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_chars(text):
    lower_text = text.lower()
    chars = {}
    for char in lower_text:
        if char in ALPHABET:
            chars[char] = 1 if char not in chars else chars[char] + 1

    return chars

def sort_chars(chars):
   prices_sorted = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))
   return prices_sorted

def print_report(chars):
    for key, value in sort_chars(chars).items():
        print(f"The {key} character was found {value} times")

main()
