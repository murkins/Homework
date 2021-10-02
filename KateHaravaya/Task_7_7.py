'''Task 7.7 mplement your custom collection called MyNumberCollection. It should be able to contain only numbers.
It should NOT inherit any other collections.
If user tries to add a string or any non numerical object there, exception `TypeError` should be raised.
Method init sholud be able to take either
`start,end,step` arguments, where `start` - first number of collection, `end` - last number of collection or some ordered iterable
collection (see the example).
Implement following functionality:
* appending new element to the end of collection
* concatenating collections together using `+`
* when element is addressed by index(using `[]`), user should get square of the addressed element.
* when iterated using cycle `for`, elements should be given normally
* user should be able to print whole collection as if it was list.'''

def print_error(func):
    def wrapper(*args):
        try:
            func(*args)
        except Exception as e:
            print(e)

    return wrapper

@print_error
def append_collection_to_arr(coll, arr):
    for element in coll:
        if (type(element) == tuple
                or type(element) == list
                or type(element) == set):
            append_collection_to_arr(element, arr)
        elif type(element) != int:
            raise TypeError("MyNumberCollection supports only numbers")
        else:
            arr.append(element)

class MyNumberCollection:
    def __init__(self, *arr):
        self.arr = []

        append_collection_to_arr(arr, self.arr)

    @print_error
    def append(self, num):
        if type(num) != int:
            raise TypeError(f"TypeError: '{num}' is not a number")
        else:
            self.arr.append(num)

    def __add__(self, other):
        new = MyNumberCollection()

        for element in (self.arr + other.arr):
            new.append(element)

        return new

    def __getitem__(self, item):
        return self.arr[item]

    def __repr__(self):
        return str(self.arr)


col1 = MyNumberCollection(0, 5, 2)
print(col1)

col2 = MyNumberCollection((1, 2, 3, 4, 5))
print(col2)

col3 = MyNumberCollection((1, 2, 3, "4", 5))

col1.append(7)
print(col1)

col2.append("string")

print(col1 + col2)
print(col1)
print(col2)
print(col2[4])
for item in col1:
    print(item)
