'''Task 4.8 Implement a function get_pairs(lst: List) -> List[Tuple] which returns a list of tuples containing pairs of elements.
 Pairs should be formed as in the example. If there is only one element in the list return None instead.'''

def get_pairs(numbers):
    zipped = None

    if len(numbers) > 0:
        zipped = []
        for i in range(len(numbers) - 1):
            zipped.append((numbers[i], numbers[i + 1]))

    return zipped

print(get_pairs([1, 2, 3, 8, 9]))

