def main():
    file_path = "books/frankenstein.txt"
    text = get_book(file_path)
    print (count_words(text))
    print(character_count(text))


def get_book(fp):
    with open(fp, "r")  as f:
        return f.read()

def count_words(book_content):
    num_words = 0
    for word in book_content.split():
        num_words += 1
    return num_words

def character_count(book_content):
    char_count = {}
    book_content = book_content.lower()
    for char in book_content:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

main()
