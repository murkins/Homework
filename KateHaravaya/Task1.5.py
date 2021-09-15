# Task 1.5. Write a Python program to print all unique values of all dictionaries in a list.

def task_1_5(input_array):
    unique_values = set()

    for cur_dict in input_array:
        for val in cur_dict.values():
            unique_values.add(val)
    return list(unique_values)

print(task_1_5([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]))

