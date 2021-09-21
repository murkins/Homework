'''Task 4.2 Write a function that check whether a string is a palindrome or not.
Usage of any reversing functions is prohibited. 
To check your implementation you can use strings from here.'''
def get_palindrome(some_string):
    left = 0
    right = len(some_string) - 1

    res = True

    while left < right:
        if some_string[left] == some_string[right]:
            left += 1
            right -= 1
        else:
            res = False
            break

    return "This string is palindrome" if res else "THis string is not a palindrome"

print(get_palindrome("mazdam"))
