"""Problem 31

Coin sums
=========

In England the currency is made up of pound, £, and pence, p, and there
are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""
import operator


def count_ways(goal, coins):
    print()
    count = 0
    for total, counts in get_counts(coins, goal):
        print(f'\r{count} {counts}', end='')
        if total == goal:
            count += 1
            print()
    print()
    return count


def get_total(counts, coins):
    return sum(map(operator.mul, counts, coins))


def get_counts(coins, goal):
    counts = [0] * len(coins)
    max_counts = tuple(goal // c for c in coins)
    num_coins = len(coins)

    index = 0
    while True:
        total = get_total(counts, coins)
        yield total, counts

        # find the right index to increase (optimize our search)
        if total >= goal:
            # we need to tick over to the next total smaller than goal. to do
            # that, we need to zero out the left most nonzero coin coint and
            # increase the one to its right
            for i in range(num_coins - 1):
                if counts[i] == 0:
                    continue
                counts[i] = 0
                index = i + 1  # index to increase
                break
            else:
                return  # we ran out of coins to increase
        else:
            # we need to find the smallest index for which increasing it alone
            # can make a sum larger than the goal (and set that as the index to
            # increase below)
            deficit = goal - total
            for i in range(num_coins):
                if (max_counts[i] - counts[i]) * coins[i] >= deficit:
                    index = i  # index to increase
                    break
            else:
                # don't think this should ever happen... maybe if the goal
                # exceeds the maximum coin value? or maybe if the smallest
                # coin is larger than the goal?
                raise Exception(f'wat: goal={goal}, coins={coins}, '
                                f'counts={counts}')

        # now that we know which index to increase, do it
        while True:
            counts[index] += 1
            if counts[index] > max_counts[index]:
                # handle digit rollovers
                counts[index] = 0
                index += 1
                if index >= num_coins:
                    return  # we ran out of coins to increase
            else:
                index = 0
                break


def get_answer(coins, goal):
    dp = [1] + [0] * goal
    for coin in coins:
        for i in range(goal - coin + 1):
            dp[i + coin] += dp[i]
    return dp[-1]


print(get_answer([1, 2, 5, 10, 20, 50, 100, 200], 200))


def answer(goal=200):
    english = (1, 2, 5, 10, 20, 50, 100, 200)
    return count_ways(goal=goal, coins=english)


if __name__ == '__main__':
    print(answer())
