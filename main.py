def main():
    book_path = "books/frankenstein.txt"
    print_report(book_path)


def print_report(book_path):
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    unique_char_count = unique_char_counter(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    print_char_report(unique_char_count)
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def unique_char_counter(text):
    lowered_string = text.lower()
    unique_char_dict = {}
    for character in lowered_string:
        if character in unique_char_dict:
            unique_char_dict[character] += 1
        else:
            unique_char_dict[character] = 1
    return unique_char_dict


def sort_on_num(dict):
    return dict["num"]


def print_char_report(char_dict):
    characters = []
    for character in char_dict:
        if character.isalpha():
            characters.append({
                "character": character,
                "num": char_dict[character]
            })
    characters.sort(reverse=True, key=sort_on_num)
    for entry in characters:
        print(f"The '{entry["character"]}' character was found {entry["num"]} times")
    
main()
