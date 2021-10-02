'''Task 7.10 Implement a generator which will generate odd numbers endlessly.'''

def endless_generator():
    odd_number = 1
    while True:
        yield odd_number
        odd_number += 2


gen = endless_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))




