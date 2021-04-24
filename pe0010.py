# Summation of primes
# Problem 10
#
# Find the sum of all the primes below two million.
#
# Answer: 142913828922

import pefn

m = pefn.math()
u = pefn.utility()


u.tstart()
i = max(m.known_primes)
while i < 2e6:
    m.is_prime_turbo(i)
    i += 1
m.save_known_primes_file()
print(sum(m.known_primes))
print(max(m.known_primes))
u.tstop()
