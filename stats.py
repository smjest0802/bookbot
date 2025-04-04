def count_words(file_contents):
    file_split = file_contents.split()
    return len(file_split)

def count_letters(file_contents):
    letter_counts = {}
    lower_case = file_contents.lower()
    for character in lower_case:
        if character in letter_counts:
            letter_counts[character] += 1
        else:
            letter_counts[character] = 1
    return letter_counts

def sort_letters(letter_counts):
    sorted_letters = []

    for letter in letter_counts:
        sorted_letters.append({
            "letter": letter,
            "count": letter_counts[letter]
        })

    sorted_letters.sort(key=which_field, reverse=True)

    return sorted_letters

def which_field(entry):
    return entry['count']