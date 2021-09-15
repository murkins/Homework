"""Task 1.1. Write a Python program to calculate
 the length of a string without using the `len` function"""

def task_1_1(example_of_string):
    result_lenght = 0
    for i in example_of_string:
        result_lenght += 1
    return result_lenght
print(task_1_1("I love Python"))




