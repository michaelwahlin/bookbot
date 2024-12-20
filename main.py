def main():
    file_path = "books/frankenstein.txt"
    text = get_book(file_path)
    wc = count_words(text)
    char_count = character_count(text)

    print(f"--- Begin report of {file_path} ---")
    print(f"{wc} words found in the document\n")
    for char in char_count:
        print(f"The '{char[1]}' character was found {char[0]} times")
    print("--- End report ---")



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
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    char_count_list = []
    for count in char_count:
        char_count_list.append([char_count[count], count])
    char_count_list.sort(reverse=True)
    
    return char_count_list

main()
