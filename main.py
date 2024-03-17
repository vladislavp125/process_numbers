from functools import reduce


def process_numbers(numbers):
    even = list(filter(lambda x: x % 2 == 0 and x > 0, numbers))
    square = list(map(lambda y: y ** 2, even))
    return reduce(lambda x, y: x + y, square)


print(process_numbers([2, 3, 4, 5, 6, 7, -1, -300]))
