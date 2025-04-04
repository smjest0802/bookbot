from stats import count_words
from stats import count_letters
from stats import sort_letters

def get_book_text(filepath):
    contents = ""

    with open(filepath) as f:
        contents = f.read()

    return contents

def main():
    filename = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filename}")
    file_contents = get_book_text(filename)
    word_count = count_words(file_contents)
    print ("----------- Word Count ----------")
    print (f"Found {word_count} total words")
    letter_count = count_letters(file_contents)
    sorted_letters = sort_letters(letter_count)
    print ("--------- Character Count -------")
    for entry in sorted_letters:
        if entry["letter"].isalpha():
            print (f"{entry["letter"]}: {entry["count"]}")
    print ("============= END ===============")

main()