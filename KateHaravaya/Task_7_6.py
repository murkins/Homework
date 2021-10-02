'''Task 7.6 Create console program for proving Goldbach's conjecture.
Program accepts number for input and print result.
For pressing 'q' program succesfully close.
Use function from Task 5.5 for validating input, handle all exceptions and print user friendly output.'''

class CustomException(Exception):
    def __init__(self):
        super().__init__()

class InvalidArgTypeException(CustomException):
    def __init__(self):
        super().__init__()

class NumNotEvenException(CustomException):
    def __init__(self):
        super().__init__()

class NumNotGreaterException(CustomException):
    def __init__(self):
        super().__init__()

class NumNotGoldbachException(CustomException):
    def __init__(self):
        super().__init__()

def check_errors(func):
    def wrapper(*args):
        try:
            func(*args)
        except InvalidArgTypeException:
            print("InvalidArgTypeException: You have passed invalid argument")
        except NumNotEvenException:
            print("NumNotEvenException: You have passed number that is not even ")
        except NumNotGreaterException:
            print("NumNotGreaterException: You have passed number that greater then 2")
        except NumNotGoldbachException:
            print("NumNotGoldbachException: You provided number that is not goldbach")

    return wrapper

def is_prime(n):
    d = 2

    while d * d <= n and n % d != 0:
        d += 1

    return d * d > n

def is_goldback(num):

    for i in range(2, num // 2 + 1):
        if is_prime(i):
            other_num = num - i
            if is_prime(other_num):
                return True

    return False

@check_errors
def check_number(num):
    if type(num) != int:
        raise InvalidArgTypeException()

    num_is_even = num % 2 == 0
    num_greater_than_4 = num >= 4

    if not num_is_even:
        raise NumNotEvenException()

    if not num_greater_than_4:
        raise NumNotGreaterException()

    num_is_goldbach = is_goldback(num)
    if not num_is_goldbach:
        raise NumNotGoldbach

    print("This Number is Goldbach number")

check_number(1)
check_number(4)
check_number(5)
check_number("6")
check_number(6)
check_number(6.20)
check_number(24)
check_number(128)
