#Task 1.6. Write a Python program to convert a given tuple of positive integers into an integer.

def task_1_6_1(input_tuple):
    sum_res = 0
    multiplyer = 1

    for digit in reversed(input_tuple):
        sum_res += digit * multiplyer
        multiplyer *= 10

    return sum_res
print(task_1_6_1((1, 2, 3, 4)))



