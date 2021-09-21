'''Task 4.6 Implement a function get_shortest_word(s: str) -> str which returns the longest word in the given string.
The word can contain any symbols except whitespaces ( , \n, \t and so on). 
If there are multiple longest words in the string with a same length return the word that occures first.'''

def get_longest_word(s, symbol = ' '):
    res = ''
    current_world = []

    for i in s:
        if i != symbol:
            current_world.append(i)

        else:
            if len(current_world) > 0:
                if len(current_world) > len(res):
                    res = ''.join(current_world)
                current_world = []

        if len(current_world) > len(res):
            res = ''.join(current_world)
    return res

print(get_longest_word('Python is simple and effective!'))
