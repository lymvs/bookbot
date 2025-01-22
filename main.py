BOOK_PATH = "books/frankenstein.txt"

def get_number_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_char_freq(text):
    char_freq = {}
    for c in text.lower():
        if c in char_freq:
            char_freq[c] += 1
        else:
            char_freq[c] = 1
    return char_freq


def sort_on(dict):
    return dict["num"]


def turn_dict_to_list_of_dicts(dict):
    list_dicts = []
    for k, v in dict.items():
        list_dicts.append({"char": k, "num": v})
    return list_dicts


def main():
    text = get_book_text(BOOK_PATH)
    num_words = get_number_words(text)
    char_freq = get_char_freq(text)
    words_list = turn_dict_to_list_of_dicts(char_freq)
    words_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {BOOK_PATH} ---")
    print(f"{num_words} words found in the document")
    print("\n")
    for i in range(len(words_list)):
        if words_list[i]["char"].isalpha():
            print(f"""The '{words_list[i]["char"]}' character was found {words_list[i]["num"]} times""")
    print("--- End report ---")

if __name__ == "__main__":
    main()