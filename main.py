
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = unique_char_counter(text)
    text_report = create_report(word_count, char_count)
    #print(f"this book contains these characters: {char_count}")
    #print(f"total words in THIS BOOK: {word_count}")
    print(text_report)

# get the word count and return it
def get_word_count(text):
    words = text.split()
    return len(words)

    # print(file_contents)
    
# get the text of the book and return it
def get_book_text(path):
    with open(path) as f:
        return f.read()

def unique_char_counter(text):
    char_dict = {}
    for char in text:
        if char.isalpha():
            lowered = char.lower()
            if lowered in char_dict:
                char_dict[lowered] += 1
            else:
                char_dict[lowered] = 1
    return char_dict

# create a report of words and the characters
def create_report(words, chars_dict):
    
    report = []
    report.append("--- starting report on BOOK NAME ---")
    report.append(f"Total words: {words} \n")
    dict_list = [{"char": key, "num": value} for key, value in chars_dict.items()]
    sorted_list = sorted(dict_list, key=lambda x: x["num"], reverse=True)
 
    for item in sorted_list:
        char = item["char"]
        num = item["num"]
        report.append(f"The '{char}' character was found {num} times.")
        report.append("")
    report.append("\n --- ending report ---")
    
    return "\n".join(report)
main()


