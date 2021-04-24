# 10001st prime
# Problem 7
#
# What is the 10 001st prime number?
#
# Answer: 104743

import pefn

m = pefn.math()
u = pefn.utility()


u.tstart()
i = 5
while len(m.known_primes) < 1e5:
    m.is_prime_turbo(i)
    i += 1
# u.sav(m.known_primes, 'assets/1e5_primes.pickle')
print(m.known_primes[-1])
u.tstop()
