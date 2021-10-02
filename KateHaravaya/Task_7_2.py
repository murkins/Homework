'''Task 7.2 Implement context manager for opening and working with file,
including handling exceptions with @contextmanager decorator.'''

from contextlib import contextmanager

@contextmanager
def open_file(name_file, mode):
    file_obj = open(name_file, mode)
    try:
        yield file_obj
    except Exception as e:
        print(f"In file '{name_file} caught exception: {e}")
    finally:
        file_obj.close()

with open_file("new_file2.txt", "r") as file_obj:
    file_obj.write("Hello, World!\n")



