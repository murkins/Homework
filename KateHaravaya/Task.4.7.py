'''Task 4.7 Implement a function foo(List[int]) -> List[int] which, given a list of integers,
return a new list such that each element at index i of the new list is the product of all the numbers
in the original array except the one at i'''

def foo(example):
    res = []
    number = 1
    for i in example:
        number *= i
    for j in example:
        res.append(number // j)

    return res

print(foo([1, 2, 3, 4, 5]))

