'''Task 7.1 Implement class-based context manager for opening and working with file,
 including handling exceptions. Do not use 'with open()'. Pass filename and mode via constructor.'''
import sys
import traceback
class WorkWithFile:
    def __init__(self, file_name, mode):
        self.file_obj = open(file_name, mode)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exception, value, trace):
        if value is not None:
            print(exception, value)
            return True

        self.file_obj.close()
        return True

with WorkWithFile("new_file.txt", "w") as file:
    file.write("Hello, World!\n")


