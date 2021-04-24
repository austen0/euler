# Smallest multiple
# Problem 5
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#
# Answer: 232792560

import pefn

m = pefn.math()
u = pefn.utility()


def lcm(x):
    for i in range(5, x + 1):
        m.is_prime(i)
    lcm = 1
    for prime in m.known_primes:
        pwr = 1
        while prime ** pwr <= x:
            lcm = lcm * prime
            pwr += 1
    return lcm


if __name__ == "__main__":
    u.tstart()
    print(lcm(20))
    u.tstop()
