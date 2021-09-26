'''Task5_2. Implement a function which search for most common words in the file.
Use `data/lorem_ipsum.txt` file as a example.

python
def most_common_words(filepath, number_of_words=3):
    pass

print(most_common_words('lorem_ipsum.txt'))
 ['donec', 'etiam', 'aliquam']'''

import data
import string
def get_most_common_words(file_path, number_of_words=3):
    file = open(file_path, "r")
    file_text = file.read()

    # Getting list of words in file
    current_word = []
    list_words = []
    for character in file_text:
        if character.isalpha():
            current_word.append(character)
        else:
            if len(current_word) > 0:
                list_words.append(''.join(current_word).lower())
                current_word = []

    if len(current_word) > 0:
        list_words.append(''.join(current_word).lower())
        current_word = []

    # creating Word -> Count mapping
    word_to_count = {}
    for word in list_words:
        word_to_count[word] = word_to_count.get(word, 0) + 1

    sorted_by_count = sorted(word_to_count.items(), key=lambda pair:pair[1])


    most_common_words = []
    for i in range(number_of_words):
        word_to_append = sorted_by_count[len(sorted_by_count) - 1 - i][0]
        most_common_words.append(word_to_append)

    return most_common_words

print(get_most_common_words("data/lorem_ipsum.txt"))
