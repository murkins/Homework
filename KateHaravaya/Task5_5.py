'''Task5_5 Implement a decorator `remember_result`
which remembers last result of function it decorates
and prints it before next call. '''

last_result = None

def remember_result(func):
    def wrapper(*args):
        global last_result
        print(f'Last result = {last_result}')

        result = func(*args)
        last_result = result

        return result

    return wrapper

@remember_result
def sum_list(*args):
    result = ""

    if type(args[0]) == int:
        result = 0

    for item in args:
        result += item

    print(f"Current result = '{result}'")

    return result

sum_list('a', 'bc')
sum_list('abc', 'def', 'jek')
sum_list(10, 20, 30, 40)

