'''Task 7.5 Implement function for check that number is even and is greater than 2.
Throw different exceptions for this errors.
Custom exceptions must be derived from custom base exception
(not Base Exception class).'''

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

    return wrapper

@check_errors
def check_number(num):
    if type(num) != int:
        raise InvalidArgTypeException()

    num_is_even = num % 2 == 0
    num_greater_than_2 = num > 2

    if not num_is_even:
        raise NumNotEvenException()

    if not num_greater_than_2:
        raise NumNotGreaterException()

    print("Number is OK")

check_number(2)
check_number(3)
check_number(4)