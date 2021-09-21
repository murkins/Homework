'''Task 4.4. Implement a function split_by_index(s: str, indexes: List[int]) -> List[str]
which splits the s string by indexes specified in indexes. Wrong indexes must be ignored'''

def split_by_index(s, index):
    res = []
    current_word = []
    index.append(len(s))
    index.sort()

    next_index_at = 0
    i = 0
    while i < len(s):
        if i != index[next_index_at]:
            current_word.append(s[i])
            i += 1
        else:
            res.append(''.join(current_word))
            current_word = []
            next_index_at += 1

    if current_word:
        res.append(''.join(current_word))

    return res

print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))

