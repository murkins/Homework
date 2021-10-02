'''Task 7.4 Implement decorator for supressing exceptions.
 If exception not occure write log to console..'''

def suppress_errors(func):
    def wrapper():
        try:
            func()

            print("No error occured!")
        except Exception as e:
            pass

    return wrapper

@suppress_errors
def foo():
    with open("new_file.txt", "r") as file:
        print(file.read())

@suppress_errors
def bar():
    with open("file_that_not_exist.txt", "r") as file:
        print(file.read())

foo()
bar()