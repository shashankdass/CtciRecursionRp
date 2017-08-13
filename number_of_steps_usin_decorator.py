import time


def timeit(fn):
    def new_fn(*args, **kw):
        start_time = time.time()
        print("starting at:{}".format(start_time))
        result = fn(*args, **kw)
        end_time = time.time()
        print("ending at:{}".format(end_time))
        print("Time elapsed:{}".format(end_time - start_time))
        return result

    return new_fn


@timeit
def number_of_ways_rec(steps):
    if steps == 0:
        return 0
    if steps == 1:
        return 1
    if steps == 2:
        return 1 + number_of_ways_rec(steps - 1)
    if steps == 3:
        return 1 + number_of_ways_rec(steps - 1) + number_of_ways_rec(steps - 2)
    return number_of_ways_rec(steps - 1) + number_of_ways_rec(steps - 2) + number_of_ways_rec(steps - 3)


@timeit
def number_of_ways_dp(steps):
    dp = [0] * (steps + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, steps + 1):
        if i == 2:
            dp[i] = 1 + dp[i - 1]
        elif i == 3:
            dp[i] = 1 + dp[i - 1] + dp[i - 2]
        else:
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[steps]


print(number_of_ways_rec(6))
print(number_of_ways_dp(6))
