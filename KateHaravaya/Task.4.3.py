#4.3 Implement a function which works the same as str.split method (without using str.split itself, ofcourse).

def split_string(s, symbol = ' '):
    res = []
    current_word = []

    for i in s:
        if i != symbol:
            current_word.append(i)
        else:
            if len(current_word) != 0:
                res.append(''.join(current_word))
                current_word = []

    if len(current_word) != 0:
        res.append(''.join(current_word))

    return res
print(split_string('    I love Python   very  mach!'))

