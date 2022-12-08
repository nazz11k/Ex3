

def simple_numbers_generator():
    numbers = [x for x in range(1, 1001)]
    for number in numbers[1:500]:
        if number is not None:
            for i in range(2 * number, 1001, number):
                numbers[i - 1] = None
    return [x for x in numbers if x is not None and x >= 100]


def sum_of_digits(number):
    result = 0
    while number > 0:
        result += number % 10
        number //= 10
    return result


def find_required_numbers(n):
    numbers = simple_numbers_generator()
    result = 0
    for number in numbers:
        if sum_of_digits(number) == n:
            result += 1
    return result




