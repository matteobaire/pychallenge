from timeit import default_timer as timer


def count_coins(som, coins):
    ways_to_make = [0 for _ in xrange(som + 1)]
    ways_to_make[0] = 1
    for coin in coins:
        for t in xrange(som + 1):
            if t >= coin:
                ways_to_make[t] += ways_to_make[t - coin]
        print ways_to_make

    return ways_to_make[som]


start = timer()
ans = count_coins(200, [1, 2, 5, 10, 20, 50, 100, 200])
elapsed_time = (timer() - start) * 1000  # s --> ms

print "Found %d in %r ms." % (ans, elapsed_time)