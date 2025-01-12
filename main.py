
def main():
    word_count = 0
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    print(f"total words in THIS BOOK: {word_count}")


def get_word_count(text):
    words = text.split()
    return len(words)

    # print(file_contents)
    
# get the text of the book and return it
def get_book_text(path):
    with open(path) as f:
        return f.read()

main()


