def get_book_text(filepath):
    contents = ""

    with open(filepath) as f:
        contents = f.read()

    return contents

def count_words(file_contents):
    file_split = file_contents.split()
    return len(file_split)

def main():
    file_contents = get_book_text("./books/frankenstein.txt")
    word_count = count_words(file_contents)
    print (f"{word_count} words found in the document")

main()