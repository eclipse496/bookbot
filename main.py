def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    char_count = count_characters(book_text)

    print(f"=== Begin report of {book_path} ===")
    print(f"Document has {get_num_words(book_text)} words")
    char_count = count_characters(book_text)
    
    print()
    for entry in char_count:
        if not entry["character"].isalpha():
            continue
        else:
            print(f"'{entry['character']}' was found {entry['count']} times")
    print("=== End report ===")

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
    
    sorted_dict = []
    for key in character_count:
        sorted_dict.append({"character":key, "count":character_count[key]})
    sorted_dict.sort(reverse=True, key=sort_on)
    
    return sorted_dict

def sort_on(dict):
    return dict["count"]

main()