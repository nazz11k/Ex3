from math import sqrt, ceil


def check_if_perfect(number):
    return calc_div_sum(number) == number


def calc_div_sum(number):
    div_sum = 0
    for i in range(1, ceil(sqrt(number))):
        if number % i == 0:
            div_sum += i
            if i != 1 and i != number / i:
                div_sum += number / i
    return div_sum
