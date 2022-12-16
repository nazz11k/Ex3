coins = [50, 25, 10, 5, 2, 1]


def exchange(sum):
    result = []
    for coin in coins:
        while sum >= coin:
            result.append(coin)
            sum -= coin
    return result


