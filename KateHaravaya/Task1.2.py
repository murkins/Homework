"""Task 1.2. Write a Python program to count the number of characters (character frequency)
 in a string (ignore case of letters)."""

def task_1_2(example_of_string):
    example_of_string = example_of_string.lower()
    hash_table = {}

    for symbol in example_of_string:
       hash_table[symbol] = hash_table.get(symbol, 0) + 1
       
    return hash_table

print(task_1_2("Oh, it is python"))

