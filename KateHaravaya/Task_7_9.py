'''Task 7.9 Implement an iterator class EvenRange, which accepts start and end of the interval as an init arguments and gives only even numbers during iteration.
If user tries to iterate after it gave all possible numbers `Out of numbers!` should be printed.
_Note: Do not use function `range()` at all_'''

class EvenRange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

        if self.start % 2 == 1:
            self.start += 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.stop:
            return "Out of numbers!"

        cur_iter = self.start
        self.start += 2
        return cur_iter



er1 = EvenRange(3, 14)
try:
    print(next(er1))
    print(next(er1))
    print(next(er1))
    print(next(er1))
    print(next(er1))
    print(next(er1))
    print(next(er1))
    print(next(er1))
    print(next(er1))
    print(next(er1))
    print(next(er1))
    print(next(er1))
    print(next(er1))
    print(next(er1))
    print(next(er1))
except StopIteration:
    print("Out of numbers!")
