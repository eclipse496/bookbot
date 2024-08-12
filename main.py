def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    
    print(get_num_words(book_text))
    count_characters(book_text)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_num_words(text):
    text_as_list = text.split()
    return len(text_as_list)

def count_characters(text):
    lowercased_text = text.lower()

    character_count = {}
    for char in lowercased_text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    
    print(character_count)


main()