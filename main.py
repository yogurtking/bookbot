
def main():
    word_count = 0
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        for i in range(len(words)):
            word_count += 1

    print(file_contents)
    print(f"total words in THIS BOOK: {word_count}")



main()


