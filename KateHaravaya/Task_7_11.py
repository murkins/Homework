'''Task 7.11 Implement a generator which will geterate [Fibonacci numbers] endlessly..'''

def endless_fib_generator():
    fibonacci, f1 = 1, 1
    while True:
        yield fibonacci
        fibonacci, f1 = f1, fibonacci + f1


gen = endless_fib_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))




