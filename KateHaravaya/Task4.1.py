#Task 4.1. Implement a function which receives a string and replaces all " symbols with ' and vise versa.

def replase_symbols(s, b ='"', c ="'"):
    result = []
    for i in s:
        if i == b:
            result.append(c)
        elif i == c:
            result.append(b)
        else:
            result.append(i)
    return  "".join(result)

print(replase_symbols('''Hello it's a cat and he has a "mouse"'''))