'''Task 7.3 Implement decorator with context manager
support for writing execution time to log-file.
 See contextlib module.'''

from contextlib import ContextDecorator
import time

class Timer(ContextDecorator):
    def __enter__(self):
        print("Begin timer")
        self.t0 = time.time()
        return self

    def __exit__(self, *exc):
        time_elapsed = time.time() - self.t0

        print(f'Function execution time: {time_elapsed:.6f}')

        with open("log_file_task_7_3.txt", "a") as file_obj:
            file_obj.write(f'Function execution time: {time_elapsed:.6f}')

        return False

@Timer()
def foo():
    for i in range(10000):
        print("I love python")

foo()