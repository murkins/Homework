'''Task 4.9 Implement a bunch of functions which receive a changeable number of strings and return next parameters:
1.	characters that appear in all strings
2.	characters that appear in at least one string
3.	characters that appear at least in two strings
4.	characters of alphabet, that were not used in any string
Note: use string.ascii_lowercase for list of alphabet letters '''

import string
def get_characters_1(number_of_strings):
    characters = []

    string_sets = [set(x.lower()) for x in number_of_strings]

    for c in string.ascii_lowercase:
        c_exist_in_all = True
        for cur_set in string_sets:
            if c not in cur_set:
                c_exist_in_all = False
                break

        if c_exist_in_all:
            characters.append(c)

    return characters

print(get_characters_1(["hello", "world", "python", ]))

def get_characters_2(number_of_strings):
    string_sets = [set(x.lower()) for x in number_of_strings]

    result_set = set()
    for cur_set in string_sets:
        result_set = result_set.union(cur_set)

    return list(result_set)

print(get_characters_2(["hello", "world", "python", ]))

def get_characters_3(number_of_strings):
    string_sets = [set(x.lower()) for x in number_of_strings]

    characters = []
    for c in string.ascii_lowercase:
        counter = 0
        for cur_set in string_sets:
            if c in cur_set:
                counter += 1

        if counter >= 2:
            characters.append(c)

    return characters

print(get_characters_3(["hello", "world", "python", ]))

def get_characters_4(number_of_strings):
    characters = []

    string_sets = [set(x.lower()) for x in number_of_strings]

    for c in string.ascii_lowercase:
        c_not_exist_in_all = True
        for cur_set in string_sets:
            if c in cur_set:
                c_not_exist_in_all = False
                break

        if c_not_exist_in_all:
            characters.append(c)

    return characters

print(get_characters_4(["hello", "world", "python", ]))

