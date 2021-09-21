#Task 4.5 Implement a function get_digits(num: int) -> Tuple[int] which returns a tuple of a given integer's digits.

def get_digits(number):
    result_tuple = (0)
    if number != 0:
        result = []
        while number > 0:
            result.append(number % 10)
            number = number // 10

        result_tuple = tuple(result[::-1])

    return result_tuple

print(get_digits(998766787656789))
print(get_digits(0))
