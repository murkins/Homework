'''Task 7.8 Implement your custom iterator class called MySquareIterator
 which gives squares of elements of collection it iterates through.'''

class MySquareIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.stop + 1:
            raise StopIteration
        count = self.start
        self.start += 1
        return count ** 2



itr = MySquareIterator(1, 5)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
for item in itr:
    print(item)


