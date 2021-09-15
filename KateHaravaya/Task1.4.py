# Task 1.4. Write a Python program to sort a dictionary by key.

def task_1_4(amount_of_fruit):
    sorted_dict_by_key = {key: amount_of_fruit[key] for key in sorted(amount_of_fruit)}
    return sorted_dict_by_key

print(task_1_4({'pears':33, 'apples':4, 'bananas':5, 'plums':7}))


