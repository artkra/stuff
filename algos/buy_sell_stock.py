import random


def trade(arr):
    trades = []
    buy = []

    for i, price in enumerate(arr):
        if len(buy) == 0:
            buy.append((i, price))
        elif len(buy) == 1 and price > buy[0][1]:
            buy.append((i, price))
        elif len(buy) == 1 and price < buy[0][1]:
            buy.pop()
            buy.append((i, price))
        elif len(buy) > 1 and price > buy[-1][1]:
            buy.pop()
            buy.append((i, price))
        elif len(buy) > 1 and price < buy[-1][1]:
            a = buy.pop()
            b = buy.pop()
            trades.append((b, a))
            buy.append((i, price))

    return trades


if __name__ == '__main__':
    arr = [random.randint(0, 300) for _ in range(random.randint(5, 20))]
    print(arr)
    print(trade(arr))