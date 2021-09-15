#Task 1.6.2 Write a program which makes a pretty print of a part of the multiplication table.

def task_1_6_2(a, b, c, d):

    #first string
    first_str = [' ']
    for cd in range(c, d + 1):
        first_str.append(str(cd))
    result_first_str = '\t'.join(first_str)

    result_strings = [result_first_str]

    #next strings
    for ab in range(a, b + 1):
        next_str = [str(ab)]

        for cd in range(c, d + 1):
            first_num = str(ab * cd)
            next_str.append(first_num)
        
        result_next_str ='\t'.join(next_str)
        result_strings.append(result_next_str)

    return '\n'.join(result_strings)


print(task_1_6_2(2, 4, 3, 7))


