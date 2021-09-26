'''Task5_6 Implement a decorator `call_once` which runs a function or method
 once and caches the result.
All consecutive calls to this function should return cached result no matter the arguments.
'''

first_result = None

def call_once(func):
    def wrapper(a, b):
        global first_result
        if first_result == None:
            result = func(a, b)
            first_result = result
            print(result)
        else:
            print(first_result)

        return first_result

    return wrapper

@call_once
def sum_of_numbers(a, b):
    return a + b

sum_of_numbers(13, 42)
sum_of_numbers(100, 42)
sum_of_numbers(13, 50)

