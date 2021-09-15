""" Task 1.3 Write a Python program that accepts a comma separated sequence of words
 as input and prints the unique words in sorted form."""

def task_1_3_1(colors):
    unique_colors = set(colors)
    return sorted(unique_colors)

print(task_1_3_1(['red', 'white', 'black', 'red', 'green', 'black']))

